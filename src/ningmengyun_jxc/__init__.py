"""
柠檬云进销存开放平台异步 Python SDK.

Usage:
    from ningmengyun_jxc import JxcClient

    async def main():
        async with JxcClient(token="your_token") as client:
            result = await client.balances.get_wh_list()
            print(result.data)
"""

from .client import JxcClient, _BaseAPI
from .exceptions import JxcError, JxcApiError, JxcAuthError
from .models import ApiResult

# ── Register all API groups onto JxcClient ──────────────────────────

from .api.auth import AuthAPI
from .api.balances import BalancesAPI
from .api.inventory_apis import (
    BomAPI,
    InventoryAPI,
    InventoryListAPI,
    DisassemblyAPI,
    DisassemblyListAPI,
    AssemblyAPI,
    AssemblyListAPI,
    StockTransferAPI,
    StockTransferListAPI,
    CostAdjAPI,
    CostAdjListAPI,
    OthersWarehousingAPI,
    OthersWarehousingOutAPI,
    OthersWarehousingListAPI,
    OthersWarehousingOutListAPI,
)
from .api.sales import (
    SellDeliveryAPI,
    SellDeliveryListAPI,
    SellOrderAPI,
    SellOrderListAPI,
    SellReturnAPI,
    SellReturnListAPI,
)
from .api.purchase import (
    PurchaseOrderAPI,
    PurchaseOrderListAPI,
    WarehousingAPI,
    WarehousingListAPI,
    WarehousingReturnAPI,
    WarehousingReturnListAPI,
)
from .api.finance import (
    ReceiptAPI,
    ReceiptListAPI,
    PaymentAPI,
    PaymentListAPI,
    AccountTransferAPI,
    AccountTransferListAPI,
    OffsetAPI,
    OffsetListAPI,
    OtherPaymentAPI,
    OtherPaymentListAPI,
    OtherReceiptAPI,
    OtherReceiptListAPI,
)
from .api.reports import (
    InventoryAgingAPI,
    ReceiveSendSummaryAPI,
    ReportReceiveDetailedAPI,
    SalesProfitAPI,
    SaleStatisticsAPI,
    SellOrderDetailAPI,
    SellOrderSummaryAPI,
    SellOrderTrackAPI,
    SellRankingsListAPI,
    SellReceiptAPI,
    PurchaseOrderDetailAPI,
    PurchaseOrderSummaryAPI,
    PurchaseOrderTrackAPI,
    PurchasePaymentAPI,
    OrderBySaleAPI,
    OperatingProfitAPI,
    ProfitAPI,
    OrpDetailsAPI,
    CashBankAPI,
    CustomerBriefAPI,
    CustomerStatementAPI,
    PurSellExpenseAPI,
    PayableDetailsAPI,
    ReceivableDetailsAPI,
    ReceivableWarningAPI,
    UnitDebtAPI,
    VendorBriefAPI,
    VendorStatementAPI,
    SellAPI,
    BaseDataSearchAPI,
)
from .api.system import (
    CodeRuleAPI,
    PageColumnSetAPI,
    VersionAPI,
    BackupAPI,
    CheckoutAPI,
    CommonAPI,
    LogAPI,
    PrintTplAPI,
    FileDownloadCenterAPI,
    PrintAPI,
    AttachmentAPI,
)
from .api.base_data import (
    WarehouseAPI,
    CustomerAPI,
    VendorAPI,
    EmployeeAPI,
    AccountAPI,
    UnitAPI,
    CustomerCodeAPI,
    PayMethodAPI,
    PriceQueryAPI,
    ProductPriceAPI,
    CustomerPriceInfoAPI,
)

# ── Patch JxcClient to register all API groups ──────────────────────

_api_registrations = [
    ("auth", AuthAPI),
    ("balances", BalancesAPI),
    ("bom", BomAPI),
    ("inventory", InventoryAPI),
    ("inventory_list", InventoryListAPI),
    ("disassembly", DisassemblyAPI),
    ("disassembly_list", DisassemblyListAPI),
    ("assembly", AssemblyAPI),
    ("assembly_list", AssemblyListAPI),
    ("stock_transfer", StockTransferAPI),
    ("stock_transfer_list", StockTransferListAPI),
    ("cost_adj", CostAdjAPI),
    ("cost_adj_list", CostAdjListAPI),
    ("others_warehousing", OthersWarehousingAPI),
    ("others_warehousing_out", OthersWarehousingOutAPI),
    ("others_warehousing_list", OthersWarehousingListAPI),
    ("others_warehousing_out_list", OthersWarehousingOutListAPI),
    ("sell_delivery", SellDeliveryAPI),
    ("sell_delivery_list", SellDeliveryListAPI),
    ("sell_order", SellOrderAPI),
    ("sell_order_list", SellOrderListAPI),
    ("sell_return", SellReturnAPI),
    ("sell_return_list", SellReturnListAPI),
    ("purchase_order", PurchaseOrderAPI),
    ("purchase_order_list", PurchaseOrderListAPI),
    ("warehousing", WarehousingAPI),
    ("warehousing_list", WarehousingListAPI),
    ("warehousing_return", WarehousingReturnAPI),
    ("warehousing_return_list", WarehousingReturnListAPI),
    ("receipt", ReceiptAPI),
    ("receipt_list", ReceiptListAPI),
    ("payment", PaymentAPI),
    ("payment_list", PaymentListAPI),
    ("account_transfer", AccountTransferAPI),
    ("account_transfer_list", AccountTransferListAPI),
    ("offset", OffsetAPI),
    ("offset_list", OffsetListAPI),
    ("other_payment", OtherPaymentAPI),
    ("other_payment_list", OtherPaymentListAPI),
    ("other_receipt", OtherReceiptAPI),
    ("other_receipt_list", OtherReceiptListAPI),
    ("inventory_aging", InventoryAgingAPI),
    ("receive_send_summary", ReceiveSendSummaryAPI),
    ("report_receive_detailed", ReportReceiveDetailedAPI),
    ("sales_profit", SalesProfitAPI),
    ("sale_statistics", SaleStatisticsAPI),
    ("sell_order_detail", SellOrderDetailAPI),
    ("sell_order_summary", SellOrderSummaryAPI),
    ("sell_order_track", SellOrderTrackAPI),
    ("sell_rankings", SellRankingsListAPI),
    ("sell_receipt", SellReceiptAPI),
    ("purchase_order_detail", PurchaseOrderDetailAPI),
    ("purchase_order_summary", PurchaseOrderSummaryAPI),
    ("purchase_order_track", PurchaseOrderTrackAPI),
    ("purchase_payment", PurchasePaymentAPI),
    ("order_by_sale", OrderBySaleAPI),
    ("operating_profit", OperatingProfitAPI),
    ("profit", ProfitAPI),
    ("orp_details", OrpDetailsAPI),
    ("cash_bank", CashBankAPI),
    ("customer_brief", CustomerBriefAPI),
    ("customer_statement", CustomerStatementAPI),
    ("pur_sell_expense", PurSellExpenseAPI),
    ("payable_details", PayableDetailsAPI),
    ("receivable_details", ReceivableDetailsAPI),
    ("receivable_warning", ReceivableWarningAPI),
    ("unit_debt", UnitDebtAPI),
    ("vendor_brief", VendorBriefAPI),
    ("vendor_statement", VendorStatementAPI),
    ("sell_page", SellAPI),
    ("base_data_search", BaseDataSearchAPI),
    ("code_rule", CodeRuleAPI),
    ("page_column_set", PageColumnSetAPI),
    ("version", VersionAPI),
    ("backup", BackupAPI),
    ("checkout", CheckoutAPI),
    ("common", CommonAPI),
    ("log", LogAPI),
    ("print_tpl", PrintTplAPI),
    ("file_download", FileDownloadCenterAPI),
    ("print_api", PrintAPI),
    ("attachment", AttachmentAPI),
    ("warehouse", WarehouseAPI),
    ("customer", CustomerAPI),
    ("vendor", VendorAPI),
    ("employee", EmployeeAPI),
    ("account", AccountAPI),
    ("unit", UnitAPI),
    ("customer_code", CustomerCodeAPI),
    ("pay_method", PayMethodAPI),
    ("price_query", PriceQueryAPI),
    ("product_price", ProductPriceAPI),
    ("customer_price_info", CustomerPriceInfoAPI),
]


def _register_all_apis(client: JxcClient):
    for name, api_cls in _api_registrations:
        client._register_api(name, api_cls(client))


# Monkey-patch __init__ to auto-register
_orig_init = JxcClient.__init__


def _new_init(self, *args, **kwargs):
    _orig_init(self, *args, **kwargs)
    _register_all_apis(self)


JxcClient.__init__ = _new_init

__all__ = [
    "JxcClient",
    "JxcError",
    "JxcApiError",
    "JxcAuthError",
    "ApiResult",
]
