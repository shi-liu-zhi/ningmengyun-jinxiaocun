"""采购相关 API"""

from typing import Optional

from ..client import _BaseAPI


class PurchaseOrderAPI(_BaseAPI):
    """采购订单页面"""

    async def test_return(self, **kwargs):
        """预测试是否可以生成入库单，退货单."""
        return await self._post("/jxc_api/PurchaseOrder/TestReturn", json_data=kwargs)

    async def get_by_id(self, id_: int):
        """获取一条单据信息."""
        return await self._post("/jxc_api/PurchaseOrder/GetById", json_data={"id": id_})

    async def init_from_warning(self, **kwargs):
        """使用库存预警相关的商品初始化采购订单信息."""
        return await self._post("/jxc_api/PurchaseOrder/InitFromWarning", json_data=kwargs)

    async def get_change_log(self, **kwargs):
        """获取变更记录."""
        return await self._post("/jxc_api/PurchaseOrder/GetChangeLog", json_data=kwargs)

    async def export_change_log(self, **kwargs):
        """导出变更记录."""
        return await self._post("/jxc_api/PurchaseOrder/ExportChangeLog", json_data=kwargs)

    async def init_from_sale_order(self, **kwargs):
        """使用销售订单生成采购订单."""
        return await self._post("/jxc_api/PurchaseOrder/InitFromSaleOrder", json_data=kwargs)

    async def get_prev_id(self, id_: int):
        """获取上一条采购订单ID."""
        return await self._post("/jxc_api/PurchaseOrder/GetPrevID", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """获取下一条采购订单ID."""
        return await self._post("/jxc_api/PurchaseOrder/GetNextID", json_data={"id": id_})

    async def add(self, **kwargs):
        """添加采购订单."""
        return await self._post("/jxc_api/PurchaseOrder/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改采购订单."""
        return await self._post("/jxc_api/PurchaseOrder/Update", json_data=kwargs)

    async def change(self, **kwargs):
        """变更采购订单."""
        return await self._post("/jxc_api/PurchaseOrder/Change", json_data=kwargs)

    async def delete(self, id_: int):
        """删除单条记录."""
        return await self._post("/jxc_api/PurchaseOrder/Delete", json_data={"id": id_})

    async def save_and_audit(self, **kwargs):
        """保存并审核."""
        return await self._post("/jxc_api/PurchaseOrder/SaveAndAudit", json_data=kwargs)

    async def un_audit(self, id_: int):
        """反审核."""
        return await self._post("/jxc_api/PurchaseOrder/UnAudit", json_data={"id": id_})

    async def get_recent_price(self, **kwargs):
        """获得最近的价格."""
        return await self._post("/jxc_api/PurchaseOrder/GetRecentPrice", json_data=kwargs)

    async def get_recent_prices(self, **kwargs):
        """批量获取获得最近的价格."""
        return await self._post("/jxc_api/PurchaseOrder/GetRecentPrices", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/PurchaseOrder/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/PurchaseOrder/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/PurchaseOrder/ShareExcel", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/PurchaseOrder/DraftDetail", json_data=kwargs)


class PurchaseOrderListAPI(_BaseAPI):
    """采购订单列表页面"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/PurchaseOrderList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """检索带有商品明细."""
        return await self._post("/jxc_api/PurchaseOrderList/SearchDetail", json_data=kwargs)

    async def batch_audit(self, ids: list[int]):
        """批量审核."""
        return await self._post("/jxc_api/PurchaseOrderList/BatchAudit", json_data={"ids": ids})

    async def batch_un_audit(self, ids: list[int]):
        """批量反审核."""
        return await self._post("/jxc_api/PurchaseOrderList/BatchUnAudit", json_data={"ids": ids})

    async def batch_delete(self, ids: list[int]):
        """批量删除."""
        return await self._post("/jxc_api/PurchaseOrderList/BatchDelete", json_data={"ids": ids})

    async def print_data(self, **kwargs):
        """打印采购订单."""
        return await self._post("/jxc_api/PurchaseOrderList/Print", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/PurchaseOrderList/Export", json_data=kwargs)

    async def batch_close(self, ids: list[int]):
        """批量关闭."""
        return await self._post("/jxc_api/PurchaseOrderList/BatchClose", json_data={"ids": ids})

    async def batch_open(self, ids: list[int]):
        """批量开启."""
        return await self._post("/jxc_api/PurchaseOrderList/BatchOpen", json_data={"ids": ids})

    async def download_template(self):
        """下载采购订单导入模板."""
        return await self._post("/jxc_api/PurchaseOrderList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/PurchaseOrderList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入采购订单记录."""
        return await self._post("/jxc_api/PurchaseOrderList/Import", json_data=kwargs)

    async def get_warehousing_info(self, **kwargs):
        """获取用于生成入库单的订单信息."""
        return await self._post("/jxc_api/PurchaseOrderList/GetWarehousingData", json_data=kwargs)


class WarehousingAPI(_BaseAPI):
    """采购入库单页面"""

    async def test_return(self, **kwargs):
        """预测试是否可以生成退货单."""
        return await self._post("/jxc_api/Warehousing/TestReturn", json_data=kwargs)

    async def init_data(self, **kwargs):
        """初始化单据信息."""
        return await self._post("/jxc_api/Warehousing/InitData", json_data=kwargs)

    async def init_from_warning(self, **kwargs):
        """使用库存预警相关的商品初始化采购入库单信息."""
        return await self._post("/jxc_api/Warehousing/InitFromWarning", json_data=kwargs)

    async def init_from_order(self, **kwargs):
        """从一条采购订单信息初始化入库单据信息."""
        return await self._post("/jxc_api/Warehousing/InitDataFromOrder", json_data=kwargs)

    async def init_from_orders(self, **kwargs):
        """从多条采购订单信息初始化入库单信息."""
        return await self._post("/jxc_api/Warehousing/InitDataFromOrders", json_data=kwargs)

    async def batch_warehouse(self, **kwargs):
        """批量入库."""
        return await self._post("/jxc_api/Warehousing/BatchWarehousing", json_data=kwargs)

    async def merge_warehouse(self, **kwargs):
        """合并入库."""
        return await self._post("/jxc_api/Warehousing/MergeWarehousing", json_data=kwargs)

    async def init_from_sell_delivery(self, **kwargs):
        """使用销售出库单生成采购入库单."""
        return await self._post("/jxc_api/Warehousing/InitFromSellDelivery", json_data=kwargs)

    async def add(self, **kwargs):
        """添加采购入库单."""
        return await self._post("/jxc_api/Warehousing/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改采购入库单."""
        return await self._post("/jxc_api/Warehousing/Update", json_data=kwargs)

    async def save_and_audit(self, **kwargs):
        """保存并审核."""
        return await self._post("/jxc_api/Warehousing/SaveAndAudit", json_data=kwargs)

    async def un_audit(self, id_: int):
        """反审核."""
        return await self._post("/jxc_api/Warehousing/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除单条单据."""
        return await self._post("/jxc_api/Warehousing/Delete", json_data={"id": id_})

    async def query_serial_no(self, **kwargs):
        """查询未出库的序列号."""
        return await self._post("/jxc_api/Warehousing/GetSerialNo", json_data=kwargs)

    async def query_batch_no(self, **kwargs):
        """查找未出库的批次号."""
        return await self._post("/jxc_api/Warehousing/GetBatchNo", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/Warehousing/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/Warehousing/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/Warehousing/ShareExcel", json_data=kwargs)

    async def calc_fee(self, **kwargs):
        """获取费用改造数据."""
        return await self._post("/jxc_api/Warehousing/CalcFee", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/Warehousing/DraftDetail", json_data=kwargs)


class WarehousingListAPI(_BaseAPI):
    """采购入库单列表页面"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/WarehousingList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """检索明细."""
        return await self._post("/jxc_api/WarehousingList/SearchDetail", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/WarehousingList/Export", json_data=kwargs)

    async def batch_audit(self, ids: list[int]):
        """批量审核."""
        return await self._post("/jxc_api/WarehousingList/BatchAudit", json_data={"ids": ids})

    async def batch_un_audit(self, ids: list[int]):
        """批量反审核."""
        return await self._post("/jxc_api/WarehousingList/BatchUnAudit", json_data={"ids": ids})

    async def batch_delete(self, ids: list[int]):
        """批量删除."""
        return await self._post("/jxc_api/WarehousingList/BatchDelete", json_data={"ids": ids})

    async def print_data(self, **kwargs):
        """打印采购入库单."""
        return await self._post("/jxc_api/WarehousingList/Print", json_data=kwargs)

    async def download_template(self):
        """下载采购入库单导入模板."""
        return await self._post("/jxc_api/WarehousingList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/WarehousingList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入采购入库单."""
        return await self._post("/jxc_api/WarehousingList/Import", json_data=kwargs)

    async def get_return_info(self, **kwargs):
        """获取用于生成退货单的入库单信息."""
        return await self._post("/jxc_api/WarehousingList/GetReturnData", json_data=kwargs)

    async def search_invoice(self, **kwargs):
        """搜索发票信息."""
        return await self._post("/jxc_api/WarehousingList/SearchInvoice", json_data=kwargs)

    async def register_invoice(self, **kwargs):
        """登记发票."""
        return await self._post("/jxc_api/WarehousingList/RegisterInvoice", json_data=kwargs)

    async def cancel_invoice(self, **kwargs):
        """取消登记发票."""
        return await self._post("/jxc_api/WarehousingList/CancelInvoice", json_data=kwargs)

    async def batch_cancel_invoice(self, **kwargs):
        """批量取消登记发票."""
        return await self._post("/jxc_api/WarehousingList/BatchCancelInvoice", json_data=kwargs)

    async def get_invoice_ids(self, **kwargs):
        """根据单据ID查询关联的发票ID."""
        return await self._post("/jxc_api/WarehousingList/GetInvoiceIds", json_data=kwargs)

    async def get_invoice_info(self, **kwargs):
        """根据单据ID查询发票信息."""
        return await self._post("/jxc_api/WarehousingList/GetInvoiceInfos", json_data=kwargs)

    async def search_journal(self, **kwargs):
        """搜索日记账."""
        return await self._post("/jxc_api/WarehousingList/SearchJournal", json_data=kwargs)

    async def write_off(self, **kwargs):
        """核销."""
        return await self._post("/jxc_api/WarehousingList/WriteOff", json_data=kwargs)

    async def manual_write_off(self, **kwargs):
        """手动核销."""
        return await self._post("/jxc_api/WarehousingList/ManualWriteOff", json_data=kwargs)

    async def cancel_write_off(self, **kwargs):
        """取消核销."""
        return await self._post("/jxc_api/WarehousingList/CancelWriteOff", json_data=kwargs)

    async def get_write_off_ids(self, **kwargs):
        """根据单据ID查询核销记录ID."""
        return await self._post("/jxc_api/WarehousingList/GetWriteOffIds", json_data=kwargs)

    async def get_write_off_info(self, **kwargs):
        """根据单据ID核销记录信息."""
        return await self._post("/jxc_api/WarehousingList/GetWriteOffInfos", json_data=kwargs)


class WarehousingReturnAPI(_BaseAPI):
    """采购退货单页面"""

    async def init_data(self, **kwargs):
        """初始化单据信息."""
        return await self._post("/jxc_api/WarehousingReturn/InitData", json_data=kwargs)

    async def get_prev_id(self, id_: int):
        """获取上一条单据ID."""
        return await self._post("/jxc_api/WarehousingReturn/GetPrevID", json_data={"id": id_})

    async def init_from_purchase_order(self, **kwargs):
        """从一条采购订单信息初始化退货单信息."""
        return await self._post("/jxc_api/WarehousingReturn/InitFromPurOrder", json_data=kwargs)

    async def init_from_purchase_orders(self, **kwargs):
        """从多条采购订单信息初始化退货单信息."""
        return await self._post("/jxc_api/WarehousingReturn/InitFromPurOrders", json_data=kwargs)

    async def init_from_warehousing(self, **kwargs):
        """从一条采购入库单信息初始化退货单信息."""
        return await self._post("/jxc_api/WarehousingReturn/InitFromWarehousing", json_data=kwargs)

    async def init_from_warehousing_multi(self, **kwargs):
        """从多条采购入库单信息初始化退货单信息."""
        return await self._post("/jxc_api/WarehousingReturn/InitFromWarehousingMulti", json_data=kwargs)

    async def add(self, **kwargs):
        """添加."""
        return await self._post("/jxc_api/WarehousingReturn/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改."""
        return await self._post("/jxc_api/WarehousingReturn/Update", json_data=kwargs)

    async def save_and_audit(self, **kwargs):
        """保存并审核."""
        return await self._post("/jxc_api/WarehousingReturn/SaveAndAudit", json_data=kwargs)

    async def un_audit(self, id_: int):
        """反审核."""
        return await self._post("/jxc_api/WarehousingReturn/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除单条记录."""
        return await self._post("/jxc_api/WarehousingReturn/Delete", json_data={"id": id_})

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/WarehousingReturn/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/WarehousingReturn/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/WarehousingReturn/ShareExcel", json_data=kwargs)

    async def calc_fee(self, **kwargs):
        """获取费用改造数据."""
        return await self._post("/jxc_api/WarehousingReturn/CalcFee", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/WarehousingReturn/DraftDetail", json_data=kwargs)


class WarehousingReturnListAPI(_BaseAPI):
    """采购退货单列表页面"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/WarehousingReturnList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """检索商品明细."""
        return await self._post("/jxc_api/WarehousingReturnList/SearchDetail", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/WarehousingReturnList/Export", json_data=kwargs)

    async def batch_audit(self, ids: list[int]):
        """批量审核."""
        return await self._post("/jxc_api/WarehousingReturnList/BatchAudit", json_data={"ids": ids})

    async def batch_un_audit(self, ids: list[int]):
        """批量反审核."""
        return await self._post("/jxc_api/WarehousingReturnList/BatchUnAudit", json_data={"ids": ids})

    async def batch_delete(self, ids: list[int]):
        """批量删除."""
        return await self._post("/jxc_api/WarehousingReturnList/BatchDelete", json_data={"ids": ids})

    async def print_data(self, **kwargs):
        """打印采购退货单."""
        return await self._post("/jxc_api/WarehousingReturnList/Print", json_data=kwargs)

    async def download_template(self):
        """下载采购退货单导入模板."""
        return await self._post("/jxc_api/WarehousingReturnList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/WarehousingReturnList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入采购退货单."""
        return await self._post("/jxc_api/WarehousingReturnList/Import", json_data=kwargs)

    async def search_invoice(self, **kwargs):
        """搜索发票信息."""
        return await self._post("/jxc_api/WarehousingReturnList/SearchInvoice", json_data=kwargs)

    async def register_invoice(self, **kwargs):
        """登记发票."""
        return await self._post("/jxc_api/WarehousingReturnList/RegisterInvoice", json_data=kwargs)

    async def cancel_invoice(self, **kwargs):
        """取消登记发票."""
        return await self._post("/jxc_api/WarehousingReturnList/CancelInvoice", json_data=kwargs)

    async def batch_cancel_invoice(self, **kwargs):
        """批量取消登记发票."""
        return await self._post("/jxc_api/WarehousingReturnList/BatchCancelInvoice", json_data=kwargs)

    async def get_invoice_ids(self, **kwargs):
        """根据单据ID查询关联的发票ID."""
        return await self._post("/jxc_api/WarehousingReturnList/GetInvoiceIds", json_data=kwargs)

    async def get_invoice_info(self, **kwargs):
        """根据单据ID查询发票信息."""
        return await self._post("/jxc_api/WarehousingReturnList/GetInvoiceInfos", json_data=kwargs)

    async def search_journal(self, **kwargs):
        """搜索日记账."""
        return await self._post("/jxc_api/WarehousingReturnList/SearchJournal", json_data=kwargs)

    async def write_off(self, **kwargs):
        """核销."""
        return await self._post("/jxc_api/WarehousingReturnList/WriteOff", json_data=kwargs)

    async def manual_write_off(self, **kwargs):
        """手动核销."""
        return await self._post("/jxc_api/WarehousingReturnList/ManualWriteOff", json_data=kwargs)

    async def cancel_write_off(self, **kwargs):
        """取消核销."""
        return await self._post("/jxc_api/WarehousingReturnList/CancelWriteOff", json_data=kwargs)

    async def get_write_off_ids(self, **kwargs):
        """根据单据ID查询核销记录ID."""
        return await self._post("/jxc_api/WarehousingReturnList/GetWriteOffIds", json_data=kwargs)

    async def get_write_off_info(self, **kwargs):
        """根据单据ID核销记录信息."""
        return await self._post("/jxc_api/WarehousingReturnList/GetWriteOffInfos", json_data=kwargs)
