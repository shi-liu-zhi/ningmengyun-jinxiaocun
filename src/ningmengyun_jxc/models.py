from dataclasses import dataclass, field
from typing import Any, Optional
from datetime import datetime


@dataclass
class ApiResult:
    """Standard API response wrapper."""
    state: int = 0
    sub_state: int = 0
    msg: str = ""
    data: Any = None


# ── Common parameter types ──────────────────────────────────────────

@dataclass
class Pagination:
    page_index: int = 0
    page_size: int = 20
    use_pager: bool = True


# ── Balances / 商品库存余额表 ───────────────────────────────────────

@dataclass
class GetWhListPara:
    featch_all: int = 0  # 0=授权查询 1=查询全部
    show_disable_wh: bool = False


@dataclass
class StockBalanceSearchCondition:
    stock_date: Optional[datetime] = None
    wh_ids: Optional[list[int]] = None
    show_disable_wh: bool = False
    wh_cat_id: Optional[list[int]] = None
    wh_range: int = 0
    prod_ids: Optional[list[int]] = None
    cat_id: Optional[list[int]] = None
    spec: Optional[str] = None
    with_zero: bool = False
    with_minus: bool = False
    show_disable_prod: bool = False
    use_ap: bool = False
    keyword: Optional[str] = None
    load_price: bool = True
    none_data_after_wh_cat_filter: bool = False
    final_stock_flag: bool = False
    page_index: int = 0
    page_size: int = 0
    use_pager: bool = False
    use_async_file_process: bool = False
    async_file_type: int = 0


# ── Inventory / 盘点单 ──────────────────────────────────────────────

@dataclass
class InventoryOrder:
    """盘点单"""
    id: Optional[int] = None
    no: Optional[str] = None
    inventory_date: Optional[str] = None
    wh_id: Optional[int] = None
    wh_name: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    details: Optional[list[dict]] = None


# ── Common order fields ─────────────────────────────────────────────

@dataclass
class OrderItem:
    """单据明细行"""
    prod_id: int = 0
    prod_name: Optional[str] = None
    spec: Optional[str] = None
    unit_id: Optional[int] = None
    unit_name: Optional[str] = None
    qty: float = 0
    price: float = 0
    amount: float = 0
    remark: Optional[str] = None


@dataclass
class BaseOrder:
    """单据基类"""
    id: Optional[int] = None
    no: Optional[str] = None
    date: Optional[str] = None
    operator_id: Optional[int] = None
    operator_name: Optional[str] = None
    dept_id: Optional[int] = None
    dept_name: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    details: Optional[list[OrderItem]] = None


# ── Customer / 客户 ─────────────────────────────────────────────────

@dataclass
class Customer:
    id: Optional[int] = None
    no: Optional[str] = None
    name: Optional[str] = None
    short_name: Optional[str] = None
    contact: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    category_id: Optional[int] = None
    category_name: Optional[str] = None
    balance: float = 0.0
    payable: float = 0.0
    initial_balance: float = 0.0


# ── Vendor / 供应商 ─────────────────────────────────────────────────

@dataclass
class Vendor:
    id: Optional[int] = None
    no: Optional[str] = None
    name: Optional[str] = None
    short_name: Optional[str] = None
    contact: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    category_id: Optional[int] = None
    category_name: Optional[str] = None
    balance: float = 0.0


# ── Warehouse / 仓库 ────────────────────────────────────────────────

@dataclass
class Warehouse:
    id: Optional[int] = None
    no: Optional[str] = None
    name: Optional[str] = None
    contact: Optional[str] = None
    phone: Optional[str] = None
    address: Optional[str] = None
    remark: Optional[str] = None
    status: Optional[int] = None
    category_id: Optional[int] = None


# ── Account / 账户 ──────────────────────────────────────────────────

@dataclass
class Account:
    id: Optional[int] = None
    no: Optional[str] = None
    name: Optional[str] = None
    account_no: Optional[str] = None
    bank: Optional[str] = None
    balance: float = 0.0
    status: Optional[int] = None
    remark: Optional[str] = None


# ── Employee / 职员 ─────────────────────────────────────────────────

@dataclass
class Employee:
    id: Optional[int] = None
    no: Optional[str] = None
    name: Optional[str] = None
    phone: Optional[str] = None
    dept_id: Optional[int] = None
    dept_name: Optional[str] = None
    status: Optional[int] = None
    remark: Optional[str] = None


# ── Unit / 计量单位 ─────────────────────────────────────────────────

@dataclass
class Unit:
    id: Optional[int] = None
    name: Optional[str] = None
    status: Optional[int] = None
