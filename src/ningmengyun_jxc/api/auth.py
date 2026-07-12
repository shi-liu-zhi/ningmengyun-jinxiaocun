"""认证与授权接口 - OAuth2 / 获取账号授权 / 单点登录 / 页面嵌入"""

from ..client import _BaseAPI


class AuthAPI(_BaseAPI):
    """认证与授权相关接口"""

    async def get_token(self, app_id: str, app_secret: str) -> dict:
        """
        获取访问令牌 (OAuth2).

        POST $ACCOUNTOPEN_HOST/oauth2/token
        """
        return await self._post(
            "/oauth2/token",
            json_data={"app_id": app_id, "app_secret": app_secret},
        )

    async def refresh_token(self, refresh_token: str) -> dict:
        """刷新令牌"""
        return await self._post(
            "/oauth2/refresh",
            json_data={"refresh_token": refresh_token},
        )

    async def get_account_books(self) -> dict:
        """
        获取账套列表.

        POST $ACCOUNTOPEN_HOST/api/AccountBooks/GetAccountBooks
        """
        return await self._post("/api/AccountBooks/GetAccountBooks")

    async def set_account_book_session(self, account_book_id: str) -> dict:
        """
        设置账套会话 - 获取cookie/token用于页面嵌入.

        POST $ACCOUNTPC_HOST/Home/SetAccountBookSession
        """
        return await self._post(
            "/Home/SetAccountBookSession",
            json_data={"accountBookId": account_book_id},
        )

    async def sso_login(self, account_book_id: str, user_name: str, password: str) -> dict:
        """
        单点登录 - 获取用户凭证.

        POST $ACCOUNTOPEN_HOST/api/SSO/Login
        """
        return await self._post(
            "/api/SSO/Login",
            json_data={
                "accountBookId": account_book_id,
                "userName": user_name,
                "password": password,
            },
        )
