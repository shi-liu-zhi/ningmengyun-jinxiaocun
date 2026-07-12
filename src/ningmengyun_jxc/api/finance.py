"""财务相关 API: 收款/付款/转账/核销/费用"""

from ..client import _BaseAPI


class ReceiptAPI(_BaseAPI):
    """收款单的添加，更新，审核等"""

    async def get_by_id(self, id_: int):
        """根据ID获得收款单."""
        return await self._post("/jxc_api/Receipt/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增收款单."""
        return await self._post("/jxc_api/Receipt/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改收款单."""
        return await self._post("/jxc_api/Receipt/Update", json_data=kwargs)

    async def audit(self, id_: int):
        """审核收款单."""
        return await self._post("/jxc_api/Receipt/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核收款单."""
        return await self._post("/jxc_api/Receipt/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除收款单."""
        return await self._post("/jxc_api/Receipt/Delete", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """下一条单据ID."""
        return await self._post("/jxc_api/Receipt/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """上一条单据ID."""
        return await self._post("/jxc_api/Receipt/GetPrevID", json_data={"id": id_})

    async def get_customer_debt(self, **kwargs):
        """获得客户的欠款."""
        return await self._post("/jxc_api/Receipt/GetCustomerDebt", json_data=kwargs)

    async def refresh(self, id_: int):
        """刷新收款单数据."""
        return await self._post("/jxc_api/Receipt/Refresh", json_data={"id": id_})

    async def get_source_data(self, **kwargs):
        """获得收款单所核销的源单的数据."""
        return await self._post("/jxc_api/Receipt/GetSourceData", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/Receipt/ShareExcel", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/Receipt/SharePDF", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/Receipt/ShareLink", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/Receipt/DraftDetail", json_data=kwargs)


class ReceiptListAPI(_BaseAPI):
    """收款单列表"""

    async def delete(self, ids: list[int]):
        """删除收款单."""
        return await self._post("/jxc_api/ReceiptList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核收款单."""
        return await self._post("/jxc_api/ReceiptList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核收款单."""
        return await self._post("/jxc_api/ReceiptList/UnAudit", json_data={"ids": ids})

    async def search(self, **kwargs):
        """搜索收款单列表."""
        return await self._post("/jxc_api/ReceiptList/Search", json_data=kwargs)

    async def get_by_order_no(self, order_no: str):
        """第三方根据订单编号取对应的收款单."""
        return await self._post("/jxc_api/ReceiptList/GetByOrderNo", json_data={"orderNo": order_no})

    async def export_data(self, **kwargs):
        """导出收款单数据."""
        return await self._post("/jxc_api/ReceiptList/Export", json_data=kwargs)

    async def download_template(self):
        """下载收款单导入模板."""
        return await self._post("/jxc_api/ReceiptList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载导入收款单失败后的错误数据."""
        return await self._post("/jxc_api/ReceiptList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入收款单."""
        return await self._post("/jxc_api/ReceiptList/Import", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印收款单."""
        return await self._post("/jxc_api/ReceiptList/Print", json_data=kwargs)


class PaymentAPI(_BaseAPI):
    """付款单的添加，更新，审核等"""

    async def get_by_id(self, id_: int):
        """根据ID获得付款单."""
        return await self._post("/jxc_api/Payment/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增付款单."""
        return await self._post("/jxc_api/Payment/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改付款单."""
        return await self._post("/jxc_api/Payment/Update", json_data=kwargs)

    async def audit(self, id_: int):
        """审核付款单."""
        return await self._post("/jxc_api/Payment/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核付款单."""
        return await self._post("/jxc_api/Payment/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除付款单."""
        return await self._post("/jxc_api/Payment/Delete", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """下一条单据ID."""
        return await self._post("/jxc_api/Payment/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """上一条单据ID."""
        return await self._post("/jxc_api/Payment/GetPrevID", json_data={"id": id_})

    async def refresh(self, id_: int):
        """刷新付款单数据."""
        return await self._post("/jxc_api/Payment/Refresh", json_data={"id": id_})

    async def get_source_data(self, **kwargs):
        """获得源单列表数据."""
        return await self._post("/jxc_api/Payment/GetSourceData", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/Payment/ShareExcel", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/Payment/SharePDF", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/Payment/ShareLink", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/Payment/DraftDetail", json_data=kwargs)


class PaymentListAPI(_BaseAPI):
    """付款单列表"""

    async def delete(self, ids: list[int]):
        """删除付款单."""
        return await self._post("/jxc_api/PaymentList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核付款单."""
        return await self._post("/jxc_api/PaymentList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核付款单."""
        return await self._post("/jxc_api/PaymentList/UnAudit", json_data={"ids": ids})

    async def search(self, **kwargs):
        """搜索付款单列表."""
        return await self._post("/jxc_api/PaymentList/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出付款单数据."""
        return await self._post("/jxc_api/PaymentList/Export", json_data=kwargs)

    async def download_template(self):
        """下载付款单导入模板."""
        return await self._post("/jxc_api/PaymentList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载导入付款单失败后的错误数据."""
        return await self._post("/jxc_api/PaymentList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入付款单."""
        return await self._post("/jxc_api/PaymentList/Import", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印付款单."""
        return await self._post("/jxc_api/PaymentList/Print", json_data=kwargs)


class AccountTransferAPI(_BaseAPI):
    """转账单的添加，更新，审核，打印等"""

    async def get_by_id(self, id_: int = None):
        """获得空白的转账单对象，或者根据传入的ID获得转账单对象."""
        return await self._post("/jxc_api/AccountTransfer/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增转账单."""
        return await self._post("/jxc_api/AccountTransfer/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改转账单."""
        return await self._post("/jxc_api/AccountTransfer/Update", json_data=kwargs)

    async def audit(self, id_: int):
        """审核转账单."""
        return await self._post("/jxc_api/AccountTransfer/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核转账单."""
        return await self._post("/jxc_api/AccountTransfer/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除转账单."""
        return await self._post("/jxc_api/AccountTransfer/Delete", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """下一条单据ID."""
        return await self._post("/jxc_api/AccountTransfer/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """上一条单据ID."""
        return await self._post("/jxc_api/AccountTransfer/GetPrevID", json_data={"id": id_})

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/AccountTransfer/ShareExcel", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/AccountTransfer/SharePDF", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/AccountTransfer/ShareLink", json_data=kwargs)


class AccountTransferListAPI(_BaseAPI):
    """转账单列表"""

    async def delete(self, ids: list[int]):
        """删除转账单."""
        return await self._post("/jxc_api/AccountTransferList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核转账单."""
        return await self._post("/jxc_api/AccountTransferList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核转账单."""
        return await self._post("/jxc_api/AccountTransferList/UnAudit", json_data={"ids": ids})

    async def search(self, **kwargs):
        """搜索转账单列表."""
        return await self._post("/jxc_api/AccountTransferList/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出转账单数据."""
        return await self._post("/jxc_api/AccountTransferList/Export", json_data=kwargs)

    async def download_template(self):
        """下载转账单导入模板."""
        return await self._post("/jxc_api/AccountTransferList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载导入转账单失败后的错误数据."""
        return await self._post("/jxc_api/AccountTransferList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入转账单."""
        return await self._post("/jxc_api/AccountTransferList/Import", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印转账单."""
        return await self._post("/jxc_api/AccountTransferList/Print", json_data=kwargs)


class OffsetAPI(_BaseAPI):
    """核销单的添加，更新等"""

    async def get_by_id(self, id_: int):
        """根据ID获得核销单."""
        return await self._post("/jxc_api/Offset/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增核销单."""
        return await self._post("/jxc_api/Offset/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改核销单."""
        return await self._post("/jxc_api/Offset/Update", json_data=kwargs)

    async def audit(self, id_: int):
        """审核."""
        return await self._post("/jxc_api/Offset/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核."""
        return await self._post("/jxc_api/Offset/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除核销单."""
        return await self._post("/jxc_api/Offset/Delete", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """下一条单据ID."""
        return await self._post("/jxc_api/Offset/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """上一条单据ID."""
        return await self._post("/jxc_api/Offset/GetPrevID", json_data={"id": id_})

    async def refresh(self, id_: int):
        """刷新核销单数据."""
        return await self._post("/jxc_api/Offset/Refresh", json_data={"id": id_})

    async def get_source_data(self, **kwargs):
        """获得源单列表数据."""
        return await self._post("/jxc_api/Offset/GetSourceData", json_data=kwargs)


class OffsetListAPI(_BaseAPI):
    """核销单列表"""

    async def search(self, **kwargs):
        """搜索核销单列表."""
        return await self._post("/jxc_api/OffsetList/Search", json_data=kwargs)

    async def audit(self, ids: list[int]):
        """审核."""
        return await self._post("/jxc_api/OffsetList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核."""
        return await self._post("/jxc_api/OffsetList/UnAudit", json_data={"ids": ids})

    async def delete(self, ids: list[int]):
        """删除核销单."""
        return await self._post("/jxc_api/OffsetList/Delete", json_data={"ids": ids})

    async def export_data(self, **kwargs):
        """导出核销单数据."""
        return await self._post("/jxc_api/OffsetList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印核销单."""
        return await self._post("/jxc_api/OffsetList/Print", json_data=kwargs)


class OtherPaymentAPI(_BaseAPI):
    """其他支出单的添加，更新，审核等"""

    async def get_by_id(self, id_: int):
        """根据ID获得付款单."""
        return await self._post("/jxc_api/OtherPayment/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增付款单."""
        return await self._post("/jxc_api/OtherPayment/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改付款单."""
        return await self._post("/jxc_api/OtherPayment/Update", json_data=kwargs)

    async def audit(self, id_: int):
        """审核付款单."""
        return await self._post("/jxc_api/OtherPayment/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核付款单."""
        return await self._post("/jxc_api/OtherPayment/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除其它支出单."""
        return await self._post("/jxc_api/OtherPayment/Delete", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """下一条单据ID."""
        return await self._post("/jxc_api/OtherPayment/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """上一条单据ID."""
        return await self._post("/jxc_api/OtherPayment/GetPrevID", json_data={"id": id_})

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/OtherPayment/ShareExcel", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/OtherPayment/SharePDF", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/OtherPayment/ShareLink", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/OtherPayment/DraftDetail", json_data=kwargs)


class OtherPaymentListAPI(_BaseAPI):
    """其它支出单列表"""

    async def delete(self, ids: list[int]):
        """删除其它支出单."""
        return await self._post("/jxc_api/OtherPaymentList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核其它支出单."""
        return await self._post("/jxc_api/OtherPaymentList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核其它支出单."""
        return await self._post("/jxc_api/OtherPaymentList/UnAudit", json_data={"ids": ids})

    async def search(self, **kwargs):
        """搜索其它支出单列表."""
        return await self._post("/jxc_api/OtherPaymentList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """搜索其它支出单列表 SearchDetails."""
        return await self._post("/jxc_api/OtherPaymentList/SearchDetails", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出其它支出单数据."""
        return await self._post("/jxc_api/OtherPaymentList/Export", json_data=kwargs)

    async def download_template(self):
        """下载其它支出单导入模板."""
        return await self._post("/jxc_api/OtherPaymentList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载导入其它支出单失败后的错误数据."""
        return await self._post("/jxc_api/OtherPaymentList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入其它支出单."""
        return await self._post("/jxc_api/OtherPaymentList/Import", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印其它支出单."""
        return await self._post("/jxc_api/OtherPaymentList/Print", json_data=kwargs)

    async def get_related(self, **kwargs):
        """关联单据."""
        return await self._post("/jxc_api/OtherPaymentList/GetRelated", json_data=kwargs)

    async def cancel_related(self, **kwargs):
        """取消关联."""
        return await self._post("/jxc_api/OtherPaymentList/CancelRelated", json_data=kwargs)

    async def get_unsettled(self, **kwargs):
        """获得未结账的单据."""
        return await self._post("/jxc_api/OtherPaymentList/GetUnsettled", json_data=kwargs)

    async def search_invoice(self, **kwargs):
        """搜索发票信息."""
        return await self._post("/jxc_api/OtherPaymentList/SearchInvoice", json_data=kwargs)

    async def register_invoice(self, **kwargs):
        """登记发票."""
        return await self._post("/jxc_api/OtherPaymentList/RegisterInvoice", json_data=kwargs)

    async def cancel_invoice(self, **kwargs):
        """取消登记发票."""
        return await self._post("/jxc_api/OtherPaymentList/CancelInvoice", json_data=kwargs)

    async def batch_cancel_invoice(self, **kwargs):
        """批量取消登记发票."""
        return await self._post("/jxc_api/OtherPaymentList/BatchCancelInvoice", json_data=kwargs)

    async def get_invoice_ids(self, **kwargs):
        """根据单据ID查询关联的发票ID."""
        return await self._post("/jxc_api/OtherPaymentList/GetInvoiceIds", json_data=kwargs)

    async def get_invoice_info(self, **kwargs):
        """根据单据ID查询发票信息."""
        return await self._post("/jxc_api/OtherPaymentList/GetInvoiceInfos", json_data=kwargs)

    async def search_journal(self, **kwargs):
        """搜索日记账."""
        return await self._post("/jxc_api/OtherPaymentList/SearchJournal", json_data=kwargs)

    async def write_off(self, **kwargs):
        """核销."""
        return await self._post("/jxc_api/OtherPaymentList/WriteOff", json_data=kwargs)

    async def manual_write_off(self, **kwargs):
        """手动核销."""
        return await self._post("/jxc_api/OtherPaymentList/ManualWriteOff", json_data=kwargs)

    async def cancel_write_off(self, **kwargs):
        """取消核销."""
        return await self._post("/jxc_api/OtherPaymentList/CancelWriteOff", json_data=kwargs)

    async def get_write_off_ids(self, **kwargs):
        """根据单据ID查询核销记录ID."""
        return await self._post("/jxc_api/OtherPaymentList/GetWriteOffIds", json_data=kwargs)

    async def get_write_off_info(self, **kwargs):
        """根据单据ID核销记录信息."""
        return await self._post("/jxc_api/OtherPaymentList/GetWriteOffInfos", json_data=kwargs)


class OtherReceiptAPI(_BaseAPI):
    """其他收入单的添加，更新，审核等"""

    async def get_by_id(self, id_: int):
        """根据ID获得其它收入单."""
        return await self._post("/jxc_api/OtherReceipt/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增其它收入单."""
        return await self._post("/jxc_api/OtherReceipt/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改其它收入单."""
        return await self._post("/jxc_api/OtherReceipt/Update", json_data=kwargs)

    async def audit(self, id_: int):
        """审核其它收入单."""
        return await self._post("/jxc_api/OtherReceipt/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核其它收入单."""
        return await self._post("/jxc_api/OtherReceipt/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除其它收入单."""
        return await self._post("/jxc_api/OtherReceipt/Delete", json_data={"id": id_})

    async def get_next_id(self, id_: int):
        """下一条单据ID."""
        return await self._post("/jxc_api/OtherReceipt/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """上一条单据ID."""
        return await self._post("/jxc_api/OtherReceipt/GetPrevID", json_data={"id": id_})

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/OtherReceipt/ShareExcel", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/OtherReceipt/SharePDF", json_data=kwargs)

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/OtherReceipt/ShareLink", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/OtherReceipt/DraftDetail", json_data=kwargs)


class OtherReceiptListAPI(_BaseAPI):
    """其他收入单列表"""

    async def delete(self, ids: list[int]):
        """删除其它收入单."""
        return await self._post("/jxc_api/OtherReceiptList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核其它收入单."""
        return await self._post("/jxc_api/OtherReceiptList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核其它收入单."""
        return await self._post("/jxc_api/OtherReceiptList/UnAudit", json_data={"ids": ids})

    async def search(self, **kwargs):
        """搜索其他收入单列表."""
        return await self._post("/jxc_api/OtherReceiptList/Search", json_data=kwargs)

    async def search_detail(self, **kwargs):
        """搜索其他收入单列表 SearchDetails."""
        return await self._post("/jxc_api/OtherReceiptList/SearchDetails", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出其他收入单数据."""
        return await self._post("/jxc_api/OtherReceiptList/Export", json_data=kwargs)

    async def download_template(self):
        """下载其他收入单导入模板."""
        return await self._post("/jxc_api/OtherReceiptList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载导入其他收入单失败后的错误数据."""
        return await self._post("/jxc_api/OtherReceiptList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入其他收入单."""
        return await self._post("/jxc_api/OtherReceiptList/Import", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印其他收入单."""
        return await self._post("/jxc_api/OtherReceiptList/Print", json_data=kwargs)
