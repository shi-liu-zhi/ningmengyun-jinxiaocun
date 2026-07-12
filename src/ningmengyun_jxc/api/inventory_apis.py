"""库存相关 API: 盘点单 / 拆卸单 / 组合单 / 调拨单 / 成本调整单 / 其它出入库"""

from typing import Optional

from ..client import _BaseAPI


class BomAPI(_BaseAPI):
    """Bom 单控制器"""

    async def get_page_data(self):
        """Bom 单据页面使用."""
        return await self._post("/jxc_api/Bom/GetPageData")

    async def find_template_by_name(self, name: str):
        """根据名字查找组装单模板."""
        return await self._post(
            "/jxc_api/Bom/FindTemplateByName",
            json_data={"name": name},
        )

    async def save(self, **kwargs):
        """保存Bom."""
        return await self._post("/jxc_api/Bom/Save", json_data=kwargs)

    async def copy_bom(self, ids: list[int]):
        """列表选择多条复制Bom."""
        return await self._post("/jxc_api/Bom/CopyBom", json_data={"ids": ids})

    async def delete_template(self, pt_id: int):
        """删除模板."""
        return await self._post(
            "/jxc_api/Bom/DelTemplate",
            json_data={"ptId": pt_id},
        )

    async def un_audit(self, id_: int):
        """反审核."""
        return await self._post(
            "/jxc_api/Bom/UnAudit",
            json_data={"id": id_},
        )

    async def get_next_no(self):
        """获取下一个可用编号."""
        return await self._post("/jxc_api/Bom/GetNextNo")

    async def query(self, **kwargs):
        """拆卸单查询."""
        return await self._post("/jxc_api/Bom/ListSearch", json_data=kwargs)

    async def audit(self, id_: int):
        """审核Bom."""
        return await self._post("/jxc_api/Bom/Audit", json_data={"id": id_})

    async def export_bom(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/Bom/Export", json_data=kwargs)

    async def download_bom(self):
        """下载Bom."""
        return await self._post("/jxc_api/Bom/Download")

    async def import_bom(self, **kwargs):
        """导入Bom."""
        return await self._post("/jxc_api/Bom/Import", json_data=kwargs)

    async def download_error_data(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/Bom/DownloadErrorData", json_data=kwargs)

    async def print_bom(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/Bom/Print", json_data=kwargs)

    async def import_cost_adj(self, **kwargs):
        """导入入库成本调整."""
        return await self._post("/jxc_api/Bom/ImportCostAdjustment", json_data=kwargs)


class InventoryAPI(_BaseAPI):
    """盘点单控制器"""

    async def list_products(self, **kwargs):
        """盘点商品列表."""
        return await self._post("/jxc_api/Inventory/ProductList", json_data=kwargs)

    async def get_by_id(self, id_: int):
        """根据盘点单id获取盘点单数据."""
        return await self._post(
            "/jxc_api/Inventory/GetById",
            json_data={"id": id_},
        )

    async def query(self, **kwargs):
        """单据查询."""
        return await self._post("/jxc_api/Inventory/ListSearch", json_data=kwargs)

    async def check_doc_open(self, **kwargs):
        """验证生成单据是否打开."""
        return await self._post("/jxc_api/Inventory/CheckDocOpen", json_data=kwargs)

    async def add(self, **kwargs):
        """新增盘点单."""
        return await self._post("/jxc_api/Inventory/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改盘点单."""
        return await self._post("/jxc_api/Inventory/Update", json_data=kwargs)

    async def finish(self, id_: int):
        """结束盘点."""
        return await self._post(
            "/jxc_api/Inventory/Finish",
            json_data={"id": id_},
        )

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/Inventory/ShareLink", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/Inventory/Export", json_data=kwargs)

    async def export_system_stock(self, **kwargs):
        """导出系统库存."""
        return await self._post("/jxc_api/Inventory/ExportSystemStock")

    async def export_result(self, **kwargs):
        """导出盘点结果."""
        return await self._post("/jxc_api/Inventory/ExportResult", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入单据信息."""
        return await self._post("/jxc_api/Inventory/Import", json_data=kwargs, params={"type": "excel"})

    async def download_error_data(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/Inventory/DownloadErrorData", json_data=kwargs)


class InventoryListAPI(_BaseAPI):
    """盘点单列表控制器"""

    async def query(self, **kwargs):
        """盘点单查询."""
        return await self._post("/jxc_api/InventoryList/ListSearch", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除盘点单."""
        return await self._post(
            "/jxc_api/InventoryList/Delete",
            json_data={"ids": ids},
        )


class DisassemblyAPI(_BaseAPI):
    """拆卸单控制器"""

    async def get_by_id(self, id_: int):
        """根据拆卸单id获取拆卸单数据."""
        return await self._post("/jxc_api/Disassembly/GetById", json_data={"id": id_})

    async def save(self, **kwargs):
        """保存拆卸单."""
        return await self._post("/jxc_api/Disassembly/Save", json_data=kwargs)

    async def audit(self, id_: int):
        """审核拆卸单."""
        return await self._post("/jxc_api/Disassembly/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核拆卸单."""
        return await self._post("/jxc_api/Disassembly/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除拆卸单."""
        return await self._post("/jxc_api/Disassembly/Delete", json_data={"id": id_})

    async def save_template(self, **kwargs):
        """保存模板."""
        return await self._post("/jxc_api/Disassembly/SaveTemplate", json_data=kwargs)

    async def save_template_info(self, **kwargs):
        """保存模板信息."""
        return await self._post("/jxc_api/Disassembly/SaveTemplateInfo", json_data=kwargs)

    async def delete_template(self, pt_id: int):
        """删除模板."""
        return await self._post("/jxc_api/Disassembly/DelTemplate", json_data={"ptId": pt_id})

    async def get_template_info(self, **kwargs):
        """获取模板信息."""
        return await self._post("/jxc_api/Disassembly/GetTemplateInfo", json_data=kwargs)

    async def check_template_name(self, name: str):
        """检测模板名称是否存在."""
        return await self._post("/jxc_api/Disassembly/CheckTemplateName", json_data={"name": name})

    async def check_template_exists(self, pt_id: int):
        """检测模板是否存在."""
        return await self._post("/jxc_api/Disassembly/CheckTemplate", json_data={"ptId": pt_id})

    async def get_next_no(self, date: str):
        """根据单据日期获取编号."""
        return await self._post("/jxc_api/Disassembly/GetNextNo", json_data={"date": date})

    async def get_out_cost(self, **kwargs):
        """获得商品出库成本."""
        return await self._post("/jxc_api/Disassembly/GetOutCost", json_data=kwargs)

    async def get_child_cost(self, **kwargs):
        """获得拆卸单子件成本."""
        return await self._post("/jxc_api/Disassembly/GetChildCost", json_data=kwargs)

    async def get_next_id(self, id_: int):
        """获取下一条单据."""
        return await self._post("/jxc_api/Disassembly/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """获取上一条单据."""
        return await self._post("/jxc_api/Disassembly/GetPrevID", json_data={"id": id_})

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/Disassembly/DraftDetail", json_data=kwargs)


class DisassemblyListAPI(_BaseAPI):
    """拆卸单列表控制器"""

    async def query(self, **kwargs):
        """拆卸单查询."""
        return await self._post("/jxc_api/DisassemblyList/ListSearch", json_data=kwargs)

    async def query_detail(self, **kwargs):
        """拆卸单明细查询."""
        return await self._post("/jxc_api/DisassemblyList/DetailSearch", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除拆卸单."""
        return await self._post("/jxc_api/DisassemblyList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核拆卸单."""
        return await self._post("/jxc_api/DisassemblyList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核拆卸单."""
        return await self._post("/jxc_api/DisassemblyList/UnAudit", json_data={"ids": ids})

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/DisassemblyList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/DisassemblyList/Print", json_data=kwargs)


class AssemblyAPI(_BaseAPI):
    """组合单控制器"""

    async def get_by_id(self, id_: int):
        """根据组合单id获取组合单数据."""
        return await self._post("/jxc_api/Assembly/GetById", json_data={"id": id_})

    async def save(self, **kwargs):
        """保存组装单."""
        return await self._post("/jxc_api/Assembly/Save", json_data=kwargs)

    async def audit(self, id_: int):
        """审核组合单."""
        return await self._post("/jxc_api/Assembly/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核组合单."""
        return await self._post("/jxc_api/Assembly/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除组合单."""
        return await self._post("/jxc_api/Assembly/Delete", json_data={"id": id_})

    async def get_out_cost(self, **kwargs):
        """获得商品出库成本."""
        return await self._post("/jxc_api/Assembly/GetOutCost", json_data=kwargs)

    async def find_template(self, name: str):
        """根据模板名称查询模板."""
        return await self._post("/jxc_api/Assembly/FindTemplate", json_data={"name": name})

    async def save_template_info(self, **kwargs):
        """保存模板信息."""
        return await self._post("/jxc_api/Assembly/SaveTemplateInfo", json_data=kwargs)

    async def delete_template(self, pt_id: int):
        """删除模板."""
        return await self._post("/jxc_api/Assembly/DelTemplate", json_data={"ptId": pt_id})

    async def get_template_by_id(self, pt_id: int):
        """根据模板id获取模板."""
        return await self._post("/jxc_api/Assembly/GetTemplate", json_data={"ptId": pt_id})

    async def check_template_name(self, name: str):
        """检测模板名称是否存在."""
        return await self._post("/jxc_api/Assembly/CheckTemplateName", json_data={"name": name})

    async def check_template(self, pt_id: int):
        """检测模板是否存在."""
        return await self._post("/jxc_api/Assembly/CheckTemplate", json_data={"ptId": pt_id})

    async def get_next_no(self, date: str):
        """根据单据日期获取编号."""
        return await self._post("/jxc_api/Assembly/GetNextNo", json_data={"date": date})

    async def get_next_id(self, id_: int):
        """获取下一条单据."""
        return await self._post("/jxc_api/Assembly/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """获取上一条单据."""
        return await self._post("/jxc_api/Assembly/GetPrevID", json_data={"id": id_})

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/Assembly/DraftDetail", json_data=kwargs)


class AssemblyListAPI(_BaseAPI):
    """组合单列表控制器"""

    async def query(self, **kwargs):
        """组装单查询."""
        return await self._post("/jxc_api/AssemblyList/ListSearch", json_data=kwargs)

    async def query_detail(self, **kwargs):
        """组装单明细查询."""
        return await self._post("/jxc_api/AssemblyList/DetailSearch", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除组合单."""
        return await self._post("/jxc_api/AssemblyList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核组合单."""
        return await self._post("/jxc_api/AssemblyList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核组合单."""
        return await self._post("/jxc_api/AssemblyList/UnAudit", json_data={"ids": ids})

    async def download_template(self):
        """下载采购入库单导入模板."""
        return await self._post("/jxc_api/AssemblyList/DownloadTemplate")

    async def import_data(self, **kwargs):
        """导入组装单."""
        return await self._post("/jxc_api/AssemblyList/Import", json_data=kwargs)

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/AssemblyList/DownloadErrorData", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/AssemblyList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/AssemblyList/Print", json_data=kwargs)


class StockTransferAPI(_BaseAPI):
    """调拨单控制器"""

    async def get_by_id(self, id_: int):
        """根据调拨单id获取调拨单数据."""
        return await self._post("/jxc_api/StockTransfer/GetById", json_data={"id": id_})

    async def save(self, **kwargs):
        """保存调拨单."""
        return await self._post("/jxc_api/StockTransfer/Save", json_data=kwargs)

    async def add(self, **kwargs):
        """新增调拨单."""
        return await self._post("/jxc_api/StockTransfer/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改调拨单."""
        return await self._post("/jxc_api/StockTransfer/Update", json_data=kwargs)

    async def audit(self, id_: int):
        """审核调拨单."""
        return await self._post("/jxc_api/StockTransfer/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核调拨单."""
        return await self._post("/jxc_api/StockTransfer/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除调拨单."""
        return await self._post("/jxc_api/StockTransfer/Delete", json_data={"id": id_})

    async def get_next_no(self, date: str):
        """根据单据日期获取编号."""
        return await self._post("/jxc_api/StockTransfer/GetNextNo", json_data={"date": date})

    async def get_next_id(self, id_: int):
        """获取下一条调拨单."""
        return await self._post("/jxc_api/StockTransfer/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """获取上一条调拨单."""
        return await self._post("/jxc_api/StockTransfer/GetPrevID", json_data={"id": id_})

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/StockTransfer/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/StockTransfer/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/StockTransfer/ShareExcel", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/StockTransfer/DraftDetail", json_data=kwargs)


class StockTransferListAPI(_BaseAPI):
    """调拨单列表控制器"""

    async def query(self, **kwargs):
        """调拨单查询."""
        return await self._post("/jxc_api/StockTransferList/ListSearch", json_data=kwargs)

    async def query_detail(self, **kwargs):
        """调拨单明细查询."""
        return await self._post("/jxc_api/StockTransferList/DetailSearch", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除调拨单."""
        return await self._post("/jxc_api/StockTransferList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核调拨单."""
        return await self._post("/jxc_api/StockTransferList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核调拨单."""
        return await self._post("/jxc_api/StockTransferList/UnAudit", json_data={"ids": ids})

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/StockTransferList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """获取要打印的调拨单据信息列表."""
        return await self._post("/jxc_api/StockTransferList/Print", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/StockTransferList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/StockTransferList/DownloadErrorData", json_data=kwargs)

    async def import_excel(self, **kwargs):
        """导入Excel."""
        return await self._post("/jxc_api/StockTransferList/Import", json_data=kwargs)


class CostAdjAPI(_BaseAPI):
    """成本调整单控制器"""

    async def get_by_id(self, id_: int):
        """根据成本调整单id获取成本调整单数据."""
        return await self._post("/jxc_api/Costadj/GetById", json_data={"id": id_})

    async def save(self, **kwargs):
        """保存成本调整单."""
        return await self._post("/jxc_api/Costadj/Save", json_data=kwargs)

    async def add(self, **kwargs):
        """新增成本调整单."""
        return await self._post("/jxc_api/Costadj/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改成本调整单."""
        return await self._post("/jxc_api/Costadj/Update", json_data=kwargs)

    async def delete(self, id_: int):
        """删除成本调整单."""
        return await self._post("/jxc_api/Costadj/Delete", json_data={"id": id_})

    async def get_next_no(self, date: str):
        """根据单据日期获取编号."""
        return await self._post("/jxc_api/Costadj/GetNextNo", json_data={"date": date})

    async def get_next_id(self, id_: int):
        """获取下一条单据."""
        return await self._post("/jxc_api/Costadj/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """获取上一条单据."""
        return await self._post("/jxc_api/Costadj/GetPrevID", json_data={"id": id_})

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/Costadj/DraftDetail", json_data=kwargs)


class CostAdjListAPI(_BaseAPI):
    """成本调整单列表控制器"""

    async def query(self, **kwargs):
        """成本调整单查询."""
        return await self._post("/jxc_api/CostadjList/ListSearch", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除成本调整单."""
        return await self._post("/jxc_api/CostadjList/Delete", json_data={"ids": ids})

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/CostadjList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """打印."""
        return await self._post("/jxc_api/CostadjList/Print", json_data=kwargs)


class OthersWarehousingAPI(_BaseAPI):
    """其它入库单控制器"""

    async def get_by_id(self, id_: int):
        """根据其它入库单id获取其它入库单数据."""
        return await self._post("/jxc_api/OthersWarehousing/GetById", json_data={"id": id_})

    async def save(self, **kwargs):
        """保存其它入库单."""
        return await self._post("/jxc_api/OthersWarehousing/Save", json_data=kwargs)

    async def get_biz_types(self):
        """获取其他入库单业务类型选项列表."""
        return await self._post("/jxc_api/OthersWarehousing/GetOtherInBizType")

    async def audit(self, id_: int):
        """审核其它入库单."""
        return await self._post("/jxc_api/OthersWarehousing/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核其它入库单."""
        return await self._post("/jxc_api/OthersWarehousing/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除其它入库单."""
        return await self._post("/jxc_api/OthersWarehousing/Delete", json_data={"id": id_})

    async def get_next_no(self, date: str):
        """根据单据日期获取编号."""
        return await self._post("/jxc_api/OthersWarehousing/GetNextNo", json_data={"date": date})

    async def get_next_id(self, id_: int):
        """获取下一条单据."""
        return await self._post("/jxc_api/OthersWarehousing/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """获取上一条单据."""
        return await self._post("/jxc_api/OthersWarehousing/GetPrevID", json_data={"id": id_})

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/OthersWarehousing/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/OthersWarehousing/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/OthersWarehousing/ShareExcel", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/OthersWarehousing/DraftDetail", json_data=kwargs)


class OthersWarehousingOutAPI(_BaseAPI):
    """其它出库单控制器"""

    async def get_by_id(self, id_: int):
        """根据其它出库单id获取其它出库单数据."""
        return await self._post("/jxc_api/OthersWarehousingOut/GetById", json_data={"id": id_})

    async def save(self, **kwargs):
        """保存其它出库单."""
        return await self._post("/jxc_api/OthersWarehousingOut/Save", json_data=kwargs)

    async def get_biz_types(self):
        """获取其他出库单业务类型选项列表."""
        return await self._post("/jxc_api/OthersWarehousingOut/GetOtherOutBizType")

    async def audit(self, id_: int):
        """审核其它出库单."""
        return await self._post("/jxc_api/OthersWarehousingOut/Audit", json_data={"id": id_})

    async def un_audit(self, id_: int):
        """反审核其它出库单."""
        return await self._post("/jxc_api/OthersWarehousingOut/UnAudit", json_data={"id": id_})

    async def delete(self, id_: int):
        """删除其它出库单."""
        return await self._post("/jxc_api/OthersWarehousingOut/Delete", json_data={"id": id_})

    async def get_next_no(self, date: str):
        """根据单据日期获取编号."""
        return await self._post("/jxc_api/OthersWarehousingOut/GetNextNo", json_data={"date": date})

    async def get_next_id(self, id_: int):
        """获取下一条单据."""
        return await self._post("/jxc_api/OthersWarehousingOut/GetNextID", json_data={"id": id_})

    async def get_prev_id(self, id_: int):
        """获取上一条单据."""
        return await self._post("/jxc_api/OthersWarehousingOut/GetPrevID", json_data={"id": id_})

    async def share_link(self, **kwargs):
        """分享链接."""
        return await self._post("/jxc_api/OthersWarehousingOut/ShareLink", json_data=kwargs)

    async def share_pdf(self, **kwargs):
        """分享PDF."""
        return await self._post("/jxc_api/OthersWarehousingOut/SharePDF", json_data=kwargs)

    async def share_excel(self, **kwargs):
        """分享Excel."""
        return await self._post("/jxc_api/OthersWarehousingOut/ShareExcel", json_data=kwargs)

    async def draft_detail(self, **kwargs):
        """草稿详情."""
        return await self._post("/jxc_api/OthersWarehousingOut/DraftDetail", json_data=kwargs)


class OthersWarehousingListAPI(_BaseAPI):
    """其它入库单列表控制器"""

    async def query(self, **kwargs):
        """其它入库单查询."""
        return await self._post("/jxc_api/OthersWarehousingList/ListSearch", json_data=kwargs)

    async def query_detail(self, **kwargs):
        """其它入库单明细查询."""
        return await self._post("/jxc_api/OthersWarehousingList/DetailSearch", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除其它入库单."""
        return await self._post("/jxc_api/OthersWarehousingList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核其它入库单."""
        return await self._post("/jxc_api/OthersWarehousingList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核其它入库单."""
        return await self._post("/jxc_api/OthersWarehousingList/UnAudit", json_data={"ids": ids})

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/OthersWarehousingList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """获取要打印的销售单据信息列表."""
        return await self._post("/jxc_api/OthersWarehousingList/Print", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/OthersWarehousingList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/OthersWarehousingList/DownloadErrorData", json_data=kwargs)

    async def import_excel(self, **kwargs):
        """导入Excel."""
        return await self._post("/jxc_api/OthersWarehousingList/Import", json_data=kwargs)


class OthersWarehousingOutListAPI(_BaseAPI):
    """其它出库单列表控制器"""

    async def query(self, **kwargs):
        """其它出库单查询."""
        return await self._post("/jxc_api/OthersWarehousingOutList/ListSearch", json_data=kwargs)

    async def query_detail(self, **kwargs):
        """其它出库单明细查询."""
        return await self._post("/jxc_api/OthersWarehousingOutList/DetailSearch", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除其它出库单."""
        return await self._post("/jxc_api/OthersWarehousingOutList/Delete", json_data={"ids": ids})

    async def audit(self, ids: list[int]):
        """审核其它出库单."""
        return await self._post("/jxc_api/OthersWarehousingOutList/Audit", json_data={"ids": ids})

    async def un_audit(self, ids: list[int]):
        """反审核其它出库单."""
        return await self._post("/jxc_api/OthersWarehousingOutList/UnAudit", json_data={"ids": ids})

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/OthersWarehousingOutList/Export", json_data=kwargs)

    async def print_data(self, **kwargs):
        """获取要打印的其他出库单信息列表."""
        return await self._post("/jxc_api/OthersWarehousingOutList/Print", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/OthersWarehousingOutList/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/OthersWarehousingOutList/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入数据."""
        return await self._post("/jxc_api/OthersWarehousingOutList/Import", json_data=kwargs)
