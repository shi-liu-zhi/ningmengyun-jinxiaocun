# 柠檬云进销存开放平台 Python SDK

柠檬云进销存（云进销存）开放平台异步 Python SDK，基于 `httpx` 实现，覆盖全部开放 API 接口。

## 安装

```bash
pip install ningmengyun-jxc
```

## 快速开始

```python
import asyncio
from ningmengyun_jxc import JxcClient

async def main():
    client = JxcClient(
        token="your_bearer_token",
        account_book_id="your_account_book_id",
        # 默认使用生产环境，测试环境传 env="test"
    )
    
    # 获取仓库列表
    result = await client.balances.get_wh_list(featch_all=1)
    print(result.data)
    
    await client.aclose()

asyncio.run(main())
```

## 环境配置

| 环境 | SCMAPI_HOST |
|------|-------------|
| 生产 | https://jxcapi.ningmengyun.com |
| 测试 | http://scmtestapi.ningmengyun.com |

## API 覆盖率

SDK 覆盖开放平台全部的云进销存接口，按功能模块组织：

- **认证与公共接口** - OAuth2、账套管理、通用接口
- **商品库存** - 商品库存余额表、收发汇总/明细表、库存账龄分析
- **入库/出库** - 采购入库单、采购退货单、其它入库单、其它出库单
- **销售** - 销售订单、销售出库单、销售退货单、销售报表
- **采购** - 采购订单、采购入库单、采购退货单、采购报表
- **财务** - 收款单、付款单、转账单、核销单、费用
- **基础资料** - 客户、供应商、商品、仓库、账户、职员、计量单位
- **配置与系统** - 编码规则、列设置、打印模板、备份恢复、结账
- **附件与日志** - 附件管理、操作日志、登录日志

## 返回值

所有接口返回统一格式：

```python
@dataclass
class ApiResult:
    state: int       # 1000=成功, 2000=业务失败, 9999=接口失败
    sub_state: int
    msg: str
    data: Any
```
