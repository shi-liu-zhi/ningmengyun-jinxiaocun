"""报表类 API: 库存账龄分析 / 收发汇总/明细 / 销售报表 / 采购报表 / 利润表等"""

from ..client import _BaseAPI


class InventoryAgingAPI(_BaseAPI):
    """库存账龄分析表"""

    async def get_aging(self):
        """获取账龄."""
        return await self._post("/jxc_api/InventoryAging/GetAging")

    async def save_aging(self, **kwargs):
        """保存库存账龄设置."""
        return await self._post("/jxc_api/InventoryAging/SaveAging", json_data=kwargs)

    async def reset_aging(self):
        """恢复默认账龄."""
        return await self._post("/jxc_api/InventoryAging/ResetAging")

    async def export_data(self, **kwargs):
        """导出库存账龄分析表."""
        return await self._post("/jxc_api/InventoryAging/Export", json_data=kwargs)

    async def search(self, **kwargs):
        """检索库存账龄分析表数据."""
        return await self._post("/jxc_api/InventoryAging/Search", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/InventoryAging/Print", json_data=kwargs)


class ReceiveSendSummaryAPI(_BaseAPI):
    """商品收发汇总表"""

    async def init_data(self):
        """初始化商品收发汇总表."""
        return await self._post("/jxc_api/ReceiveSendSummary/InitData")

    async def search(self, **kwargs):
        """获取商品收发汇总表信息."""
        return await self._post("/jxc_api/ReceiveSendSummary/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/ReceiveSendSummary/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/ReceiveSendSummary/Print", json_data=kwargs)


class ReportReceiveDetailedAPI(_BaseAPI):
    """商品收发明细表"""

    async def init_data(self):
        """初始化商品收发明细表."""
        return await self._post("/jxc_api/ReportReceiveDetailed/InitData")

    async def search(self, **kwargs):
        """检索商品收发明细表数据."""
        return await self._post("/jxc_api/ReportReceiveDetailed/Search", json_data=kwargs)

    async def export_excel(self, **kwargs):
        """导出Excel."""
        return await self._post("/jxc_api/ReportReceiveDetailed/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/ReportReceiveDetailed/Print", json_data=kwargs)


class SalesProfitAPI(_BaseAPI):
    """销售利润表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/SalesProfit/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SalesProfit/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/SalesProfit/Print", json_data=kwargs)


class SaleStatisticsAPI(_BaseAPI):
    """销售统计数据"""

    async def get_receipt_stats(self):
        """销售收款情况统计."""
        return await self._post("/jxc_api/SaleStatistics/GetSaleReceiptStatistics")


class SellOrderDetailAPI(_BaseAPI):
    """销售明细表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/SellOrderDetail/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellOrderDetail/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/SellOrderDetail/Print", json_data=kwargs)


class SellOrderSummaryAPI(_BaseAPI):
    """销售汇总表"""

    async def search(self, **kwargs):
        """检索销售汇总表."""
        return await self._post("/jxc_api/SellOrderSummary/Search", json_data=kwargs)

    async def search_by_product(self, **kwargs):
        """检索销售汇总表（按商品）."""
        return await self._post("/jxc_api/SellOrderSummary/SearchByProduct", json_data=kwargs)

    async def search_by_customer(self, **kwargs):
        """检索销售汇总表（按客户）."""
        return await self._post("/jxc_api/SellOrderSummary/SearchByCustomer", json_data=kwargs)

    async def search_by_seller(self, **kwargs):
        """检索销售汇总表（按销售人员）."""
        return await self._post("/jxc_api/SellOrderSummary/SearchBySeller", json_data=kwargs)

    async def share_link_by_product(self, **kwargs):
        """分享销售汇总表链接(按商品)."""
        return await self._post("/jxc_api/SellOrderSummary/ShareLinkByProduct", json_data=kwargs)

    async def share_link_by_customer(self, **kwargs):
        """分享销售汇总表链接(按客户)."""
        return await self._post("/jxc_api/SellOrderSummary/ShareLinkByCustomer", json_data=kwargs)

    async def share_link_by_seller(self, **kwargs):
        """分享销售汇总表链接(按销售员)."""
        return await self._post("/jxc_api/SellOrderSummary/ShareLinkBySeller", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/SellOrderSummary/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/SellOrderSummary/ShareExcel", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellOrderSummary/Export", json_data=kwargs)

    async def print_by_product(self, **kwargs):
        """打印销售汇总表（按商品）."""
        return await self._post("/jxc_api/SellOrderSummary/PrintByProduct", json_data=kwargs)

    async def print_by_customer(self, **kwargs):
        """打印销售汇总表（按客户）."""
        return await self._post("/jxc_api/SellOrderSummary/PrintByCustomer", json_data=kwargs)

    async def print_by_dept(self, **kwargs):
        """打印销售汇总表（按部门）."""
        return await self._post("/jxc_api/SellOrderSummary/PrintByDept", json_data=kwargs)

    async def print_by_seller(self, **kwargs):
        """打印销售汇总表（按销售人员）."""
        return await self._post("/jxc_api/SellOrderSummary/PrintBySeller", json_data=kwargs)


class SellOrderTrackAPI(_BaseAPI):
    """销售订单跟踪表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/SellOrderTrack/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellOrderTrack/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/SellOrderTrack/Print", json_data=kwargs)


class SellRankingsListAPI(_BaseAPI):
    """销售排行表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/SellRankingsList/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellRankingsList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/SellRankingsList/Print", json_data=kwargs)


class SellReceiptAPI(_BaseAPI):
    """销售收款一览表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/SellReceipt/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/SellReceipt/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/SellReceipt/Print", json_data=kwargs)


class PurchaseOrderDetailAPI(_BaseAPI):
    """采购明细表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/PurchaseOrderDetail/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/PurchaseOrderDetail/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/PurchaseOrderDetail/Print", json_data=kwargs)


class PurchaseOrderSummaryAPI(_BaseAPI):
    """采购汇总表"""

    async def search(self, **kwargs):
        """检索采购汇总表."""
        return await self._post("/jxc_api/PurchaseOrderSummary/Search", json_data=kwargs)

    async def search_by_product(self, **kwargs):
        """检索采购汇总表(按商品)."""
        return await self._post("/jxc_api/PurchaseOrderSummary/SearchByProduct", json_data=kwargs)

    async def search_by_vendor(self, **kwargs):
        """检索采购汇总表(按供应商)."""
        return await self._post("/jxc_api/PurchaseOrderSummary/SearchByVendor", json_data=kwargs)

    async def search_by_buyer(self, **kwargs):
        """检索采购汇总表(按采购员)."""
        return await self._post("/jxc_api/PurchaseOrderSummary/SearchByBuyer", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/PurchaseOrderSummary/Export", json_data=kwargs)

    async def print_by_product(self, **kwargs):
        """打印——按商品."""
        return await self._post("/jxc_api/PurchaseOrderSummary/PrintByProduct", json_data=kwargs)

    async def print_by_vendor(self, **kwargs):
        """打印——按供应商."""
        return await self._post("/jxc_api/PurchaseOrderSummary/PrintByVendor", json_data=kwargs)

    async def print_by_buyer(self, **kwargs):
        """打印——按采购员."""
        return await self._post("/jxc_api/PurchaseOrderSummary/PrintByBuyer", json_data=kwargs)

    async def share_link_by_product(self, **kwargs):
        """分享链接（按商品）."""
        return await self._post("/jxc_api/PurchaseOrderSummary/ShareLinkByProduct", json_data=kwargs)

    async def share_link_by_vendor(self, **kwargs):
        """分享链接（按供应商）."""
        return await self._post("/jxc_api/PurchaseOrderSummary/ShareLinkByVendor", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/PurchaseOrderSummary/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/PurchaseOrderSummary/ShareExcel", json_data=kwargs)


class PurchaseOrderTrackAPI(_BaseAPI):
    """采购订单跟踪表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/PurchaseOrderTrack/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/PurchaseOrderTrack/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/PurchaseOrderTrack/Print", json_data=kwargs)


class PurchasePaymentAPI(_BaseAPI):
    """采购付款一览表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/PurchasePayment/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/PurchasePayment/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/PurchasePayment/Print", json_data=kwargs)


class OrderBySaleAPI(_BaseAPI):
    """以销定购"""

    async def search(self, **kwargs):
        """查询以销定购."""
        return await self._post("/jxc_api/OrderBySale/Search", json_data=kwargs)

    async def gen_purchase_order(self, **kwargs):
        """使用销售订单生成采购订单."""
        return await self._post("/jxc_api/OrderBySale/GeneratePurOrder", json_data=kwargs)

    async def gen_warehousing(self, **kwargs):
        """使用销售订单生成采购入库单."""
        return await self._post("/jxc_api/OrderBySale/GenerateWarehousing", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/OrderBySale/Export", json_data=kwargs)


class OperatingProfitAPI(_BaseAPI):
    """经营利润表"""

    async def search(self, **kwargs):
        """查询利润数据."""
        return await self._post("/jxc_api/OperatingProfit/Search", json_data=kwargs)

    async def search_with_ar(self, **kwargs):
        """查询利润数据-应收应付和收款信息."""
        return await self._post("/jxc_api/OperatingProfit/SearchWithARAP", json_data=kwargs)

    async def search_all(self, **kwargs):
        """查询利润数据-全部."""
        return await self._post("/jxc_api/OperatingProfit/SearchAll", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出利润表到Excel."""
        return await self._post("/jxc_api/OperatingProfit/Export", json_data=kwargs)


class ProfitAPI(_BaseAPI):
    """利润表"""

    async def search(self, **kwargs):
        """查询利润数据."""
        return await self._post("/jxc_api/Profit/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出利润表到Excel."""
        return await self._post("/jxc_api/Profit/Export", json_data=kwargs)


class OrpDetailsAPI(_BaseAPI):
    """其他收支明细表"""

    async def search(self, **kwargs):
        """查询其他收支记录."""
        return await self._post("/jxc_api/OrpDetails/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/OrpDetails/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/OrpDetails/Print", json_data=kwargs)


class CashBankAPI(_BaseAPI):
    """现金银行报表"""

    async def search(self, **kwargs):
        """获取账户收支明细数据."""
        return await self._post("/jxc_api/CashBank/Search", json_data=kwargs)

    async def cash_flow(self, **kwargs):
        """资金流水."""
        return await self._post("/jxc_api/CashBank/CashFlow", json_data=kwargs)

    async def share_cash_flow(self, **kwargs):
        """分享资金流水."""
        return await self._post("/jxc_api/CashBank/ShareCashFlow", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/CashBank/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/CashBank/Print", json_data=kwargs)


class CustomerBriefAPI(_BaseAPI):
    """往来客户一览表"""

    async def search(self, **kwargs):
        """获取客户应收汇总数据."""
        return await self._post("/jxc_api/CustomerBrief/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/CustomerBrief/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/CustomerBrief/Print", json_data=kwargs)


class CustomerStatementAPI(_BaseAPI):
    """客户对账单"""

    async def init_filter(self):
        """获得列表过滤的初始条件."""
        return await self._post("/jxc_api/CustomerStatement/InitFilter")

    async def search(self, **kwargs):
        """查询客户收款记录数据."""
        return await self._post("/jxc_api/CustomerStatement/Search", json_data=kwargs)

    async def share_data(self, **kwargs):
        """分享客户收款记录数据."""
        return await self._post("/jxc_api/CustomerStatement/Share", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出客户对账单信息到Excel."""
        return await self._post("/jxc_api/CustomerStatement/Export", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/CustomerStatement/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/CustomerStatement/ShareExcel", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印支持显示商品明细."""
        return await self._post("/jxc_api/CustomerStatement/Print", json_data=kwargs)

    async def share_wx_qr(self, **kwargs):
        """分享微信二维码."""
        return await self._post("/jxc_api/CustomerStatement/ShareWeChatQR", json_data=kwargs)


class PurSellExpenseAPI(_BaseAPI):
    """采购销售费用表"""

    async def search(self, **kwargs):
        """查询."""
        return await self._post("/jxc_api/PurSellExpense/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出到Excel."""
        return await self._post("/jxc_api/PurSellExpense/Export", json_data=kwargs)


class PayableDetailsAPI(_BaseAPI):
    """应付账款明细表"""

    async def search(self, **kwargs):
        """获取应付账款明细表数据."""
        return await self._post("/jxc_api/PayableDetails/Search", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/PayableDetails/Print", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/PayableDetails/Export", json_data=kwargs)


class ReceivableDetailsAPI(_BaseAPI):
    """应收账款明细表"""

    async def search(self, **kwargs):
        """获取应收账款明细表数据."""
        return await self._post("/jxc_api/ReceivableDetails/Search", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/ReceivableDetails/Print", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/ReceivableDetails/Export", json_data=kwargs)


class ReceivableWarningAPI(_BaseAPI):
    """应收账款预警表"""

    async def get_days(self):
        """获取预警天数."""
        return await self._post("/jxc_api/ReceivableWarning/GetDays")

    async def save_days(self, **kwargs):
        """保存预警天数设置."""
        return await self._post("/jxc_api/ReceivableWarning/SaveDays", json_data=kwargs)

    async def search(self, **kwargs):
        """应收账款预警表查询."""
        return await self._post("/jxc_api/ReceivableWarning/Search", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/ReceivableWarning/Print", json_data=kwargs)


class UnitDebtAPI(_BaseAPI):
    """往来单位欠款表"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/UnitDebt/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/UnitDebt/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/UnitDebt/Print", json_data=kwargs)

    async def query_debt(self, **kwargs):
        """查询单位欠款."""
        return await self._post("/jxc_api/UnitDebt/QueryDebt", json_data=kwargs)


class VendorBriefAPI(_BaseAPI):
    """往来供应商一览表"""

    async def search(self, **kwargs):
        """获取供应商付款记录."""
        return await self._post("/jxc_api/VendorBrief/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/VendorBrief/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/VendorBrief/Print", json_data=kwargs)


class VendorStatementAPI(_BaseAPI):
    """供应商对账单"""

    async def init_filter(self):
        """获得列表过滤的初始条件."""
        return await self._post("/jxc_api/VendorStatement/InitFilter")

    async def search(self, **kwargs):
        """获取供应商应付汇总数据."""
        return await self._post("/jxc_api/VendorStatement/Search", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印(不显示商品明细)."""
        return await self._post("/jxc_api/VendorStatement/Print", json_data=kwargs)

    async def share_data(self, **kwargs):
        """分享供应商应付汇总数据."""
        return await self._post("/jxc_api/VendorStatement/Share", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出供应商对账单到Excel."""
        return await self._post("/jxc_api/VendorStatement/Export", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/VendorStatement/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/VendorStatement/ShareExcel", json_data=kwargs)


class SellAPI(_BaseAPI):
    """销售页面数据"""

    async def get_stats(self):
        """获得销售页面的统计数据."""
        return await self._post("/jxc_api/Sell/GetPageStatistics")


class BaseDataSearchAPI(_BaseAPI):
    """基础资料报表查询"""

    async def search_account(self, **kwargs):
        """根据查询条件获取账户数据."""
        return await self._post("/jxc_api/BaseDataSearch/SearchAccount", json_data=kwargs)

    async def search_by_type(self, **kwargs):
        """根据数据类型获取对应资料数据."""
        return await self._post("/jxc_api/BaseDataSearch/SearchByType", json_data=kwargs)

    async def filter_category(self, **kwargs):
        """根据关键字过滤类别."""
        return await self._post("/jxc_api/BaseDataSearch/FilterCategory", json_data=kwargs)

    async def get_vendor_stats(self, **kwargs):
        """根据供应商ID查询统计数据."""
        return await self._post("/jxc_api/BaseDataSearch/GetVendorStatistics", json_data=kwargs)
