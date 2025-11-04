-- SQL Table Definitions for Warehouse Order System
-- Normalized schema to avoid arrays in columns
-- SQLite Compatible Version

-- ============================================================================
-- MAIN ORDER TABLE
-- ============================================================================
CREATE TABLE ShipmentOrder (
    id INTEGER PRIMARY KEY,
    code TEXT NOT NULL,
    priority_id TEXT,
    customer_ref_code TEXT,
    depositor_ref_code TEXT,
    customer_order_no TEXT,
    depositor_order_no TEXT,
    warehouse_order_status_code TEXT,
    
    -- Customer Information
    customer_id INTEGER,
    customer_code TEXT,
    customer_description TEXT,
    
    -- Site and Warehouse Information
    inventory_site_id INTEGER,
    inventory_site_code TEXT,
    warehouse_id INTEGER,
    warehouse_code TEXT,
    warehouse_description TEXT,
    
    -- Depositor Information
    depositor_id INTEGER,
    depositor_code TEXT,
    depositor_description TEXT,
    
    -- Printing Preferences
    is_print_carrier_label_pack_list_as_label INTEGER,
    is_print_carrier_label_pack_list_on_same_page INTEGER,
    
    -- Carrier Information
    carrier_tracking_number TEXT,
    carrier_description TEXT,
    carrier_shipping_options_id INTEGER,
    carrier_depositor_list_id INTEGER,
    carrier_rate REAL,
    carrier_markup_rate REAL,
    carrier_package_type_id INTEGER,
    carrier_weight TEXT,
    carrier_billing_type_id INTEGER,
    carrier_billing_type_description TEXT,
    carrier_shipping_description TEXT,
    
    -- Order Type
    warehouse_order_type_id INTEGER,
    warehouse_order_type_code TEXT,
    is_amazon_fba INTEGER,
    
    -- Dates
    order_date TEXT,
    planned_delivery_date TEXT,
    planned_ship_date TEXT,
    planned_pick_date TEXT,
    actual_pick_date TEXT,
    actual_delivery_date TEXT,
    actual_ship_date TEXT,
    planned_pickup_date TEXT,
    invoice_date TEXT,
    entry_date_time TEXT,
    last_modified_date TEXT,
    cancellation_date TEXT,
    receipt_date TEXT,
    earliest_ship_date TEXT,
    latest_ship_date TEXT,
    earliest_delivery_date TEXT,
    latest_delivery_date TEXT,
    
    -- Notes and Instructions
    notes TEXT,
    instructions TEXT,
    gift_note TEXT,
    extra_notes TEXT,
    extra_notes1 TEXT,
    extra_notes2 TEXT,
    extra_notes3 TEXT,
    extra_notes4 TEXT,
    extra_notes5 TEXT,
    
    -- Document Flags
    is_document_exist TEXT,
    is_waybill_printed INTEGER,
    is_carrier_label_printed INTEGER,
    is_pick_list_printed INTEGER,
    
    -- Purchase Order
    purchase_order_id INTEGER,
    purchase_order_code TEXT,
    
    -- Status Flags
    is_imported INTEGER,
    is_exported INTEGER,
    is_exported2 INTEGER,
    is_exported4 INTEGER,
    is_exported5 INTEGER,
    is_backorder INTEGER,
    is_allocated INTEGER,
    is_picking_started INTEGER,
    is_picking_completed INTEGER,
    is_cancel_requested INTEGER,
    is_gift INTEGER,
    is_prime_order INTEGER,
    is_address_verified INTEGER,
    is_get_order_details INTEGER,
    is_auto_generate INTEGER,
    is_use_same_lot_number INTEGER,
    is_allow_changing_tax_and_duties_payor INTEGER,
    is_get_customer_address_info INTEGER,
    is_use_saturday_delivery INTEGER,
    is_skip_adress_verification_stamps INTEGER,
    is_fedex_one_rate INTEGER,
    
    -- Invoice Information
    invoice_customer_id INTEGER,
    invoice_customer_party_id INTEGER,
    invoice_customer_description TEXT,
    invoice_customer_address_id INTEGER,
    invoice_customer_address_description TEXT,
    invoice_no TEXT,
    delivery_note_no TEXT,
    
    -- Financial Information
    total_sales_gross_price REAL,
    total_sales_vat REAL,
    total_sales_discount REAL,
    cargo_discount REAL,
    total_markup_rate REAL,
    total_carrier_rate REAL,
    order_risk_score REAL,
    insurance_cost REAL,
    
    -- Additional Information
    account_number TEXT,
    driver TEXT,
    platenumber TEXT,
    billing_type_id INTEGER,
    billing_type_description TEXT,
    route_id INTEGER,
    route_description TEXT,
    channel_description TEXT,
    integration_key TEXT,
    entered_by TEXT,
    canceled_by TEXT,
    nof_shipment_label INTEGER,
    nof_products INTEGER,
    store_name TEXT,
    linked_channel_id INTEGER,
    linked_channel_description TEXT,
    
    -- Address References
    customer_address_id INTEGER,
    customer_address_description TEXT,
    
    -- Project Information
    project_id INTEGER,
    project_description TEXT,
    
    -- Receipt Information
    warehouse_receipt_id INTEGER,
    warehouse_receipt_code TEXT,
    warehouse_receipt_type_id INTEGER,
    receipt_order_code TEXT,
    
    -- Related Orders
    back_warehouse_order_code TEXT,
    back_warehouse_order_id INTEGER,
    drop_ship_master_order_id INTEGER,
    drop_ship_warehouse_order_code TEXT,
    drop_ship_notes TEXT,
    master_warehouse_order_code TEXT,
    warehouse_drop_ship_order_code TEXT,
    warehouse_back_order_code TEXT,
    warehouse_master_order_code TEXT,
    warehouse_receipt_order_code TEXT,
    
    -- Channel Information
    channel_order_code TEXT,
    client_party_id INTEGER,
    channel_depositor_parameter_id INTEGER,
    
    -- Warehouse Information
    po_window_warehouse_id INTEGER,
    
    -- Cancellation Information
    ware_order_cancel_reason_id INTEGER,
    ware_order_cancel_reason_description TEXT,
    warehouse_ord_return_reason_id INTEGER,
    warehouse_ord_return_reason_description TEXT,
    
    -- Order Items
    order_items TEXT,
    
    -- EDI Reference
    master_edi_reference TEXT,
    
    -- Priority
    priority INTEGER,
    
    -- Fraud Detection
    fraud_recommendation_id INTEGER,
    fraud_recommendation_code TEXT,
    fraud_recommendation_description TEXT,
    
    -- Shipment Method
    shipment_method_id INTEGER,
    shipment_method_description TEXT,
    
    -- Stock Information
    avaliable_stock_quantity INTEGER,
    
    -- Store
    store TEXT,
    
    -- Company
    company_name TEXT,
    
    -- Carrier Info
    party_carrier_info_id INTEGER,
    business_days_in_transit INTEGER,
    
    -- Supplier Information
    supplier_id INTEGER,
    supplier_address_id INTEGER,
    
    -- Customer Information
    customer_email TEXT,
    
    -- Operation Status
    warehouse_order_operation_status TEXT,
    
    -- FBA Order Information
    org_fba_order_id INTEGER,
    warehouse_fba_order_status_code TEXT,
    warehouse_fba_order_status_desc TEXT,
    
    -- Selected Order
    selected_order TEXT,
    
    -- Package Information
    package_code TEXT,
    sscc TEXT,
    shipment_type_id INTEGER,
    insurance_type TEXT,
    
    -- Tax and Duties
    taxes_and_duties_billing_type TEXT,
    tax_and_duties_payor_info TEXT,
    
    -- API Response Metadata
    success INTEGER,
    success_message TEXT,
    page_size INTEGER,
    selected_page_index INTEGER,
    page_count INTEGER,
    record_count INTEGER,
    
    -- Processing Metadata
    api_fetch_timestamp TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for shipment_order
CREATE INDEX idx_code ON ShipmentOrder(code);
CREATE INDEX idx_customer_id ON ShipmentOrder(customer_id);
CREATE INDEX idx_warehouse_id ON ShipmentOrder(warehouse_id);
CREATE INDEX idx_order_date ON ShipmentOrder(order_date);
CREATE INDEX idx_status_code ON ShipmentOrder(warehouse_order_status_code);
CREATE INDEX idx_last_modified ON ShipmentOrder(last_modified_date);

-- ============================================================================
-- ORDER LINE ITEMS TABLE
-- ============================================================================
CREATE TABLE ShipmentOrder_Line (
    id INTEGER PRIMARY KEY,
    code TEXT NOT NULL,
    warehouse_order_id INTEGER NOT NULL,
    
    -- Inventory Item Information
    inventory_item_id INTEGER,
    inventory_item_description TEXT,
    inventory_item_info TEXT,
    barcode TEXT,
    display_member TEXT,
    
    -- Pack Type Information
    inventory_item_pack_type_id INTEGER,
    inventory_item_pack_type_description TEXT,
    pack_quantity INTEGER,
    
    -- Insurance
    insurance_amount_per_unit REAL,
    
    -- EDI Reference
    edi_reference TEXT,
    
    -- Physical Dimensions
    unit_weight REAL,
    unit_volume REAL,
    total_weight REAL,
    total_volume REAL,
    line_weight REAL,
    
    -- Quantities
    allocated_cu_quantity INTEGER,
    picked_cu_quantity INTEGER,
    loaded_cu_quantity INTEGER,
    shipped_cu_quantity INTEGER,
    planned_pack_quantity INTEGER,
    planned_cu_quantity INTEGER,
    sorted_cu_quantity INTEGER,
    packed_cu_quantity INTEGER,
    cancelled_cu_quantity INTEGER,
    
    -- Free Attributes
    free_attr1 TEXT,
    free_attr2 TEXT,
    free_attr3 TEXT,
    
    -- Pricing
    currency_price REAL,
    tax_rate REAL,
    net_currency_price REAL,
    sales_unit_price REAL,
    
    -- Supplier
    supplier_id INTEGER,
    supplier_description TEXT,
    
    -- Notes
    notes1 TEXT,
    notes2 TEXT,
    notes3 TEXT,
    
    -- Channel Order Detail
    channel_order_detail_code TEXT,
    
    -- Lot and Batch Information
    lot_no TEXT,
    expiry_date TEXT,
    production_date TEXT,
    
    -- Package Type
    package_type TEXT,
    
    -- Stock Kit
    stock_kit_code TEXT,
    
    -- Suitability and Quarantine
    suitability_reason TEXT,
    quarantine_reason TEXT,

    -- Logiwa status IDs
    warehouse_status_id INTEGER,
    custom_status_id INTEGER,
    fba_status_id INTEGER,
    
    -- Metadata
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (warehouse_order_id) REFERENCES ShipmentOrder(id) ON DELETE CASCADE
);

-- Indexes for shipment_order_line
CREATE INDEX idx_line_warehouse_order_id ON ShipmentOrder_Line(warehouse_order_id);
CREATE INDEX idx_line_inventory_item_id ON ShipmentOrder_Line(inventory_item_id);
CREATE INDEX idx_line_barcode ON ShipmentOrder_Line(barcode);
CREATE INDEX idx_line_code ON ShipmentOrder_Line(code);

-- ============================================================================
-- ADDRESS TABLE
-- ============================================================================
CREATE TABLE ShipmentOrder_Address (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    warehouse_order_id INTEGER NOT NULL,
    address_type TEXT NOT NULL, -- 'SHIPPING', 'BILLING', 'THIRD_PARTY'
    
    -- Account Information
    account_number TEXT,
    
    -- Address Details
    country TEXT,
    state TEXT,
    city TEXT,
    customer_address TEXT,
    address_text TEXT,
    address_directions TEXT,
    postal_code TEXT,
    
    -- Metadata
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (warehouse_order_id) REFERENCES ShipmentOrder(id) ON DELETE CASCADE
);

-- Indexes for shipment_order_address
CREATE INDEX idx_address_warehouse_order_id ON ShipmentOrder_Address(warehouse_order_id);
CREATE INDEX idx_address_type ON ShipmentOrder_Address(address_type);


CREATE TABLE ShipmentOrder_Runs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fetch_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    success INTEGER
);


-- ============================================================================
-- STAGING TABLE
-- ============================================================================
CREATE TABLE ShipmentOrder_Staging (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    raw_json TEXT NOT NULL,
    fetch_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_id) REFERENCES ShipmentOrder(id) ON DELETE CASCADE
);

-- Create indexes separately in SQLite
CREATE INDEX idx_warehouse_order_id ON ShipmentOrder_Staging(order_id);
CREATE UNIQUE INDEX unique_order_custom_status ON ShipmentOrder_Staging(id, order_id);


-- ============================================================================
-- COMMENTS AND DOCUMENTATION
-- ============================================================================

-- Table Relationships:
-- 1. shipment_order (1) -> (Many) shipment_order_line
-- 2. shipment_order (1) -> (Many) shipment_order_address
