"""基础资料 API: 客户/供应商/商品/仓库/账户/职员/计量单位/结算方式/价格等"""

from typing import Optional

from ..client import _BaseAPI


class WarehouseAPI(_BaseAPI):
    """仓库控制器"""

    async def search(self, **kwargs):
        """根据查询条件获取仓库数据."""
        return await self._post("/jxc_api/Warehouse/Search", json_data=kwargs)

    async def get_wh_list(self):
        """获取可用的仓库列表."""
        return await self._post("/jxc_api/Warehouse/GetWhList")

    async def add(self, **kwargs):
        """新增仓库."""
        return await self._post("/jxc_api/Warehouse/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改仓库."""
        return await self._post("/jxc_api/Warehouse/Update", json_data=kwargs)

    async def delete(self, id_: int):
        """删除仓库."""
        return await self._post("/jxc_api/Warehouse/Delete", json_data={"id": id_})

    async def enable(self, id_: int):
        """启用仓库."""
        return await self._post("/jxc_api/Warehouse/Enable", json_data={"id": id_})

    async def disable(self, id_: int):
        """禁用仓库."""
        return await self._post("/jxc_api/Warehouse/Disable", json_data={"id": id_})

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/Warehouse/Export", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/Warehouse/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/Warehouse/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入数据."""
        return await self._post("/jxc_api/Warehouse/Import", json_data=kwargs)

    async def recalc_cost(self):
        """重算成本."""
        return await self._post("/jxc_api/Warehouse/ReCalcCost")

    async def fix_qty(self, **kwargs):
        """修正数量."""
        return await self._post("/jxc_api/Warehouse/FixQty", json_data=kwargs)


class CustomerAPI(_BaseAPI):
    """客户控制器"""

    async def search(self, **kwargs):
        """根据查询条件获取客户数据,PC调用."""
        return await self._post("/jxc_api/Customer/Search", json_data=kwargs)

    async def search_app(self, **kwargs):
        """根据查询条件获取客户数据,APP调用."""
        return await self._post("/jxc_api/Customer/SearchApp", json_data=kwargs)

    async def get_by_id(self, id_: int):
        """根据客户id获取客户详情."""
        return await self._post("/jxc_api/Customer/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增客户."""
        return await self._post("/jxc_api/Customer/Add", json_data=kwargs)

    async def check_name(self, name: str, id_: int = None):
        """检查系统是否存在这个名字."""
        return await self._post("/jxc_api/Customer/CheckName", json_data={"name": name, "id": id_})

    async def update(self, **kwargs):
        """修改客户."""
        return await self._post("/jxc_api/Customer/Update", json_data=kwargs)

    async def batch_update(self, **kwargs):
        """批量修改客户."""
        return await self._post("/jxc_api/Customer/BatchUpdate", json_data=kwargs)

    async def delete(self, id_: int):
        """删除客户."""
        return await self._post("/jxc_api/Customer/Delete", json_data={"id": id_})

    async def enable(self, id_: int):
        """启用客户."""
        return await self._post("/jxc_api/Customer/Enable", json_data={"id": id_})

    async def disable(self, id_: int):
        """禁用客户."""
        return await self._post("/jxc_api/Customer/Disable", json_data={"id": id_})

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/Customer/Export", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/Customer/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/Customer/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入数据."""
        return await self._post("/jxc_api/Customer/Import", json_data=kwargs)

    async def import_category(self, **kwargs):
        """导入客户类别数据."""
        return await self._post("/jxc_api/Customer/ImportCategory", json_data=kwargs)

    async def export_category(self):
        """导出客户类别信息."""
        return await self._post("/jxc_api/Customer/ExportCategory")

    async def download_category_template(self):
        """下载客户类别模板."""
        return await self._post("/jxc_api/Customer/DownloadCategoryTemplate")

    async def download_category_error(self, **kwargs):
        """下载客户类别错误数据."""
        return await self._post("/jxc_api/Customer/DownloadCategoryErrorData", json_data=kwargs)

    async def get_categories(self):
        """检索类别."""
        return await self._post("/jxc_api/Customer/GetCategories")

    async def add_category(self, **kwargs):
        """新增类别."""
        return await self._post("/jxc_api/Customer/AddCategory", json_data=kwargs)

    async def update_category(self, **kwargs):
        """修改类别."""
        return await self._post("/jxc_api/Customer/UpdateCategory", json_data=kwargs)

    async def delete_category(self, id_: int):
        """删除类别."""
        return await self._post("/jxc_api/Customer/DeleteCategory", json_data={"id": id_})


class VendorAPI(_BaseAPI):
    """供应商控制器"""

    async def search(self, **kwargs):
        """根据查询条件获取供应商数据,PC调用."""
        return await self._post("/jxc_api/Vendor/Search", json_data=kwargs)

    async def search_app(self, **kwargs):
        """根据查询条件获取供应商数据,APP调用."""
        return await self._post("/jxc_api/Vendor/SearchApp", json_data=kwargs)

    async def get_by_id(self, id_: int):
        """根据供应商id获取供应商详情."""
        return await self._post("/jxc_api/Vendor/GetById", json_data={"id": id_})

    async def add(self, **kwargs):
        """新增供应商."""
        return await self._post("/jxc_api/Vendor/Add", json_data=kwargs)

    async def check_name(self, name: str, id_: int = None):
        """检查系统是否存在这个名字."""
        return await self._post("/jxc_api/Vendor/CheckName", json_data={"name": name, "id": id_})

    async def update(self, **kwargs):
        """修改供应商."""
        return await self._post("/jxc_api/Vendor/Update", json_data=kwargs)

    async def batch_update(self, **kwargs):
        """批量修改供应商."""
        return await self._post("/jxc_api/Vendor/BatchUpdate", json_data=kwargs)

    async def delete(self, id_: int):
        """删除供应商."""
        return await self._post("/jxc_api/Vendor/Delete", json_data={"id": id_})

    async def enable(self, id_: int):
        """启用供应商."""
        return await self._post("/jxc_api/Vendor/Enable", json_data={"id": id_})

    async def disable(self, id_: int):
        """禁用供应商."""
        return await self._post("/jxc_api/Vendor/Disable", json_data={"id": id_})

    async def export_data(self, **kwargs):
        """导出供应商."""
        return await self._post("/jxc_api/Vendor/Export", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/Vendor/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/Vendor/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入数据."""
        return await self._post("/jxc_api/Vendor/Import", json_data=kwargs)

    async def export_category(self):
        """导出供应商类别信息."""
        return await self._post("/jxc_api/Vendor/ExportCategory")

    async def download_category_template(self):
        """下载供应商类别模板."""
        return await self._post("/jxc_api/Vendor/DownloadCategoryTemplate")

    async def download_category_error(self, **kwargs):
        """下载供应商类别错误数据."""
        return await self._post("/jxc_api/Vendor/DownloadCategoryErrorData", json_data=kwargs)

    async def get_categories(self):
        """检索类别."""
        return await self._post("/jxc_api/Vendor/GetCategories")

    async def add_category(self, **kwargs):
        """新增类别."""
        return await self._post("/jxc_api/Vendor/AddCategory", json_data=kwargs)

    async def update_category(self, **kwargs):
        """修改类别."""
        return await self._post("/jxc_api/Vendor/UpdateCategory", json_data=kwargs)

    async def delete_category(self, id_: int):
        """删除类别."""
        return await self._post("/jxc_api/Vendor/DeleteCategory", json_data={"id": id_})


class EmployeeAPI(_BaseAPI):
    """职员控制器"""

    async def search(self, **kwargs):
        """根据查询条件获取职员数据."""
        return await self._post("/jxc_api/Employee/Search", json_data=kwargs)

    async def add(self, **kwargs):
        """新增职员."""
        return await self._post("/jxc_api/Employee/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改职员."""
        return await self._post("/jxc_api/Employee/Update", json_data=kwargs)

    async def delete(self, id_: int):
        """删除职员."""
        return await self._post("/jxc_api/Employee/Delete", json_data={"id": id_})

    async def enable(self, id_: int):
        """启用职员."""
        return await self._post("/jxc_api/Employee/Enable", json_data={"id": id_})

    async def disable(self, id_: int):
        """禁用职员."""
        return await self._post("/jxc_api/Employee/Disable", json_data={"id": id_})

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/Employee/Export", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/Employee/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/Employee/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入数据."""
        return await self._post("/jxc_api/Employee/Import", json_data=kwargs)


class AccountAPI(_BaseAPI):
    """账户控制器"""

    async def search(self, **kwargs):
        """根据查询条件获取账户数据."""
        return await self._post("/jxc_api/Account/Search", json_data=kwargs)

    async def add(self, **kwargs):
        """新增账户."""
        return await self._post("/jxc_api/Account/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改账户."""
        return await self._post("/jxc_api/Account/Update", json_data=kwargs)

    async def delete(self, id_: int):
        """删除账户."""
        return await self._post("/jxc_api/Account/Delete", json_data={"id": id_})

    async def enable(self, id_: int):
        """启用账户."""
        return await self._post("/jxc_api/Account/Enable", json_data={"id": id_})

    async def disable(self, id_: int):
        """禁用账户."""
        return await self._post("/jxc_api/Account/Disable", json_data={"id": id_})

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/Account/Export", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/Account/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/Account/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入数据."""
        return await self._post("/jxc_api/Account/Import", json_data=kwargs)


class UnitAPI(_BaseAPI):
    """计量单位"""

    async def get_all(self):
        """获取单位数据."""
        return await self._post("/jxc_api/Unit/GetAll")

    async def search(self, **kwargs):
        """分页获取单位数据."""
        return await self._post("/jxc_api/Unit/Search", json_data=kwargs)

    async def search_multi(self, **kwargs):
        """分页获取多单位."""
        return await self._post("/jxc_api/Unit/SearchMultiUnit", json_data=kwargs)

    async def add(self, **kwargs):
        """新增单位."""
        return await self._post("/jxc_api/Unit/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """修改单位."""
        return await self._post("/jxc_api/Unit/Update", json_data=kwargs)

    async def delete(self, id_: int):
        """删除单位."""
        return await self._post("/jxc_api/Unit/Delete", json_data={"id": id_})

    async def import_data(self, **kwargs):
        """导入计量单位."""
        return await self._post("/jxc_api/Unit/Import", json_data=kwargs)

    async def export_data(self):
        """导出计量单位信息."""
        return await self._post("/jxc_api/Unit/Export")

    async def export_partial(self, **kwargs):
        """导出部分计量单位信息."""
        return await self._post("/jxc_api/Unit/ExportPartial", json_data=kwargs)

    async def export_by_condition(self, **kwargs):
        """按条件导出单位."""
        return await self._post("/jxc_api/Unit/ExportByCondition", json_data=kwargs)

    async def download_template(self):
        """下载计量单位模板."""
        return await self._post("/jxc_api/Unit/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载计量单位错误数据."""
        return await self._post("/jxc_api/Unit/DownloadErrorData", json_data=kwargs)


class CustomerCodeAPI(_BaseAPI):
    """客户商品编码控制器"""

    async def search(self, **kwargs):
        """根据查询条件获取客户商品编码数据."""
        return await self._post("/jxc_api/CustomerCode/Search", json_data=kwargs)

    async def save(self, **kwargs):
        """保存客户商品编码."""
        return await self._post("/jxc_api/CustomerCode/Save", json_data=kwargs)

    async def delete(self, id_: int):
        """删除客户商品编码."""
        return await self._post("/jxc_api/CustomerCode/Delete", json_data={"id": id_})

    async def export_data(self, **kwargs):
        """导出列表数据到Excel."""
        return await self._post("/jxc_api/CustomerCode/Export", json_data=kwargs)

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/CustomerCode/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/CustomerCode/DownloadErrorData", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入数据."""
        return await self._post("/jxc_api/CustomerCode/Import", json_data=kwargs)


class PayMethodAPI(_BaseAPI):
    """结算方式控制器"""

    async def search(self, **kwargs):
        """根据查询条件获取结算方式数据."""
        return await self._post("/jxc_api/PayMethod/Search", json_data=kwargs)

    async def add(self, **kwargs):
        """新增结算方式."""
        return await self._post("/jxc_api/PayMethod/Add", json_data=kwargs)

    async def get_next_no(self):
        """获取下一个可用的结算方式编码."""
        return await self._post("/jxc_api/PayMethod/GetNextNo")

    async def update(self, **kwargs):
        """修改结算方式."""
        return await self._post("/jxc_api/PayMethod/Update", json_data=kwargs)

    async def delete(self, id_: int):
        """删除结算方式."""
        return await self._post("/jxc_api/PayMethod/Delete", json_data={"id": id_})


class PriceQueryAPI(_BaseAPI):
    """价格查询"""

    async def search(self, **kwargs):
        """价格资料列表查询."""
        return await self._post("/jxc_api/PriceQuery/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """价格资料列表导出."""
        return await self._post("/jxc_api/PriceQuery/Export", json_data=kwargs)


class ProductPriceAPI(_BaseAPI):
    """价格策略（2.7新增）"""

    async def get_price(self, **kwargs):
        """获取一条价格设置金额信息."""
        return await self._post("/jxc_api/ProductPrice/GetPrice", json_data=kwargs)

    async def get_related_prices(self, **kwargs):
        """获取相关商品的相关价格设置."""
        return await self._post("/jxc_api/ProductPrice/GetRelatedPrices", json_data=kwargs)

    async def add(self, **kwargs):
        """添加商品价格策略."""
        return await self._post("/jxc_api/ProductPrice/Add", json_data=kwargs)

    async def delete(self, id_: int):
        """删除价格策略信息."""
        return await self._post("/jxc_api/ProductPrice/Delete", json_data={"id": id_})

    async def download_template(self):
        """下载模板."""
        return await self._post("/jxc_api/ProductPrice/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载错误数据."""
        return await self._post("/jxc_api/ProductPrice/DownloadErrorData", json_data=kwargs)


class CustomerPriceInfoAPI(_BaseAPI):
    """客户价格资料"""

    async def search(self, **kwargs):
        """查询."""
        return await self._post("/jxc_api/CustomerPriceInfo/Search", json_data=kwargs)

    async def check_dup_interval(self, **kwargs):
        """是否有相同交易数量的交易区间."""
        return await self._post("/jxc_api/CustomerPriceInfo/CheckDupInterval", json_data=kwargs)

    async def set_active(self, **kwargs):
        """设为生效状态."""
        return await self._post("/jxc_api/CustomerPriceInfo/SetActive", json_data=kwargs)

    async def set_inactive(self, **kwargs):
        """设为失效状态."""
        return await self._post("/jxc_api/CustomerPriceInfo/SetInActive", json_data=kwargs)

    async def delete(self, **kwargs):
        """删除价格资料."""
        return await self._post("/jxc_api/CustomerPriceInfo/Delete", json_data=kwargs)

    async def import_data(self, **kwargs):
        """导入接口."""
        return await self._post("/jxc_api/CustomerPriceInfo/Import", json_data=kwargs)

    async def download_template(self):
        """下载导入模版."""
        return await self._post("/jxc_api/CustomerPriceInfo/DownloadTemplate")

    async def download_error(self, **kwargs):
        """下载导入错误数据."""
        return await self._post("/jxc_api/CustomerPriceInfo/DownloadErrorData", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出价格资料."""
        return await self._post("/jxc_api/CustomerPriceInfo/Export", json_data=kwargs)
