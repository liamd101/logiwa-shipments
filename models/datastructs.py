"""
Data models for Warehouse Order API response
Normalized structure for SQL storage
"""

from dataclasses import dataclass
from typing import Optional
from datetime import datetime
from decimal import Decimal


@dataclass
class ShipmentOrder:
    """Main order header table"""

    id: int
    code: str
    priority_id: Optional[str] = None
    customer_ref_code: Optional[str] = None
    depositor_ref_code: Optional[str] = None
    customer_order_no: Optional[str] = None
    depositor_order_no: Optional[str] = None
    warehouse_order_status_code: Optional[str] = None
    customer_id: Optional[int] = None
    customer_code: Optional[str] = None
    customer_description: Optional[str] = None
    inventory_site_id: Optional[int] = None
    inventory_site_code: Optional[str] = None
    warehouse_id: Optional[int] = None
    warehouse_code: Optional[str] = None
    warehouse_description: Optional[str] = None
    depositor_id: Optional[int] = None
    depositor_code: Optional[str] = None
    depositor_description: Optional[str] = None
    is_print_carrier_label_pack_list_as_label: Optional[bool] = None
    is_print_carrier_label_pack_list_on_same_page: Optional[bool] = None
    carrier_tracking_number: Optional[str] = None
    warehouse_order_type_id: Optional[int] = None
    warehouse_order_type_code: Optional[str] = None
    is_amazon_fba: Optional[bool] = None
    order_date: Optional[datetime] = None
    planned_delivery_date: Optional[datetime] = None
    planned_ship_date: Optional[datetime] = None
    notes: Optional[str] = None
    is_document_exist: Optional[str] = None
    purchase_order_id: Optional[int] = None
    purchase_order_code: Optional[str] = None
    is_imported: Optional[bool] = None
    is_exported: Optional[bool] = None
    is_exported4: Optional[bool] = None
    is_exported5: Optional[bool] = None
    is_backorder: Optional[bool] = None
    nof_shipment_label: Optional[int] = None
    is_allocated: Optional[bool] = None
    is_picking_started: Optional[bool] = None
    is_picking_completed: Optional[bool] = None
    invoice_customer_id: Optional[int] = None
    invoice_customer_party_id: Optional[int] = None
    invoice_customer_description: Optional[str] = None
    invoice_customer_address_id: Optional[int] = None
    invoice_customer_address_description: Optional[str] = None
    total_sales_gross_price: Optional[Decimal] = None
    total_sales_vat: Optional[Decimal] = None
    total_sales_discount: Optional[Decimal] = None
    instructions: Optional[str] = None
    account_number: Optional[str] = None
    driver: Optional[str] = None
    platenumber: Optional[str] = None
    billing_type_id: Optional[int] = None
    billing_type_description: Optional[str] = None
    route_id: Optional[int] = None
    route_description: Optional[str] = None
    channel_description: Optional[str] = None
    is_cancel_requested: Optional[bool] = None
    carrier_description: Optional[str] = None
    integration_key: Optional[str] = None
    entered_by: Optional[str] = None
    canceled_by: Optional[str] = None
    carrier_shipping_options_id: Optional[int] = None
    carrier_depositor_list_id: Optional[int] = None
    nof_products: Optional[int] = None
    store_name: Optional[str] = None
    linked_channel_id: Optional[int] = None
    linked_channel_description: Optional[str] = None
    carrier_rate: Optional[Decimal] = None
    carrier_markup_rate: Optional[Decimal] = None
    carrier_package_type_id: Optional[int] = None
    customer_address_id: Optional[int] = None
    customer_address_description: Optional[str] = None
    planned_pick_date: Optional[datetime] = None
    actual_pick_date: Optional[datetime] = None
    actual_delivery_date: Optional[datetime] = None
    project_id: Optional[int] = None
    project_description: Optional[str] = None
    warehouse_receipt_id: Optional[int] = None
    warehouse_receipt_code: Optional[str] = None
    back_warehouse_order_code: Optional[str] = None
    drop_ship_master_order_id: Optional[int] = None
    drop_ship_warehouse_order_code: Optional[str] = None
    drop_ship_notes: Optional[str] = None
    is_waybill_printed: Optional[bool] = None
    invoice_no: Optional[str] = None
    delivery_note_no: Optional[str] = None
    is_carrier_label_printed: Optional[bool] = None
    channel_order_code: Optional[str] = None
    carrier_weight: Optional[str] = None
    client_party_id: Optional[int] = None
    po_window_warehouse_id: Optional[int] = None
    ware_order_cancel_reason_id: Optional[int] = None
    ware_order_cancel_reason_description: Optional[str] = None
    is_gift: Optional[bool] = None
    gift_note: Optional[str] = None
    order_items: Optional[str] = None
    extra_notes: Optional[str] = None
    extra_notes1: Optional[str] = None
    extra_notes2: Optional[str] = None
    extra_notes3: Optional[str] = None
    extra_notes4: Optional[str] = None
    extra_notes5: Optional[str] = None
    master_edi_reference: Optional[str] = None
    priority: Optional[int] = None
    fraud_recommendation_id: Optional[int] = None
    fraud_recommendation_code: Optional[str] = None
    fraud_recommendation_description: Optional[str] = None
    order_risk_score: Optional[Decimal] = None
    is_exported2: Optional[bool] = None
    shipment_method_id: Optional[int] = None
    shipment_method_description: Optional[str] = None
    is_address_verified: Optional[bool] = None
    avaliable_stock_quantity: Optional[int] = None
    store: Optional[str] = None
    channel_depositor_parameter_id: Optional[int] = None
    carrier_billing_type_id: Optional[int] = None
    carrier_billing_type_description: Optional[str] = None
    is_pick_list_printed: Optional[bool] = None
    is_prime_order: Optional[bool] = None
    invoice_date: Optional[datetime] = None
    entry_date_time: Optional[datetime] = None
    cargo_discount: Optional[Decimal] = None
    warehouse_ord_return_reason_id: Optional[int] = None
    warehouse_ord_return_reason_description: Optional[str] = None
    company_name: Optional[str] = None
    total_markup_rate: Optional[Decimal] = None
    total_carrier_rate: Optional[Decimal] = None
    actual_ship_date: Optional[datetime] = None
    planned_pickup_date: Optional[datetime] = None
    carrier_shipping_description: Optional[str] = None
    is_get_order_details: Optional[bool] = None
    last_modified_date: Optional[datetime] = None
    cancellation_date: Optional[datetime] = None
    master_warehouse_order_code: Optional[str] = None
    party_carrier_info_id: Optional[int] = None
    business_days_in_transit: Optional[int] = None
    supplier_id: Optional[int] = None
    supplier_address_id: Optional[int] = None
    receipt_order_code: Optional[str] = None
    receipt_date: Optional[datetime] = None
    warehouse_receipt_type_id: Optional[int] = None
    is_auto_generate: Optional[bool] = None
    is_use_same_lot_number: Optional[bool] = None
    is_allow_changing_tax_and_duties_payor: Optional[bool] = None
    is_get_customer_address_info: Optional[bool] = None
    customer_email: Optional[str] = None
    warehouse_drop_ship_order_code: Optional[str] = None
    warehouse_back_order_code: Optional[str] = None
    warehouse_master_order_code: Optional[str] = None
    warehouse_receipt_order_code: Optional[str] = None
    warehouse_order_operation_status: Optional[str] = None
    org_fba_order_id: Optional[int] = None
    warehouse_fba_order_status_code: Optional[str] = None
    warehouse_fba_order_status_desc: Optional[str] = None
    selected_order: Optional[str] = None
    package_code: Optional[str] = None
    sscc: Optional[str] = None
    shipment_type_id: Optional[int] = None
    insurance_cost: Optional[Decimal] = None
    insurance_type: Optional[str] = None
    is_use_saturday_delivery: Optional[bool] = None
    is_skip_adress_verification_stamps: Optional[bool] = None
    is_fedex_one_rate: Optional[bool] = None
    taxes_and_duties_billing_type: Optional[str] = None
    tax_and_duties_payor_info: Optional[str] = None
    back_warehouse_order_id: Optional[int] = None
    earliest_ship_date: Optional[datetime] = None
    latest_ship_date: Optional[datetime] = None
    earliest_delivery_date: Optional[datetime] = None
    latest_delivery_date: Optional[datetime] = None
    # Metadata fields
    success: Optional[bool] = None
    success_message: Optional[str] = None
    page_size: Optional[int] = None
    selected_page_index: Optional[int] = None
    page_count: Optional[int] = None
    record_count: Optional[int] = None
    # Processing metadata
    api_fetch_timestamp: Optional[datetime] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ShipmentOrderLine:
    """Order line items - DetailInfo array"""

    id: int
    code: str
    warehouse_order_id: int
    inventory_item_id: Optional[int] = None
    inventory_item_description: Optional[str] = None
    inventory_item_info: Optional[str] = None
    barcode: Optional[str] = None
    display_member: Optional[str] = None
    inventory_item_pack_type_id: Optional[int] = None
    inventory_item_pack_type_description: Optional[str] = None
    pack_quantity: Optional[int] = None
    insurance_amount_per_unit: Optional[Decimal] = None
    edi_reference: Optional[str] = None
    unit_weight: Optional[Decimal] = None
    unit_volume: Optional[Decimal] = None
    allocated_cu_quantity: Optional[int] = None
    picked_cu_quantity: Optional[int] = None
    loaded_cu_quantity: Optional[int] = None
    shipped_cu_quantity: Optional[int] = None
    planned_pack_quantity: Optional[int] = None
    planned_cu_quantity: Optional[int] = None
    sorted_cu_quantity: Optional[int] = None
    packed_cu_quantity: Optional[int] = None
    cancelled_cu_quantity: Optional[int] = None
    free_attr1: Optional[str] = None
    free_attr2: Optional[str] = None
    free_attr3: Optional[str] = None
    currency_price: Optional[Decimal] = None
    tax_rate: Optional[Decimal] = None
    net_currency_price: Optional[Decimal] = None
    total_weight: Optional[Decimal] = None
    total_volume: Optional[Decimal] = None
    line_weight: Optional[Decimal] = None
    supplier_id: Optional[int] = None
    supplier_description: Optional[str] = None
    notes1: Optional[str] = None
    notes2: Optional[str] = None
    notes3: Optional[str] = None
    sales_unit_price: Optional[Decimal] = None
    channel_order_detail_code: Optional[str] = None
    lot_no: Optional[str] = None
    expiry_date: Optional[datetime] = None
    production_date: Optional[datetime] = None
    package_type: Optional[str] = None
    stock_kit_code: Optional[str] = None
    suitability_reason: Optional[str] = None
    quarantine_reason: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ShipmentOrderAddress:
    """Shipping and billing addresses - based on ThirdPartyAccount structure"""

    id: int  # Auto-generated
    warehouse_order_id: int
    address_type: str  # 'SHIPPING', 'BILLING', 'THIRD_PARTY'
    account_number: Optional[str] = None
    country: Optional[str] = None
    state: Optional[str] = None
    city: Optional[str] = None
    customer_address: Optional[str] = None
    address_text: Optional[str] = None
    address_directions: Optional[str] = None
    postal_code: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


@dataclass
class ChannelId:
    """"""

    order_id: int
    channel_id: int


@dataclass
class WarehouseOrderStatusId:
    """"""

    order_id: int
    status_id: int


@dataclass
class WarehouseFBAOrderStatusId:
    """"""

    order_id: int
    status_id: int


@dataclass
class CustomStatus:
    """"""

    order_id: int
    status_id: int


@dataclass
class CarrierId:
    """"""

    order_id: int
    carrier_id: int
