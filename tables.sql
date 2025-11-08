-- SQL Table Definitions for Warehouse Order System
-- Normalized schema to avoid arrays in columns
-- Microsoft SQL Server 2019 (Version 15) Compatible Version

-- ============================================================================
-- MAIN ORDER TABLE
-- ============================================================================
CREATE TABLE dbo.ShipmentOrder (
    id INT PRIMARY KEY,
    code NVARCHAR(255) NOT NULL,
    priority_id NVARCHAR(255),
    customer_ref_code NVARCHAR(255),
    depositor_ref_code NVARCHAR(255),
    customer_order_no NVARCHAR(255),
    depositor_order_no NVARCHAR(255),
    warehouse_order_status_code NVARCHAR(255),
    
    -- Customer Information
    customer_id INT,
    customer_code NVARCHAR(255),
    customer_description NVARCHAR(255),
    
    -- Site and Warehouse Information
    inventory_site_id INT,
    inventory_site_code NVARCHAR(255),
    warehouse_id INT,
    warehouse_code NVARCHAR(255),
    warehouse_description NVARCHAR(255),
    
    -- Depositor Information
    depositor_id INT,
    depositor_code NVARCHAR(255),
    depositor_description NVARCHAR(255),
    
    -- Printing Preferences
    is_print_carrier_label_pack_list_as_label BIT,
    is_print_carrier_label_pack_list_on_same_page BIT,
    
    -- Carrier Information
    carrier_tracking_number NVARCHAR(255),
    carrier_description NVARCHAR(255),
    carrier_shipping_options_id INT,
    carrier_depositor_list_id INT,
    carrier_rate DECIMAL(18,2),
    carrier_markup_rate DECIMAL(18,2),
    carrier_package_type_id INT,
    carrier_weight NVARCHAR(255),
    carrier_billing_type_id INT,
    carrier_billing_type_description NVARCHAR(255),
    carrier_shipping_description NVARCHAR(255),
    
    -- Order Type
    warehouse_order_type_id INT,
    warehouse_order_type_code NVARCHAR(255),
    is_amazon_fba BIT,
    
    -- Dates
    order_date DATETIME2,
    planned_delivery_date DATETIME2,
    planned_ship_date DATETIME2,
    planned_pick_date DATETIME2,
    actual_pick_date DATETIME2,
    actual_delivery_date DATETIME2,
    actual_ship_date DATETIME2,
    planned_pickup_date DATETIME2,
    invoice_date DATETIME2,
    entry_date_time DATETIME2,
    last_modified_date DATETIME2,
    cancellation_date DATETIME2,
    receipt_date DATETIME2,
    earliest_ship_date DATETIME2,
    latest_ship_date DATETIME2,
    earliest_delivery_date DATETIME2,
    latest_delivery_date DATETIME2,
    
    -- Notes and Instructions
    notes NVARCHAR(255),
    instructions NVARCHAR(255),
    gift_note NVARCHAR(255),
    extra_notes NVARCHAR(255),
    extra_notes1 NVARCHAR(255),
    extra_notes2 NVARCHAR(255),
    extra_notes3 NVARCHAR(255),
    extra_notes4 NVARCHAR(255),
    extra_notes5 NVARCHAR(255),
    
    -- Document Flags
    is_document_exist NVARCHAR(255),
    is_waybill_printed BIT,
    is_carrier_label_printed BIT,
    is_pick_list_printed BIT,
    
    -- Purchase Order
    purchase_order_id INT,
    purchase_order_code NVARCHAR(255),
    
    -- Status Flags
    is_imported BIT,
    is_exported BIT,
    is_exported2 BIT,
    is_exported4 BIT,
    is_exported5 BIT,
    is_backorder BIT,
    is_allocated BIT,
    is_picking_started BIT,
    is_picking_completed BIT,
    is_cancel_requested BIT,
    is_gift BIT,
    is_prime_order BIT,
    is_address_verified BIT,
    is_get_order_details BIT,
    is_auto_generate BIT,
    is_use_same_lot_number BIT,
    is_allow_changing_tax_and_duties_payor BIT,
    is_get_customer_address_info BIT,
    is_use_saturday_delivery BIT,
    is_skip_adress_verification_stamps BIT,
    is_fedex_one_rate BIT,
    
    -- Invoice Information
    invoice_customer_id INT,
    invoice_customer_party_id INT,
    invoice_customer_description NVARCHAR(255),
    invoice_customer_address_id INT,
    invoice_customer_address_description NVARCHAR(255),
    invoice_no NVARCHAR(255),
    delivery_note_no NVARCHAR(255),
    
    -- Financial Information
    total_sales_gross_price DECIMAL(18,2),
    total_sales_vat DECIMAL(18,2),
    total_sales_discount DECIMAL(18,2),
    cargo_discount DECIMAL(18,2),
    total_markup_rate DECIMAL(18,2),
    total_carrier_rate DECIMAL(18,2),
    order_risk_score DECIMAL(18,2),
    insurance_cost DECIMAL(18,2),
    
    -- Additional Information
    account_number NVARCHAR(255),
    driver NVARCHAR(255),
    platenumber NVARCHAR(255),
    billing_type_id INT,
    billing_type_description NVARCHAR(255),
    route_id INT,
    route_description NVARCHAR(255),
    channel_description NVARCHAR(255),
    integration_key NVARCHAR(255),
    entered_by NVARCHAR(255),
    canceled_by NVARCHAR(255),
    nof_shipment_label INT,
    nof_products INT,
    store_name NVARCHAR(255),
    linked_channel_id INT,
    linked_channel_description NVARCHAR(255),
    
    -- Address References
    customer_address_id INT,
    customer_address_description NVARCHAR(255),
    
    -- Project Information
    project_id INT,
    project_description NVARCHAR(255),
    
    -- Receipt Information
    warehouse_receipt_id INT,
    warehouse_receipt_code NVARCHAR(255),
    warehouse_receipt_type_id INT,
    receipt_order_code NVARCHAR(255),
    
    -- Related Orders
    back_warehouse_order_code NVARCHAR(255),
    back_warehouse_order_id INT,
    drop_ship_master_order_id INT,
    drop_ship_warehouse_order_code NVARCHAR(255),
    drop_ship_notes NVARCHAR(255),
    master_warehouse_order_code NVARCHAR(255),
    warehouse_drop_ship_order_code NVARCHAR(255),
    warehouse_back_order_code NVARCHAR(255),
    warehouse_master_order_code NVARCHAR(255),
    warehouse_receipt_order_code NVARCHAR(255),
    
    -- Channel Information
    channel_order_code NVARCHAR(255),
    client_party_id INT,
    channel_depositor_parameter_id INT,
    
    -- Warehouse Information
    po_window_warehouse_id INT,
    
    -- Cancellation Information
    ware_order_cancel_reason_id INT,
    ware_order_cancel_reason_description NVARCHAR(255),
    warehouse_ord_return_reason_id INT,
    warehouse_ord_return_reason_description NVARCHAR(255),
    
    -- Order Items
    order_items NVARCHAR(255),
    
    -- EDI Reference
    master_edi_reference NVARCHAR(255),
    
    -- Priority
    priority INT,
    
    -- Fraud Detection
    fraud_recommendation_id INT,
    fraud_recommendation_code NVARCHAR(255),
    fraud_recommendation_description NVARCHAR(255),
    
    -- Shipment Method
    shipment_method_id INT,
    shipment_method_description NVARCHAR(255),
    
    -- Stock Information
    avaliable_stock_quantity INT,
    
    -- Store
    store NVARCHAR(255),
    
    -- Company
    company_name NVARCHAR(255),
    
    -- Carrier Info
    party_carrier_info_id INT,
    business_days_in_transit INT,
    
    -- Supplier Information
    supplier_id INT,
    supplier_address_id INT,
    
    -- Customer Information
    customer_email NVARCHAR(255),
    
    -- Operation Status
    warehouse_order_operation_status NVARCHAR(255),
    
    -- FBA Order Information
    org_fba_order_id INT,
    warehouse_fba_order_status_code NVARCHAR(255),
    warehouse_fba_order_status_desc NVARCHAR(255),
    
    -- Selected Order
    selected_order NVARCHAR(255),
    
    -- Package Information
    package_code NVARCHAR(255),
    sscc NVARCHAR(255),
    shipment_type_id INT,
    insurance_type NVARCHAR(255),
    
    -- Tax and Duties
    taxes_and_duties_billing_type NVARCHAR(255),
    tax_and_duties_payor_info NVARCHAR(255),
    
    -- API Response Metadata
    success BIT,
    success_message NVARCHAR(255),
    page_size INT,
    selected_page_index INT,
    page_count INT,
    record_count INT,
    
    -- Processing Metadata
    api_fetch_timestamp DATETIME2,
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE()
);

-- Indexes for ShipmentOrder
CREATE INDEX idx_code ON dbo.ShipmentOrder(code);
CREATE INDEX idx_customer_id ON dbo.ShipmentOrder(customer_id);
CREATE INDEX idx_warehouse_id ON dbo.ShipmentOrder(warehouse_id);
CREATE INDEX idx_order_date ON dbo.ShipmentOrder(order_date);
CREATE INDEX idx_status_code ON dbo.ShipmentOrder(warehouse_order_status_code);
CREATE INDEX idx_last_modified ON dbo.ShipmentOrder(last_modified_date);

-- ============================================================================
-- ORDER LINE ITEMS TABLE
-- ============================================================================
CREATE TABLE dbo.ShipmentOrder_Line (
    id INT IDENTITY(1,1) PRIMARY KEY,
    code NVARCHAR(255) NOT NULL,
    warehouse_order_id INT NOT NULL,
    
    -- Inventory Item Information
    inventory_item_id INT,
    inventory_item_description NVARCHAR(255),
    inventory_item_info NVARCHAR(255),
    barcode NVARCHAR(255),
    display_member NVARCHAR(255),
    
    -- Pack Type Information
    inventory_item_pack_type_id INT,
    inventory_item_pack_type_description NVARCHAR(255),
    pack_quantity INT,
    
    -- Insurance
    insurance_amount_per_unit DECIMAL(18,2),
    
    -- EDI Reference
    edi_reference NVARCHAR(255),
    
    -- Physical Dimensions
    unit_weight DECIMAL(18,4),
    unit_volume DECIMAL(18,4),
    total_weight DECIMAL(18,4),
    total_volume DECIMAL(18,4),
    line_weight DECIMAL(18,4),
    
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
    free_attr1 NVARCHAR(255),
    free_attr2 NVARCHAR(255),
    free_attr3 NVARCHAR(255),
    
    -- Pricing
    currency_price DECIMAL(18,2),
    tax_rate DECIMAL(18,4),
    net_currency_price DECIMAL(18,2),
    sales_unit_price DECIMAL(18,2),
    
    -- Supplier
    supplier_id INT,
    supplier_description NVARCHAR(255),
    
    -- Notes
    notes1 NVARCHAR(255),
    notes2 NVARCHAR(255),
    notes3 NVARCHAR(255),
    
    -- Channel Order Detail
    channel_order_detail_code NVARCHAR(255),
    
    -- Lot and Batch Information
    lot_no NVARCHAR(255),
    expiry_date DATETIME2,
    production_date DATETIME2,
    
    -- Package Type
    package_type NVARCHAR(255),
    
    -- Stock Kit
    stock_kit_code NVARCHAR(255),
    
    -- Suitability and Quarantine
    suitability_reason NVARCHAR(255),
    quarantine_reason NVARCHAR(255),

    -- Logiwa status IDs
    warehouse_status_id INT,
    custom_status_id INT,
    fba_status_id INT,
    
    -- Metadata
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE(),
    
    CONSTRAINT FK_ShipmentOrderLine_ShipmentOrder 
        FOREIGN KEY (warehouse_order_id) 
        REFERENCES dbo.ShipmentOrder(id) 
        ON DELETE CASCADE
);

-- Indexes for ShipmentOrder_Line
CREATE INDEX idx_line_warehouse_order_id ON dbo.ShipmentOrder_Line(warehouse_order_id);
CREATE INDEX idx_line_inventory_item_id ON dbo.ShipmentOrder_Line(inventory_item_id);
CREATE INDEX idx_line_barcode ON dbo.ShipmentOrder_Line(barcode);
CREATE INDEX idx_line_code ON dbo.ShipmentOrder_Line(code);

-- ============================================================================
-- ADDRESS TABLE
-- ============================================================================
CREATE TABLE dbo.ShipmentOrder_Address (
    id INT IDENTITY(1,1) PRIMARY KEY,
    warehouse_order_id INT NOT NULL,
    address_type NVARCHAR(50) NOT NULL, -- 'SHIPPING', 'BILLING', 'THIRD_PARTY'
    
    -- Account Information
    account_number NVARCHAR(255),
    
    -- Address Details
    country NVARCHAR(255),
    state NVARCHAR(255),
    city NVARCHAR(255),
    customer_address NVARCHAR(255),
    address_text NVARCHAR(255),
    address_directions NVARCHAR(255),
    postal_code NVARCHAR(255),
    
    -- Metadata
    created_at DATETIME2 DEFAULT GETDATE(),
    updated_at DATETIME2 DEFAULT GETDATE(),
    
    CONSTRAINT FK_ShipmentOrderAddress_ShipmentOrder 
        FOREIGN KEY (warehouse_order_id) 
        REFERENCES dbo.ShipmentOrder(id) 
        ON DELETE CASCADE
);

-- Indexes for ShipmentOrder_Address
CREATE INDEX idx_address_warehouse_order_id ON dbo.ShipmentOrder_Address(warehouse_order_id);
CREATE INDEX idx_address_type ON dbo.ShipmentOrder_Address(address_type);

-- need some tables for this fuckass nested bullshit
CREATE TABLE dbo.ShipmentOrder_Channel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    channel_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES dbo.ShipmentOrder(id) ON DELETE CASCADE
);

CREATE TABLE dbo.ShipmentOrder_WarehouseOrderStatus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES dbo.ShipmentOrder(id) ON DELETE CASCADE
);

CREATE TABLE dbo.ShipmentOrder_WarehouseFBAOrderStatus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES dbo.ShipmentOrder(id) ON DELETE CASCADE
);

CREATE TABLE dbo.ShipmentOrder_CustomStatus (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    status_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES dbo.ShipmentOrder(id) ON DELETE CASCADE
);

CREATE TABLE dbo.ShipmentOrder_Carrier (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    carrier_id INTEGER NOT NULL,
    FOREIGN KEY (order_id) REFERENCES dbo.ShipmentOrder(id) ON DELETE CASCADE
);


-- ============================================================================
-- RUNS TABLE
-- ============================================================================
CREATE TABLE dbo.ShipmentOrder_Runs (
    id INT IDENTITY(1,1) PRIMARY KEY,
    fetch_timestamp DATETIME2 DEFAULT GETDATE(),
    success BIT
);

-- ============================================================================
-- STAGING TABLE
-- ============================================================================
CREATE TABLE dbo.ShipmentOrder_Staging (
    id INT IDENTITY(1,1) PRIMARY KEY,
    order_id INT NOT NULL,
    raw_json NVARCHAR(255) NOT NULL,
    fetch_timestamp DATETIME2 DEFAULT GETDATE(),

    CONSTRAINT FK_ShipmentOrderStaging_ShipmentOrder 
        FOREIGN KEY (order_id) 
        REFERENCES dbo.ShipmentOrder(id) 
        ON DELETE CASCADE
);

-- Create indexes for ShipmentOrder_Staging
CREATE INDEX idx_warehouse_order_id ON dbo.ShipmentOrder_Staging(order_id);
CREATE UNIQUE INDEX unique_order_custom_status ON dbo.ShipmentOrder_Staging(id, order_id);

-- ============================================================================
-- COMMENTS AND DOCUMENTATION
-- ============================================================================

-- Table Relationships:
-- 1. ShipmentOrder (1) -> (Many) ShipmentOrder_Line
-- 2. ShipmentOrder (1) -> (Many) ShipmentOrder_Address
-- 3. ShipmentOrder (1) -> (Many) ShipmentOrder_Staging
