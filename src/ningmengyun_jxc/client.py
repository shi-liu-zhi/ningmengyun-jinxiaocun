"""Main async HTTP client for 柠檬云进销存 API."""

from __future__ import annotations

import json
from typing import Any, Optional
from urllib.parse import urlencode

import httpx

from .exceptions import JxcApiError, JxcAuthError
from .models import ApiResult

# ── Hosts ────────────────────────────────────────────────────────────

PRODUCTION_HOST = "https://jxcapi.ningmengyun.com"
TEST_HOST = "http://scmtestapi.ningmengyun.com"

# ── State constants ──────────────────────────────────────────────────

STATE_SUCCESS = 1000
STATE_BIZ_FAIL = 2000
STATE_API_FAIL = 9999


class _BaseAPI:
    """Base class for API resource groups."""

    def __init__(self, client: "JxcClient"):
        self._client = client

    def _build_url(self, path: str) -> str:
        return f"{self._client.base_url}{path}"

    async def _request(
        self,
        method: str,
        path: str,
        params: Optional[dict] = None,
        json_data: Any = None,
        headers: Optional[dict] = None,
        **kwargs,
    ) -> ApiResult:
        url = self._build_url(path)
        req_headers = self._client._get_headers()
        if headers:
            req_headers.update(headers)

        # Build query string from params if any
        request_params = None
        if params:
            # Filter out None values
            filtered = {k: v for k, v in params.items() if v is not None}
            request_params = filtered

        # If json_data is a dict, filter out None values too
        if isinstance(json_data, dict):
            json_data = {k: v for k, v in json_data.items() if v is not None}
        elif isinstance(json_data, list):
            json_data = [
                {k: v for k, v in item.items() if v is not None}
                if isinstance(item, dict)
                else item
                for item in json_data
            ]

        resp = await self._client._session.request(
            method,
            url,
            params=request_params,
            json=json_data,
            headers=req_headers,
            **kwargs,
        )
        return self._client._handle_response(resp)

    async def _get(self, path: str, params: Optional[dict] = None, **kwargs) -> ApiResult:
        return await self._request("GET", path, params=params, **kwargs)

    async def _post(self, path: str, json_data: Any = None, params: Optional[dict] = None, **kwargs) -> ApiResult:
        return await self._request("POST", path, json_data=json_data, params=params, **kwargs)


class JxcClient:
    """
    柠檬云进销存异步客户端.

    Args:
        token: Bearer token for authentication.
        account_book_id: 账套ID.
        env: "production" (default) or "test".
        base_url: Custom base URL (overrides env).
        timeout: HTTP timeout in seconds (default 30).
    """

    def __init__(
        self,
        token: str = "",
        account_book_id: str = "",
        env: str = "production",
        base_url: Optional[str] = None,
        timeout: float = 30.0,
    ):
        self.token = token
        self.account_book_id = account_book_id

        if base_url:
            self.base_url = base_url
        elif env == "test":
            self.base_url = TEST_HOST
        else:
            self.base_url = PRODUCTION_HOST

        self._session: httpx.AsyncClient = httpx.AsyncClient(
            timeout=httpx.Timeout(timeout),
        )
        self._closed = False

        # ── API resource groups (lazy-initialized) ──
        self._apis: dict[str, _BaseAPI] = {}

    def _get_headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        if self.account_book_id:
            headers["AccountBookId"] = self.account_book_id
        return headers

    @staticmethod
    def _handle_response(resp: httpx.Response) -> ApiResult:
        try:
            body = resp.json()
        except json.JSONDecodeError:
            raise JxcApiError(
                state=STATE_API_FAIL,
                msg=f"Invalid JSON response: {resp.text[:200]}",
            )

        state = body.get("State", STATE_API_FAIL)
        sub_state = body.get("SubState", 0)
        msg = body.get("Msg", "")
        data = body.get("Data")

        result = ApiResult(state=state, sub_state=sub_state, msg=msg, data=data)

        if state == STATE_API_FAIL:
            if "token" in msg.lower() or "认证" in msg or "授权" in msg:
                raise JxcAuthError(state, msg, data)
            raise JxcApiError(state, msg, data)

        if state == STATE_BIZ_FAIL:
            raise JxcApiError(state, msg, data)

        return result

    def _register_api(self, name: str, api: _BaseAPI):
        self._apis[name] = api

    def __getattr__(self, name: str):
        # Allow access to registered APIs as attributes
        if name in self._apis:
            return self._apis[name]
        raise AttributeError(f"'{type(self).__name__}' has no attribute '{name}'")

    async def aclose(self):
        """Close the underlying HTTP session."""
        if not self._closed:
            self._closed = True
            await self._session.aclose()

    async def __aenter__(self):
        return self

    async def __aexit__(self, *args):
        await self.aclose()
