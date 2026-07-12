"""销售相关 API"""

from typing import Optional

from ..client import _BaseAPI


class SellDeliveryAPI(_BaseAPI):
    """销售出库单页面"""

    async def init_data(self, **kwargs):
        """初始化销售出库单."""
        return await self._post("/jxc_api/SellDelivery/InitData", json_data=kwargs)

    async def test_return(self, id_: int):
        """测试是否可以生成退货单."""
        return await self._post("/jxc_api/SellDelivery/TestReturn", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """获取上一条销售订单ID."""
        return await self._post("/jxc_api/SellDelivery/GetPrevID", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """获取下一条销售订单ID."""
        return await self._post("/jxc_api/SellDelivery/GetNextID", json_data={"id": id_})

    async def init_from_order(self, **kwargs):
        """使用销售订单初始化单据信息."""
        return await self._post("/jxc_api/SellDelivery/InitDataFromOrder", json_data=kwargs)

    async def init_from_orders(self, **kwargs):
        """从多条销售订单信息初始化入库单信息."""
        return await self._post("/jxc_api/SellDelivery/InitDataFromOrders", json_data=kwargs)

    async def batch_deliver(self, **kwargs):
        """从多条销售订单信息生成入库单记录（批量出库）."""
        return await self._post("/jxc_api/SellDelivery/BatchDelivery", json_data=kwargs)

    async def merge_deliver(self, **kwargs):
        """从多条销售订单信息生成入库单记录（合并出库）."""
        return await self._post("/jxc_api/SellDelivery/MergeDelivery", json_data=kwargs)

    async def init_from_purchase(self, **kwargs):
        """使用采购入库单生成销售出库单."""
        return await self._post("/jxc_api/SellDelivery/InitFromPurInWare", json_data=kwargs)

    async def add(self, **kwargs):
        """添加."""
        return await self._post("/jxc_api/SellDelivery/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改."""
        return await self._post("/jxc_api/SellDelivery/Update", json_data=kwargs)

    async def save_and_audit(self, **kwargs):
        """保存并审核."""
        return await self._post("/jxc_api/SellDelivery/SaveAndAudit", json_data=kwargs)

    async def un_audit(self, id_: int):
        """反审核."""
        return await self._post("/jxc_api/SellDelivery/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除单条记录."""
        return await self._post("/jxc_api/SellDelivery/Delete", json_data={"id": id_})

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/SellDelivery/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/SellDelivery/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/SellDelivery/ShareExcel", json_data=kwargs)

    async def calc_fee(self, **kwargs):
        """获取费用改造数量或者金额发生变化时的数据."""
        return await self._post("/jxc_api/SellDelivery/CalcFee", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/SellDelivery/DraftDetail", json_data=kwargs)


class SellDeliveryListAPI(_BaseAPI):
    """销售出库单列表页面"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/SellDeliveryList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """查询单据及商品详情."""
        return await self._post("/jxc_api/SellDeliveryList/SearchDetail", json_data=kwargs)

    async def batch_audit(self, ids: list[int]):
        """批量审核."""
        return await self._post("/jxc_api/SellDeliveryList/BatchAudit", json_data={"ids": ids})

    async def batch_un_audit(self, ids: list[int]):
        """批量反审核."""
        return await self._post("/jxc_api/SellDeliveryList/BatchUnAudit", json_data={"ids": ids})

    async def batch_delete(self, ids: list[int]):
        """批量删除."""
        return await self._post("/jxc_api/SellDeliveryList/BatchDelete", json_data={"ids": ids})

    async def print_data(self, **kwargs):
        """打印销售出库单."""
        return await self._post("/jxc_api/SellDeliveryList/Print", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellDeliveryList/Export", json_data=kwargs)

    async def download_template(self):
        """下载销售出库单导入模板."""
        return await self._post("/jxc_api/SellDeliveryList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/SellDeliveryList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入销售出库单信息."""
        return await self._post("/jxc_api/SellDeliveryList/Import", json_data=kwargs)

    async def get_return_info(self, **kwargs):
        """获取用于生成退货单的出库单信息."""
        return await self._post("/jxc_api/SellDeliveryList/GetReturnData", json_data=kwargs)

    async def search_invoice(self, **kwargs):
        """搜索发票信息."""
        return await self._post("/jxc_api/SellDeliveryList/SearchInvoice", json_data=kwargs)

    async def register_invoice(self, **kwargs):
        """登记发票."""
        return await self._post("/jxc_api/SellDeliveryList/RegisterInvoice", json_data=kwargs)

    async def cancel_invoice(self, **kwargs):
        """取消登记发票."""
        return await self._post("/jxc_api/SellDeliveryList/CancelInvoice", json_data=kwargs)

    async def batch_cancel_invoice(self, **kwargs):
        """批量取消登记发票."""
        return await self._post("/jxc_api/SellDeliveryList/BatchCancelInvoice", json_data=kwargs)

    async def get_invoice_ids(self, **kwargs):
        """根据单据ID查询关联的发票ID."""
        return await self._post("/jxc_api/SellDeliveryList/GetInvoiceIds", json_data=kwargs)

    async def get_invoice_info(self, **kwargs):
        """根据单据ID查询发票信息."""
        return await self._post("/jxc_api/SellDeliveryList/GetInvoiceInfos", json_data=kwargs)

    async def search_journal(self, **kwargs):
        """搜索日记账."""
        return await self._post("/jxc_api/SellDeliveryList/SearchJournal", json_data=kwargs)

    async def write_off(self, **kwargs):
        """核销."""
        return await self._post("/jxc_api/SellDeliveryList/WriteOff", json_data=kwargs)

    async def manual_write_off(self, **kwargs):
        """手动核销."""
        return await self._post("/jxc_api/SellDeliveryList/ManualWriteOff", json_data=kwargs)

    async def cancel_write_off(self, **kwargs):
        """取消核销."""
        return await self._post("/jxc_api/SellDeliveryList/CancelWriteOff", json_data=kwargs)

    async def get_write_off_ids(self, **kwargs):
        """根据单据ID查询核销记录ID."""
        return await self._post("/jxc_api/SellDeliveryList/GetWriteOffIds", json_data=kwargs)

    async def get_write_off_info(self, **kwargs):
        """根据单据ID核销记录信息."""
        return await self._post("/jxc_api/SellDeliveryList/GetWriteOffInfos", json_data=kwargs)


class SellOrderAPI(_BaseAPI):
    """销售订单"""

    async def init_data(self, **kwargs):
        """初始化销售订单."""
        return await self._post("/jxc_api/SellOrder/InitData", json_data=kwargs)

    async def get_change_log(self, **kwargs):
        """获取变更记录."""
        return await self._post("/jxc_api/SellOrder/GetChangeLog", json_data=kwargs)

    async def export_change_log(self, **kwargs):
        """导出变更记录."""
        return await self._post("/jxc_api/SellOrder/ExportChangeLog", json_data=kwargs)

    async def init_from_purchase_order(self, **kwargs):
        """使用采购订单生成销售订单."""
        return await self._post("/jxc_api/SellOrder/InitDataFromPurOrder", json_data=kwargs)

    async def test_deliver(self, **kwargs):
        """预先判断是否可以生成出库单."""
        return await self._post("/jxc_api/SellOrder/TestDeliver", json_data=kwargs)

    async def get_prev_id(self, id_: int):
        """获取上一条销售订单ID."""
        return await self._post("/jxc_api/SellOrder/GetPrevID", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """获取下一条销售订单ID."""
        return await self._post("/jxc_api/SellOrder/GetNextID", json_data={"id": id_})

    async def add(self, **kwargs):
        """添加销售订单."""
        return await self._post("/jxc_api/SellOrder/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改销售订单."""
        return await self._post("/jxc_api/SellOrder/Update", json_data=kwargs)

    async def change_order(self, **kwargs):
        """变更销售订单."""
        return await self._post("/jxc_api/SellOrder/Change", json_data=kwargs)

    async def save_and_audit(self, **kwargs):
        """保存并审核."""
        return await self._post("/jxc_api/SellOrder/SaveAndAudit", json_data=kwargs)

    async def un_audit(self, id_: int):
        """反审核销售订单."""
        return await self._post("/jxc_api/SellOrder/UnAudit", json_data={"id": id_})

    async def close(self, id_: int):
        """关闭销售订单."""
        return await self._post("/jxc_api/SellOrder/Close", json_data={"id": id_})

    async def open(self, id_: int):
        """开启销售订单."""
        return await self._post("/jxc_api/SellOrder/Open", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除单条记录."""
        return await self._post("/jxc_api/SellOrder/Delete", json_data={"id": id_})

    async def get_recent_price(self, **kwargs):
        """获得最近的价格."""
        return await self._post("/jxc_api/SellOrder/GetRecentPrice", json_data=kwargs)

    async def get_recent_prices(self, **kwargs):
        """批量获得最近的价格."""
        return await self._post("/jxc_api/SellOrder/GetRecentPrices", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/SellOrder/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/SellOrder/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/SellOrder/ShareExcel", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/SellOrder/DraftDetail", json_data=kwargs)


class SellOrderListAPI(_BaseAPI):
    """销售订单列表页面"""

    async def search(self, **kwargs):
        """检索销售订单."""
        return await self._post("/jxc_api/SellOrderList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """查询单据及商品详情."""
        return await self._post("/jxc_api/SellOrderList/SearchDetail", json_data=kwargs)

    async def batch_audit(self, ids: list[int]):
        """批量审核."""
        return await self._post("/jxc_api/SellOrderList/BatchAudit", json_data={"ids": ids})

    async def batch_un_audit(self, ids: list[int]):
        """批量反审核."""
        return await self._post("/jxc_api/SellOrderList/BatchUnAudit", json_data={"ids": ids})

    async def batch_delete(self, ids: list[int]):
        """批量删除."""
        return await self._post("/jxc_api/SellOrderList/BatchDelete", json_data={"ids": ids})

    async def batch_close(self, ids: list[int]):
        """批量关闭."""
        return await self._post("/jxc_api/SellOrderList/BatchClose", json_data={"ids": ids})

    async def batch_close_by_detail(self, **kwargs):
        """按明细批量关闭."""
        return await self._post("/jxc_api/SellOrderList/BatchCloseByDetail", json_data=kwargs)

    async def batch_open(self, ids: list[int]):
        """批量启用."""
        return await self._post("/jxc_api/SellOrderList/BatchOpen", json_data={"ids": ids})

    async def batch_open_by_detail(self, **kwargs):
        """按明细批量启用."""
        return await self._post("/jxc_api/SellOrderList/BatchOpenByDetail", json_data=kwargs)

    async def batch_lock(self, ids: list[int]):
        """批量锁定."""
        return await self._post("/jxc_api/SellOrderList/BatchLock", json_data={"ids": ids})

    async def batch_unlock(self, ids: list[int]):
        """批量解锁."""
        return await self._post("/jxc_api/SellOrderList/BatchUnlock", json_data={"ids": ids})

    async def print_data(self, **kwargs):
        """打印销售订单."""
        return await self._post("/jxc_api/SellOrderList/Print", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellOrderList/Export", json_data=kwargs)

    async def download_template(self):
        """下载销售订单导入模板."""
        return await self._post("/jxc_api/SellOrderList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/SellOrderList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入销售订单记录."""
        return await self._post("/jxc_api/SellOrderList/Import", json_data=kwargs)

    async def get_deliver_info(self, **kwargs):
        """获取用于出库单的订单信息."""
        return await self._post("/jxc_api/SellOrderList/GetDeliverData", json_data=kwargs)


class SellReturnAPI(_BaseAPI):
    """销售退货单页面"""

    async def init_data(self, **kwargs):
        """初始化销售出库单."""
        return await self._post("/jxc_api/SellReturn/InitData", json_data=kwargs)

    async def get_default_prices(self, **kwargs):
        """获取一组商品默认价格信息."""
        return await self._post("/jxc_api/SellReturn/GetDefaultPrices", json_data=kwargs)

    async def get_prev_id(self, id_: int):
        """获取上一条销售订单ID."""
        return await self._post("/jxc_api/SellReturn/GetPrevID", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """获取下一条销售订单ID."""
        return await self._post("/jxc_api/SellReturn/GetNextID", json_data={"id": id_})

    async def init_from_order(self, **kwargs):
        """使用销售订单初始化销售退货单信息."""
        return await self._post("/jxc_api/SellReturn/InitDataFromOrder", json_data=kwargs)

    async def init_from_orders(self, **kwargs):
        """从多条销售订单信息初始化退货单信息."""
        return await self._post("/jxc_api/SellReturn/InitDataFromOrders", json_data=kwargs)

    async def init_from_delivery(self, **kwargs):
        """使用销售出库单初始化销售退货单信息."""
        return await self._post("/jxc_api/SellReturn/InitDataFromDelivery", json_data=kwargs)

    async def add(self, **kwargs):
        """添加."""
        return await self._post("/jxc_api/SellReturn/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改."""
        return await self._post("/jxc_api/SellReturn/Update", json_data=kwargs)

    async def save_and_audit(self, **kwargs):
        """保存并审核."""
        return await self._post("/jxc_api/SellReturn/SaveAndAudit", json_data=kwargs)

    async def un_audit(self, id_: int):
        """反审核."""
        return await self._post("/jxc_api/SellReturn/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除单条记录."""
        return await self._post("/jxc_api/SellReturn/Delete", json_data={"id": id_})

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/SellReturn/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/SellReturn/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/SellReturn/ShareExcel", json_data=kwargs)

    async def calc_fee(self, **kwargs):
        """获取费用改造数据."""
        return await self._post("/jxc_api/SellReturn/CalcFee", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/SellReturn/DraftDetail", json_data=kwargs)


class SellReturnListAPI(_BaseAPI):
    """销售退货单列表页面"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/SellReturnList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """查询单据及商品详情."""
        return await self._post("/jxc_api/SellReturnList/SearchDetail", json_data=kwargs)

    async def batch_audit(self, ids: list[int]):
        """批量审核."""
        return await self._post("/jxc_api/SellReturnList/BatchAudit", json_data={"ids": ids})

    async def batch_un_audit(self, ids: list[int]):
        """批量反审核."""
        return await self._post("/jxc_api/SellReturnList/BatchUnAudit", json_data={"ids": ids})

    async def batch_delete(self, ids: list[int]):
        """批量删除."""
        return await self._post("/jxc_api/SellReturnList/BatchDelete", json_data={"ids": ids})

    async def print_data(self, **kwargs):
        """打印销售退货单."""
        return await self._post("/jxc_api/SellReturnList/Print", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellReturnList/Export", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/SellReturnList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/SellReturnList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入销售退货单记录."""
        return await self._post("/jxc_api/SellReturnList/Import", json_data=kwargs)

    async def search_invoice(self, **kwargs):
        """搜索发票信息."""
        return await self._post("/jxc_api/SellReturnList/SearchInvoice", json_data=kwargs)

    async def register_invoice(self, **kwargs):
        """登记发票."""
        return await self._post("/jxc_api/SellReturnList/RegisterInvoice", json_data=kwargs)

    async def cancel_invoice(self, **kwargs):
        """取消登记发票."""
        return await self._post("/jxc_api/SellReturnList/CancelInvoice", json_data=kwargs)

    async def batch_cancel_invoice(self, **kwargs):
        """批量取消登记发票."""
        return await self._post("/jxc_api/SellReturnList/BatchCancelInvoice", json_data=kwargs)

    async def get_invoice_ids(self, **kwargs):
        """根据单据ID查询关联的发票ID."""
        return await self._post("/jxc_api/SellReturnList/GetInvoiceIds", json_data=kwargs)

    async def get_invoice_info(self, **kwargs):
        """根据单据ID查询发票信息."""
        return await self._post("/jxc_api/SellReturnList/GetInvoiceInfos", json_data=kwargs)

    async def search_journal(self, **kwargs):
        """搜索日记账."""
        return await self._post("/jxc_api/SellReturnList/SearchJournal", json_data=kwargs)

    async def write_off(self, **kwargs):
        """核销."""
        return await self._post("/jxc_api/SellReturnList/WriteOff", json_data=kwargs)

    async def manual_write_off(self, **kwargs):
        """手动核销."""
        return await self._post("/jxc_api/SellReturnList/ManualWriteOff", json_data=kwargs)

    async def cancel_write_off(self, **kwargs):
        """取消核销."""
        return await self._post("/jxc_api/SellReturnList/CancelWriteOff", json_data=kwargs)

    async def get_write_off_ids(self, **kwargs):
        """根据单据ID查询核销记录ID."""
        return await self._post("/jxc_api/SellReturnList/GetWriteOffIds", json_data=kwargs)

    async def get_write_off_info(self, **kwargs):
        """根据单据ID核销记录信息."""
        return await self._post("/jxc_api/SellReturnList/GetWriteOffInfos", json_data=kwargs)
