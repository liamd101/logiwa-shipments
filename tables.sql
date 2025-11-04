-- SQL Table Definitions for Warehouse Order System
-- Normalized schema to avoid arrays in columns

-- ============================================================================
-- MAIN ORDER TABLE
-- ============================================================================
CREATE TABLE shipment_order (
    id BIGINT PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    priority_id VARCHAR(50),
    customer_ref_code VARCHAR(255),
    depositor_ref_code VARCHAR(255),
    customer_order_no VARCHAR(255),
    depositor_order_no VARCHAR(255),
    warehouse_order_status_code VARCHAR(100),

    -- Customer Information
    customer_id BIGINT,
    customer_code VARCHAR(100),
    customer_description VARCHAR(500),

    -- Site and Warehouse Information
    inventory_site_id BIGINT,
    inventory_site_code VARCHAR(100),
    warehouse_id BIGINT,
    warehouse_code VARCHAR(100),
    warehouse_description VARCHAR(500),

    -- Depositor Information
    depositor_id BIGINT,
    depositor_code VARCHAR(100),
    depositor_description VARCHAR(500),

    -- Printing Preferences
    is_print_carrier_label_pack_list_as_label BOOLEAN,
    is_print_carrier_label_pack_list_on_same_page BOOLEAN,

    -- Carrier Information
    carrier_tracking_number VARCHAR(255),
    carrier_description VARCHAR(500),
    carrier_shipping_options_id BIGINT,
    carrier_depositor_list_id BIGINT,
    carrier_rate DECIMAL(18, 8),
    carrier_markup_rate DECIMAL(18, 8),
    carrier_package_type_id BIGINT,
    carrier_weight VARCHAR(50),
    carrier_billing_type_id BIGINT,
    carrier_billing_type_description VARCHAR(255),
    carrier_shipping_description VARCHAR(500),

    -- Order Type
    warehouse_order_type_id BIGINT,
    warehouse_order_type_code VARCHAR(100),
    is_amazon_fba BOOLEAN,

    -- Dates
    order_date TIMESTAMP,
    planned_delivery_date TIMESTAMP,
    planned_ship_date TIMESTAMP,
    planned_pick_date TIMESTAMP,
    actual_pick_date TIMESTAMP,
    actual_delivery_date TIMESTAMP,
    actual_ship_date TIMESTAMP,
    planned_pickup_date TIMESTAMP,
    invoice_date TIMESTAMP,
    entry_date_time TIMESTAMP,
    last_modified_date TIMESTAMP,
    cancellation_date TIMESTAMP,
    receipt_date TIMESTAMP,
    earliest_ship_date TIMESTAMP,
    latest_ship_date TIMESTAMP,
    earliest_delivery_date TIMESTAMP,
    latest_delivery_date TIMESTAMP,

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
    is_document_exist VARCHAR(50),
    is_waybill_printed BOOLEAN,
    is_carrier_label_printed BOOLEAN,
    is_pick_list_printed BOOLEAN,

    -- Purchase Order
    purchase_order_id BIGINT,
    purchase_order_code VARCHAR(255),

    -- Status Flags
    is_imported BOOLEAN,
    is_exported BOOLEAN,
    is_exported2 BOOLEAN,
    is_exported4 BOOLEAN,
    is_exported5 BOOLEAN,
    is_backorder BOOLEAN,
    is_allocated BOOLEAN,
    is_picking_started BOOLEAN,
    is_picking_completed BOOLEAN,
    is_cancel_requested BOOLEAN,
    is_gift BOOLEAN,
    is_prime_order BOOLEAN,
    is_address_verified BOOLEAN,
    is_get_order_details BOOLEAN,
    is_auto_generate BOOLEAN,
    is_use_same_lot_number BOOLEAN,
    is_allow_changing_tax_and_duties_payor BOOLEAN,
    is_get_customer_address_info BOOLEAN,
    is_use_saturday_delivery BOOLEAN,
    is_skip_adress_verification_stamps BOOLEAN,
    is_fedex_one_rate BOOLEAN,

    -- Invoice Information
    invoice_customer_id BIGINT,
    invoice_customer_party_id BIGINT,
    invoice_customer_description VARCHAR(500),
    invoice_customer_address_id BIGINT,
    invoice_customer_address_description VARCHAR(500),
    invoice_no VARCHAR(255),
    delivery_note_no VARCHAR(255),

    -- Financial Information
    total_sales_gross_price DECIMAL(18, 8),
    total_sales_vat DECIMAL(18, 8),
    total_sales_discount DECIMAL(18, 8),
    cargo_discount DECIMAL(18, 8),
    total_markup_rate DECIMAL(18, 8),
    total_carrier_rate DECIMAL(18, 8),
    order_risk_score DECIMAL(18, 8),
    insurance_cost DECIMAL(18, 8),

    -- Additional Information
    account_number VARCHAR(100),
    driver VARCHAR(255),
    platenumber VARCHAR(100),
    billing_type_id BIGINT,
    billing_type_description VARCHAR(255),
    route_id BIGINT,
    route_description VARCHAR(500),
    channel_description VARCHAR(500),
    integration_key VARCHAR(255),
    entered_by VARCHAR(255),
    canceled_by VARCHAR(255),
    nof_shipment_label INT,
    nof_products INT,
    store_name VARCHAR(255),
    linked_channel_id BIGINT,
    linked_channel_description VARCHAR(500),

    -- Address References
    customer_address_id BIGINT,
    customer_address_description TEXT,

    -- Project Information
    project_id BIGINT,
    project_description VARCHAR(500),

    -- Receipt Information
    warehouse_receipt_id BIGINT,
    warehouse_receipt_code VARCHAR(255),
    warehouse_receipt_type_id BIGINT,
    receipt_order_code VARCHAR(255),

    -- Related Orders
    back_warehouse_order_code VARCHAR(255),
    back_warehouse_order_id BIGINT,
    drop_ship_master_order_id BIGINT,
    drop_ship_warehouse_order_code VARCHAR(255),
    drop_ship_notes TEXT,
    master_warehouse_order_code VARCHAR(255),
    warehouse_drop_ship_order_code VARCHAR(255),
    warehouse_back_order_code VARCHAR(255),
    warehouse_master_order_code VARCHAR(255),
    warehouse_receipt_order_code VARCHAR(255),

    -- Channel Information
    channel_order_code VARCHAR(255),
    client_party_id BIGINT,
    channel_depositor_parameter_id BIGINT,

    -- Warehouse Information
    po_window_warehouse_id BIGINT,

    -- Cancellation Information
    ware_order_cancel_reason_id BIGINT,
    ware_order_cancel_reason_description VARCHAR(500),
    warehouse_ord_return_reason_id BIGINT,
    warehouse_ord_return_reason_description VARCHAR(500),

    -- Order Items
    order_items TEXT,

    -- EDI Reference
    master_edi_reference VARCHAR(255),

    -- Priority
    priority INT,

    -- Fraud Detection
    fraud_recommendation_id BIGINT,
    fraud_recommendation_code VARCHAR(100),
    fraud_recommendation_description VARCHAR(500),

    -- Shipment Method
    shipment_method_id BIGINT,
    shipment_method_description VARCHAR(500),

    -- Stock Information
    avaliable_stock_quantity INT,

    -- Store
    store VARCHAR(255),

    -- Company
    company_name VARCHAR(500),

    -- Carrier Info
    party_carrier_info_id BIGINT,
    business_days_in_transit INT,

    -- Supplier Information
    supplier_id BIGINT,
    supplier_address_id BIGINT,

    -- Customer Information
    customer_email VARCHAR(500),

    -- Operation Status
    warehouse_order_operation_status VARCHAR(255),

    -- FBA Order Information
    org_fba_order_id BIGINT,
    warehouse_fba_order_status_code VARCHAR(100),
    warehouse_fba_order_status_desc VARCHAR(500),

    -- Selected Order
    selected_order VARCHAR(255),

    -- Package Information
    package_code VARCHAR(255),
    sscc VARCHAR(255),
    shipment_type_id BIGINT,
    insurance_type VARCHAR(100),

    -- Tax and Duties
    taxes_and_duties_billing_type VARCHAR(100),
    tax_and_duties_payor_info TEXT,

    -- API Response Metadata
    success BOOLEAN,
    success_message TEXT,
    page_size INT,
    selected_page_index INT,
    page_count INT,
    record_count INT,

    -- Processing Metadata
    api_fetch_timestamp TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    -- Indexes
    INDEX idx_code (code),
    INDEX idx_customer_id (customer_id),
    INDEX idx_warehouse_id (warehouse_id),
    INDEX idx_order_date (order_date),
    INDEX idx_status_code (warehouse_order_status_code),
    INDEX idx_last_modified (last_modified_date)
);

-- ============================================================================
-- ORDER LINE ITEMS TABLE
-- ============================================================================
CREATE TABLE shipment_order_line (
    id BIGINT PRIMARY KEY,
    code VARCHAR(255) NOT NULL,
    warehouse_order_id BIGINT NOT NULL,

    -- Inventory Item Information
    inventory_item_id BIGINT,
    inventory_item_description VARCHAR(500),
    inventory_item_info VARCHAR(1000),
    barcode VARCHAR(255),
    display_member VARCHAR(1000),

    -- Pack Type Information
    inventory_item_pack_type_id BIGINT,
    inventory_item_pack_type_description VARCHAR(255),
    pack_quantity INT,

    -- Insurance
    insurance_amount_per_unit DECIMAL(18, 8),

    -- EDI Reference
    edi_reference VARCHAR(255),

    -- Physical Dimensions
    unit_weight DECIMAL(18, 8),
    unit_volume DECIMAL(18, 8),
    total_weight DECIMAL(18, 8),
    total_volume DECIMAL(18, 8),
    line_weight DECIMAL(18, 8),

    -- Quantities
    allocated_cu_quantity INT,
    picked_cu_quantity INT,
    loaded_cu_quantity INT,
    shipped_cu_quantity INT,
    planned_pack_quantity INT,
    planned_cu_quantity INT,
    sorted_cu_quantity INT,
    packed_cu_quantity INT,
    cancelled_cu_quantity INT,

    -- Free Attributes
    free_attr1 VARCHAR(500),
    free_attr2 VARCHAR(500),
    free_attr3 VARCHAR(500),

    -- Pricing
    currency_price DECIMAL(18, 8),
    tax_rate DECIMAL(18, 8),
    net_currency_price DECIMAL(18, 8),
    sales_unit_price DECIMAL(18, 8),

    -- Supplier
    supplier_id BIGINT,
    supplier_description VARCHAR(500),

    -- Notes
    notes1 TEXT,
    notes2 TEXT,
    notes3 TEXT,

    -- Channel Order Detail
    channel_order_detail_code VARCHAR(255),

    -- Lot and Batch Information
    lot_no VARCHAR(255),
    expiry_date TIMESTAMP,
    production_date TIMESTAMP,

    -- Package Type
    package_type VARCHAR(255),

    -- Stock Kit
    stock_kit_code VARCHAR(255),

    -- Suitability and Quarantine
    suitability_reason VARCHAR(500),
    quarantine_reason VARCHAR(500),

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_inventory_item_id (inventory_item_id),
    INDEX idx_barcode (barcode),
    INDEX idx_code (code)
);

-- ============================================================================
-- ADDRESS TABLE
-- ============================================================================
CREATE TABLE shipment_order_address (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    address_type VARCHAR(50) NOT NULL, -- 'SHIPPING', 'BILLING', 'THIRD_PARTY'

    -- Account Information
    account_number VARCHAR(100),

    -- Address Details
    country VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(255),
    customer_address VARCHAR(1000),
    address_text TEXT,
    address_directions TEXT,
    postal_code VARCHAR(50),

    -- Metadata
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_address_type (address_type)
);

-- ============================================================================
-- JUNCTION TABLES FOR ARRAY FIELDS
-- ============================================================================

-- Warehouse Order Status IDs
CREATE TABLE shipment_order_status_mapping (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    status_id BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_status_id (status_id),
    UNIQUE KEY unique_order_status (warehouse_order_id, status_id)
);

-- Carrier IDs
CREATE TABLE shipment_order_carrier_mapping (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    carrier_id BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_carrier_id (carrier_id),
    UNIQUE KEY unique_order_carrier (warehouse_order_id, carrier_id)
);

-- Channel IDs
CREATE TABLE shipment_order_channel_mapping (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    channel_id BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_channel_id (channel_id),
    UNIQUE KEY unique_order_channel (warehouse_order_id, channel_id)
);

-- Order Custom Status IDs
CREATE TABLE shipment_order_custom_status_mapping (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    custom_status_id BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_custom_status_id (custom_status_id),
    UNIQUE KEY unique_order_custom_status (warehouse_order_id, custom_status_id)
);

-- Warehouse FBA Order Status IDs
CREATE TABLE shipment_order_fba_status_mapping (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    fba_status_id BIGINT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_fba_status_id (fba_status_id),
    UNIQUE KEY unique_order_fba_status (warehouse_order_id, fba_status_id)
);

-- ============================================================================
-- ERROR TABLE
-- ============================================================================
CREATE TABLE shipment_order_error (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    error_message TEXT NOT NULL,
    error_code VARCHAR(100),
    error_field VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    INDEX idx_error_code (error_code)
);

create table ShipmentOrder_Runs (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    fetched_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    success BOOLEAN
);

-- ============================================================================
-- STAGING TABLE
-- ============================================================================
CREATE TABLE staging_shipment_order (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    warehouse_order_id BIGINT NOT NULL,
    raw_json TEXT NOT NULL,
    fetch_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (warehouse_order_id) REFERENCES shipment_order(id) ON DELETE CASCADE,

    -- Indexes
    INDEX idx_warehouse_order_id (warehouse_order_id),
    UNIQUE KEY unique_order_custom_status (id, warehouse_order_id)
);

-- ============================================================================
-- COMMENTS AND DOCUMENTATION
-- ============================================================================

-- Table Relationships:
-- 1. shipment_order (1) -> (Many) shipment_order_line
-- 2. shipment_order (1) -> (Many) shipment_order_address
