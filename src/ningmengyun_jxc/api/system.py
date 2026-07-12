"""系统配置相关 API: 编码规则 / 列设置 / 版本 / 备份恢复 / 结账 / 日志 / 打印模板"""

from ..client import _BaseAPI


class CodeRuleAPI(_BaseAPI):
    """编码规则"""

    async def get_list(self):
        """获取单据编码规则."""
        return await self._post("/jxc_api/CodeRule/GetList")

    async def get_by_id(self, id_: int):
        """获取指定单据编码规则."""
        return await self._post("/jxc_api/CodeRule/GetByID", json_data={"id": id_})

    async def add(self, **kwargs):
        """添加单据编码规则."""
        return await self._post("/jxc_api/CodeRule/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """编辑单据编码规则."""
        return await self._post("/jxc_api/CodeRule/Update", json_data=kwargs)

    async def enable(self, id_: int, enabled: bool):
        """启用停用."""
        return await self._post("/jxc_api/CodeRule/Enable", json_data={"id": id_, "enabled": enabled})

    async def delete(self, id_: int):
        """删除单据编码规则."""
        return await self._post("/jxc_api/CodeRule/Delete", json_data={"id": id_})

    async def can_edit(self):
        """判断能否编辑编码."""
        return await self._post("/jxc_api/CodeRule/CanEdit")

    async def should_recode_on_date_change(self):
        """判断是否编码日期变化时重新编码."""
        return await self._post("/jxc_api/CodeRule/IsRecodeOnDateChange")

    async def get_basic_rules(self):
        """获取基础资料编码规则."""
        return await self._post("/jxc_api/CodeRule/GetBasicRules")

    async def get_basic_rule_by_id(self, id_: int):
        """获取ID查询基础资料编码规则."""
        return await self._post("/jxc_api/CodeRule/GetBasicRuleByID", json_data={"id": id_})

    async def can_change_code(self):
        """当前编码是否可以更换."""
        return await self._post("/jxc_api/CodeRule/CanChangeCode")

    async def is_biz_type_bound(self):
        """编码规则是否绑定了业务类型."""
        return await self._post("/jxc_api/CodeRule/IsBizTypeBound")

    async def add_basic_rule(self, **kwargs):
        """添加基础资料编码规则."""
        return await self._post("/jxc_api/CodeRule/AddBasicRule", json_data=kwargs)

    async def update_basic_rule(self, **kwargs):
        """编辑基础资料编码规则."""
        return await self._post("/jxc_api/CodeRule/UpdateBasicRule", json_data=kwargs)

    async def delete_basic_rule(self, id_: int):
        """删除基础资料编码规则."""
        return await self._post("/jxc_api/CodeRule/DeleteBasicRule", json_data={"id": id_})

    async def enable_basic_rule(self, id_: int, enabled: bool):
        """启用基础资料编码规则."""
        return await self._post("/jxc_api/CodeRule/EnableBasicRule", json_data={"id": id_, "enabled": enabled})


class PageColumnSetAPI(_BaseAPI):
    """列设置信息操作"""

    async def save(self, **kwargs):
        """添加或修改页面列设置."""
        return await self._post("/jxc_api/PageColumnSet/Save", json_data=kwargs)

    async def batch_save(self, **kwargs):
        """批量添加或修改统一列设置."""
        return await self._post("/jxc_api/PageColumnSet/BatchSave", json_data=kwargs)

    async def query(self, **kwargs):
        """查询统一列设置."""
        return await self._post("/jxc_api/PageColumnSet/Query", json_data=kwargs)

    async def clear(self, **kwargs):
        """清除页面列设置."""
        return await self._post("/jxc_api/PageColumnSet/Clear", json_data=kwargs)

    async def sync(self, **kwargs):
        """同步列设置."""
        return await self._post("/jxc_api/PageColumnSet/Sync", json_data=kwargs)

    async def is_enabled(self):
        """判断是否启用列设置."""
        return await self._post("/jxc_api/PageColumnSet/IsEnabled")

    async def save_enabled(self, **kwargs):
        """保存列设置开关."""
        return await self._post("/jxc_api/PageColumnSet/SaveEnabled", json_data=kwargs)


class VersionAPI(_BaseAPI):
    """版本信息"""

    async def get_current(self):
        """获取当前版本信息."""
        return await self._post("/jxc_api/Vesion/GetCurrentVersion")

    async def add_access_log(self, **kwargs):
        """添加访问日志."""
        return await self._post("/jxc_api/Vesion/AddAccessLog", json_data=kwargs)


class BackupAPI(_BaseAPI):
    """备份、恢复"""

    async def get_list(self):
        """获取备份信息列表."""
        return await self._post("/jxc_api/Backup/GetList")

    async def get_backup_status(self):
        """备份是否完成."""
        return await self._post("/jxc_api/Backup/GetBackUpStatus")

    async def get_capacity(self):
        """获取容量."""
        return await self._post("/jxc_api/Backup/GetCapacity")

    async def delete_backup(self, **kwargs):
        """删除备份数据."""
        return await self._post("/jxc_api/Backup/Delete", json_data=kwargs)

    async def upload_backup(self, **kwargs):
        """上传备份文件."""
        return await self._post("/jxc_api/Backup/UploadBackupFile", json_data=kwargs)

    async def verify_temp_package(self):
        """校验是否含有72h临时包."""
        return await self._post("/jxc_api/Backup/Verify72HTempPackage")

    async def batch_delete(self, **kwargs):
        """批量删除备份包."""
        return await self._post("/jxc_api/Backup/BatchDelete", json_data=kwargs)

    async def download(self, **kwargs):
        """下载备份文件."""
        return await self._post("/jxc_api/Backup/Download", json_data=kwargs)

    async def backup_data(self):
        """备份数据."""
        return await self._post("/jxc_api/Backup/BackUpData")

    async def restore(self, **kwargs):
        """恢复数据."""
        return await self._post("/jxc_api/Backup/Restore", json_data=kwargs)

    async def toggle_auto_backup(self, **kwargs):
        """启用或关闭自动备份."""
        return await self._post("/jxc_api/Backup/SetAutoBackup", json_data=kwargs)

    async def send_email_code(self, **kwargs):
        """发送邮箱验证码."""
        return await self._post("/jxc_api/Backup/SendEmailCode", json_data=kwargs)

    async def save_settings(self, **kwargs):
        """保存设置信息."""
        return await self._post("/jxc_api/Backup/SaveSetting", json_data=kwargs)

    async def get_auto_backup_settings(self):
        """获取自动备份设置信息."""
        return await self._post("/jxc_api/Backup/GetBackUpSetting")


class CheckoutAPI(_BaseAPI):
    """结账/反结账 系统参数"""

    async def init_data(self):
        """初始化结账/反结账页面信息."""
        return await self._post("/jxc_api/Checkout/InitData")

    async def checkout(self, **kwargs):
        """结账."""
        return await self._post("/jxc_api/Checkout/CheckOut", json_data=kwargs)

    async def check_unaudited(self, **kwargs):
        """检查是否存在未审核单据."""
        return await self._post("/jxc_api/Checkout/CheckUnAudited", json_data=kwargs)

    async def un_checkout(self):
        """反结账."""
        return await self._post("/jxc_api/Checkout/UnCheckOut")

    async def check_negative_stock(self, **kwargs):
        """检查是否存在负库存商品."""
        return await self._post("/jxc_api/Checkout/CheckNegativeStock", json_data=kwargs)

    async def erp_checkout(self, **kwargs):
        """Erp结账."""
        return await self._post("/jxc_api/Checkout/ErpCheckOut", json_data=kwargs)


class CommonAPI(_BaseAPI):
    """通用接口"""

    async def get_doc_no(self, **kwargs):
        """获取单据编号."""
        return await self._post("/jxc_api/Common/GetDocNo", json_data=kwargs)

    async def get_next_code(self, code_type: str):
        """
        获取下一个编码.

        code_type: Product/Customer/Vendor/Employee/Warehouse/Account
        """
        return await self._post("/jxc_api/Common/GetNextCode", json_data={"codeType": code_type})

    async def get_recently_used(self, data_type: str):
        """获取最近使用的5个商品、客户、供应商、员工、仓库、账户."""
        return await self._post("/jxc_api/Common/GetRecentlyUsed", json_data={"dataType": data_type})

    async def get_all_account_books(self):
        """获取所有的账套."""
        return await self._post("/jxc_api/Common/GetAllAccountBooks")


class LogAPI(_BaseAPI):
    """账套日志、账套登录日志，用户操作日志"""

    async def add_login_log(self, **kwargs):
        """添加用户的账套登录日志."""
        return await self._post("/jxc_api/Log/AddLoginLog", json_data=kwargs)

    async def add_operate_log(self, **kwargs):
        """添加一条账套操作日志记录."""
        return await self._post("/jxc_api/Log/AddOperateLog", json_data=kwargs)

    async def get_operate_logs(self, **kwargs):
        """获取账套操作日志分页数据."""
        return await self._post("/jxc_api/Log/GetOperateLogs", json_data=kwargs)

    async def get_ip_address(self):
        """获取IP地址编号."""
        return await self._post("/jxc_api/Log/GetIPAddress")

    async def get_login_logs(self, **kwargs):
        """获取账套登录日志分页记录."""
        return await self._post("/jxc_api/Log/GetLoginLogs", json_data=kwargs)

    async def add_user_operate_log(self, **kwargs):
        """添加一条用户操作日志记录."""
        return await self._post("/jxc_api/Log/AddUserOperateLog", json_data=kwargs)

    async def get_user_operate_logs(self, **kwargs):
        """获取用户操作日志分页记录."""
        return await self._post("/jxc_api/Log/GetUserOperateLogs", json_data=kwargs)

    async def get_all_users(self):
        """获取所有的用户[名称:::手机号]组合列表."""
        return await self._post("/jxc_api/Log/GetAllUsers")


class PrintTplAPI(_BaseAPI):
    """打印模板页面"""

    async def get_types(self):
        """打印模板类型列表."""
        return await self._post("/jxc_api/PrintTpl/GetTypes")

    async def get_templates(self, **kwargs):
        """打印模板列表."""
        return await self._post("/jxc_api/PrintTpl/GetTemplates", json_data=kwargs)

    async def get_for_print_dialog(self, **kwargs):
        """为打印对话框获取打印模板列表及模板类型."""
        return await self._post("/jxc_api/PrintTpl/GetForPrintDialog", json_data=kwargs)

    async def get_settings(self, **kwargs):
        """获取打印模板设置信息."""
        return await self._post("/jxc_api/PrintTpl/GetSettings", json_data=kwargs)

    async def save_preview(self, **kwargs):
        """保存预览设置效果，返回编号."""
        return await self._post("/jxc_api/PrintTpl/SavePreview", json_data=kwargs)

    async def preview(self, **kwargs):
        """预览设置效果."""
        return await self._post("/jxc_api/PrintTpl/Preview", json_data=kwargs)

    async def save_settings(self, **kwargs):
        """保存模板设置信息."""
        return await self._post("/jxc_api/PrintTpl/SaveSettings", json_data=kwargs)

    async def copy_template(self, **kwargs):
        """复制模板."""
        return await self._post("/jxc_api/PrintTpl/Copy", json_data=kwargs)

    async def delete_template(self, id_: int):
        """删除模板."""
        return await self._post("/jxc_api/PrintTpl/Delete", json_data={"id": id_})

    async def set_default(self, **kwargs):
        """设为默认模板."""
        return await self._post("/jxc_api/PrintTpl/SetDefault", json_data=kwargs)

    async def upload_image(self, **kwargs):
        """上传图片."""
        return await self._post("/jxc_api/PrintTpl/UploadImage", json_data=kwargs)


class FileDownloadCenterAPI(_BaseAPI):
    """文件下载中心"""

    async def search(self, **kwargs):
        """检索."""
        return await self._post("/jxc_api/FileDownloadCenter/Search", json_data=kwargs)

    async def export_data(self, **kwargs):
        """导出."""
        return await self._post("/jxc_api/FileDownloadCenter/Export", json_data=kwargs)

    async def delete(self, ids: list[int]):
        """删除."""
        return await self._post("/jxc_api/FileDownloadCenter/Delete", json_data={"ids": ids})

    async def add_log(self, **kwargs):
        """添加日志."""
        return await self._post("/jxc_api/FileDownloadCenter/AddLog", json_data=kwargs)


class PrintAPI(_BaseAPI):
    """打印相关"""

    async def save_print_request(self, **kwargs):
        """保存打印请求信息，返回标识."""
        return await self._post("/jxc_api/Print/Save", json_data=kwargs)

    async def update_print_count(self, **kwargs):
        """更新打印次数."""
        return await self._post("/jxc_api/Print/UpdatePrintNum", json_data=kwargs)


class AttachmentAPI(_BaseAPI):
    """附件相关接口"""

    async def get_list(self, **kwargs):
        """获取附件列表."""
        return await self._post("/jxc_api/Attachment/GetList", json_data=kwargs)

    async def delete(self, id_: int):
        """删除单个附件."""
        return await self._post("/jxc_api/Attachment/Delete", json_data={"id": id_})

    async def batch_delete(self, ids: list[int]):
        """批量删除附件."""
        return await self._post("/jxc_api/Attachment/BatchDelete", json_data={"ids": ids})

    async def add(self, **kwargs):
        """添加单条附件信息."""
        return await self._post("/jxc_api/Attachment/Add", json_data=kwargs)

    async def update(self, **kwargs):
        """更新附件."""
        return await self._post("/jxc_api/Attachment/Update", json_data=kwargs)

    async def update_doc_id(self, **kwargs):
        """更新附件记录中的单据ID."""
        return await self._post("/jxc_api/Attachment/UpdateDocId", json_data=kwargs)

    async def replace_attachments(self, **kwargs):
        """将原本单据或者资料关联的附件覆盖为新的附件."""
        return await self._post("/jxc_api/Attachment/ReplaceAttachments", json_data=kwargs)

    async def log_image_update(self, **kwargs):
        """记录图片更新日志."""
        return await self._post("/jxc_api/Attachment/LogImageUpdate", json_data=kwargs)
