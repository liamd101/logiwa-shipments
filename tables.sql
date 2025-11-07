-- SQL Table Definitions for Warehouse Order System
-- Normalized schema to avoid arrays in columns
-- Microsoft SQL Server 2019 (Version 15) Compatible Version

-- ============================================================================
-- MAIN ORDER TABLE
-- ============================================================================
CREATE TABLE dbo.ShipmentOrder (
    id INT IDENTITY(1,1) PRIMARY KEY,
    code NVARCHAR(MAX) NOT NULL,
    priority_id NVARCHAR(MAX),
    customer_ref_code NVARCHAR(MAX),
    depositor_ref_code NVARCHAR(MAX),
    customer_order_no NVARCHAR(MAX),
    depositor_order_no NVARCHAR(MAX),
    warehouse_order_status_code NVARCHAR(MAX),
    
    -- Customer Information
    customer_id INT,
    customer_code NVARCHAR(MAX),
    customer_description NVARCHAR(MAX),
    
    -- Site and Warehouse Information
    inventory_site_id INT,
    inventory_site_code NVARCHAR(MAX),
    warehouse_id INT,
    warehouse_code NVARCHAR(MAX),
    warehouse_description NVARCHAR(MAX),
    
    -- Depositor Information
    depositor_id INT,
    depositor_code NVARCHAR(MAX),
    depositor_description NVARCHAR(MAX),
    
    -- Printing Preferences
    is_print_carrier_label_pack_list_as_label BIT,
    is_print_carrier_label_pack_list_on_same_page BIT,
    
    -- Carrier Information
    carrier_tracking_number NVARCHAR(MAX),
    carrier_description NVARCHAR(MAX),
    carrier_shipping_options_id INT,
    carrier_depositor_list_id INT,
    carrier_rate DECIMAL(18,2),
    carrier_markup_rate DECIMAL(18,2),
    carrier_package_type_id INT,
    carrier_weight NVARCHAR(MAX),
    carrier_billing_type_id INT,
    carrier_billing_type_description NVARCHAR(MAX),
    carrier_shipping_description NVARCHAR(MAX),
    
    -- Order Type
    warehouse_order_type_id INT,
    warehouse_order_type_code NVARCHAR(MAX),
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
    notes NVARCHAR(MAX),
    instructions NVARCHAR(MAX),
    gift_note NVARCHAR(MAX),
    extra_notes NVARCHAR(MAX),
    extra_notes1 NVARCHAR(MAX),
    extra_notes2 NVARCHAR(MAX),
    extra_notes3 NVARCHAR(MAX),
    extra_notes4 NVARCHAR(MAX),
    extra_notes5 NVARCHAR(MAX),
    
    -- Document Flags
    is_document_exist NVARCHAR(MAX),
    is_waybill_printed BIT,
    is_carrier_label_printed BIT,
    is_pick_list_printed BIT,
    
    -- Purchase Order
    purchase_order_id INT,
    purchase_order_code NVARCHAR(MAX),
    
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
    invoice_customer_description NVARCHAR(MAX),
    invoice_customer_address_id INT,
    invoice_customer_address_description NVARCHAR(MAX),
    invoice_no NVARCHAR(MAX),
    delivery_note_no NVARCHAR(MAX),
    
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
    account_number NVARCHAR(MAX),
    driver NVARCHAR(MAX),
    platenumber NVARCHAR(MAX),
    billing_type_id INT,
    billing_type_description NVARCHAR(MAX),
    route_id INT,
    route_description NVARCHAR(MAX),
    channel_description NVARCHAR(MAX),
    integration_key NVARCHAR(MAX),
    entered_by NVARCHAR(MAX),
    canceled_by NVARCHAR(MAX),
    nof_shipment_label INT,
    nof_products INT,
    store_name NVARCHAR(MAX),
    linked_channel_id INT,
    linked_channel_description NVARCHAR(MAX),
    
    -- Address References
    customer_address_id INT,
    customer_address_description NVARCHAR(MAX),
    
    -- Project Information
    project_id INT,
    project_description NVARCHAR(MAX),
    
    -- Receipt Information
    warehouse_receipt_id INT,
    warehouse_receipt_code NVARCHAR(MAX),
    warehouse_receipt_type_id INT,
    receipt_order_code NVARCHAR(MAX),
    
    -- Related Orders
    back_warehouse_order_code NVARCHAR(MAX),
    back_warehouse_order_id INT,
    drop_ship_master_order_id INT,
    drop_ship_warehouse_order_code NVARCHAR(MAX),
    drop_ship_notes NVARCHAR(MAX),
    master_warehouse_order_code NVARCHAR(MAX),
    warehouse_drop_ship_order_code NVARCHAR(MAX),
    warehouse_back_order_code NVARCHAR(MAX),
    warehouse_master_order_code NVARCHAR(MAX),
    warehouse_receipt_order_code NVARCHAR(MAX),
    
    -- Channel Information
    channel_order_code NVARCHAR(MAX),
    client_party_id INT,
    channel_depositor_parameter_id INT,
    
    -- Warehouse Information
    po_window_warehouse_id INT,
    
    -- Cancellation Information
    ware_order_cancel_reason_id INT,
    ware_order_cancel_reason_description NVARCHAR(MAX),
    warehouse_ord_return_reason_id INT,
    warehouse_ord_return_reason_description NVARCHAR(MAX),
    
    -- Order Items
    order_items NVARCHAR(MAX),
    
    -- EDI Reference
    master_edi_reference NVARCHAR(MAX),
    
    -- Priority
    priority INT,
    
    -- Fraud Detection
    fraud_recommendation_id INT,
    fraud_recommendation_code NVARCHAR(MAX),
    fraud_recommendation_description NVARCHAR(MAX),
    
    -- Shipment Method
    shipment_method_id INT,
    shipment_method_description NVARCHAR(MAX),
    
    -- Stock Information
    avaliable_stock_quantity INT,
    
    -- Store
    store NVARCHAR(MAX),
    
    -- Company
    company_name NVARCHAR(MAX),
    
    -- Carrier Info
    party_carrier_info_id INT,
    business_days_in_transit INT,
    
    -- Supplier Information
    supplier_id INT,
    supplier_address_id INT,
    
    -- Customer Information
    customer_email NVARCHAR(MAX),
    
    -- Operation Status
    warehouse_order_operation_status NVARCHAR(MAX),
    
    -- FBA Order Information
    org_fba_order_id INT,
    warehouse_fba_order_status_code NVARCHAR(MAX),
    warehouse_fba_order_status_desc NVARCHAR(MAX),
    
    -- Selected Order
    selected_order NVARCHAR(MAX),
    
    -- Package Information
    package_code NVARCHAR(MAX),
    sscc NVARCHAR(MAX),
    shipment_type_id INT,
    insurance_type NVARCHAR(MAX),
    
    -- Tax and Duties
    taxes_and_duties_billing_type NVARCHAR(MAX),
    tax_and_duties_payor_info NVARCHAR(MAX),
    
    -- API Response Metadata
    success BIT,
    success_message NVARCHAR(MAX),
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
    code NVARCHAR(MAX) NOT NULL,
    warehouse_order_id INT NOT NULL,
    
    -- Inventory Item Information
    inventory_item_id INT,
    inventory_item_description NVARCHAR(MAX),
    inventory_item_info NVARCHAR(MAX),
    barcode NVARCHAR(MAX),
    display_member NVARCHAR(MAX),
    
    -- Pack Type Information
    inventory_item_pack_type_id INT,
    inventory_item_pack_type_description NVARCHAR(MAX),
    pack_quantity INT,
    
    -- Insurance
    insurance_amount_per_unit DECIMAL(18,2),
    
    -- EDI Reference
    edi_reference NVARCHAR(MAX),
    
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
    free_attr1 NVARCHAR(MAX),
    free_attr2 NVARCHAR(MAX),
    free_attr3 NVARCHAR(MAX),
    
    -- Pricing
    currency_price DECIMAL(18,2),
    tax_rate DECIMAL(18,4),
    net_currency_price DECIMAL(18,2),
    sales_unit_price DECIMAL(18,2),
    
    -- Supplier
    supplier_id INT,
    supplier_description NVARCHAR(MAX),
    
    -- Notes
    notes1 NVARCHAR(MAX),
    notes2 NVARCHAR(MAX),
    notes3 NVARCHAR(MAX),
    
    -- Channel Order Detail
    channel_order_detail_code NVARCHAR(MAX),
    
    -- Lot and Batch Information
    lot_no NVARCHAR(MAX),
    expiry_date DATETIME2,
    production_date DATETIME2,
    
    -- Package Type
    package_type NVARCHAR(MAX),
    
    -- Stock Kit
    stock_kit_code NVARCHAR(MAX),
    
    -- Suitability and Quarantine
    suitability_reason NVARCHAR(MAX),
    quarantine_reason NVARCHAR(MAX),

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
    account_number NVARCHAR(MAX),
    
    -- Address Details
    country NVARCHAR(MAX),
    state NVARCHAR(MAX),
    city NVARCHAR(MAX),
    customer_address NVARCHAR(MAX),
    address_text NVARCHAR(MAX),
    address_directions NVARCHAR(MAX),
    postal_code NVARCHAR(MAX),
    
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
    raw_json NVARCHAR(MAX) NOT NULL,
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
