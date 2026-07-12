"""商品库存余额表 API"""

from typing import Optional

from ..client import _BaseAPI


class BalancesAPI(_BaseAPI):
    """商品库存余额表"""

    async def get_wh_list(self, featch_all: int = 0, show_disable_wh: bool = False):
        """
        获取可用的仓库列表.

        POST $SCMAPI_HOST/jxc_api/Balances/GetWhList
        """
        return await self._post(
            "/jxc_api/Balances/GetWhList",
            json_data={
                "FeatchAll": featch_all,
                "ShowDisableWh": show_disable_wh,
            },
        )

    async def search(
        self,
        stock_date: Optional[str] = None,
        wh_ids: Optional[list[int]] = None,
        show_disable_wh: bool = False,
        wh_cat_id: Optional[list[int]] = None,
        prod_ids: Optional[list[int]] = None,
        cat_id: Optional[list[int]] = None,
        spec: Optional[str] = None,
        with_zero: bool = False,
        with_minus: bool = False,
        show_disable_prod: bool = False,
        use_ap: bool = False,
        keyword: Optional[str] = None,
        load_price: bool = True,
        final_stock_flag: bool = False,
        page_index: int = 0,
        page_size: int = 20,
        use_pager: bool = True,
        **kwargs,
    ):
        """
        查询商品库存余额.

        POST $SCMAPI_HOST/jxc_api/Balances/Search
        """
        body = {
            "StockDate": stock_date,
            "WhIds": wh_ids,
            "ShowDisableWh": show_disable_wh,
            "WhCatId": wh_cat_id,
            "ProdIds": prod_ids,
            "CatId": cat_id,
            "Spec": spec,
            "WithZero": with_zero,
            "WithMinus": with_minus,
            "ShowDisableProd": show_disable_prod,
            "UseAP": use_ap,
            "Keyword": keyword,
            "LoadPrice": load_price,
            "FinalStockFlag": final_stock_flag,
            "PageIndex": page_index,
            "PageSize": page_size,
            "UsePager": use_pager,
            **kwargs,
        }
        return await self._post("/jxc_api/Balances/Search", json_data=body)

    async def export(self, **kwargs):
        """导出商品库存余额表."""
        return await self._post("/jxc_api/Balances/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印商品库存余额表."""
        return await self._post("/jxc_api/Balances/Print", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/Balances/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/Balances/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/Balances/ShareExcel", json_data=kwargs)
