"""
Parser module to convert API JSON response to normalized data structures
"""

import json
from typing import Dict, List, Any, Optional
from datetime import datetime
from decimal import Decimal
from .datastructs import (
    ShipmentOrder,
    ShipmentOrderLine,
    ShipmentOrderAddress,
    ShipmentOrderStatusMapping,
    ShipmentOrderCarrierMapping,
    ShipmentOrderChannelMapping,
    ShipmentOrderCustomStatusMapping,
    ShipmentOrderFBAStatusMapping,
    ShipmentOrderError,
)

from logging import error


class WarehouseOrderParser:
    """Parse warehouse order API responses into normalized data structures"""

    @staticmethod
    def parse_datetime(date_str: Optional[str]) -> Optional[datetime]:
        """Parse date strings from API - handles multiple formats"""
        if not date_str or date_str in ["", "null", None]:
            return None

        # Try different date formats
        formats = [
            "%m.%d.%Y %I:%M:%S",  # 03.17.2022 12:32:59
            "%m/%d/%Y %I:%M:%S %p",  # 5/17/2023 1:28:36 AM
            "%Y-%m-%dT%H:%M:%S",  # ISO format
            "%Y-%m-%d %H:%M:%S",  # Standard SQL format
        ]

        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except (ValueError, TypeError):
                continue

        return None

    @staticmethod
    def parse_decimal(value: Any) -> Optional[Decimal]:
        """Safely parse decimal values"""
        if value is None or value == "" or value == "null":
            return None
        try:
            return Decimal(str(value))
        except Exception as e:
            error(e)
            return None

    @staticmethod
    def parse_int(value: Any) -> Optional[int]:
        """Safely parse integer values"""
        if value is None or value == "" or value == "null":
            return None
        try:
            return int(value)
        except Exception as e:
            error(e)
            return None

    @staticmethod
    def parse_bool(value: Any) -> Optional[bool]:
        """Safely parse boolean values"""
        if value is None or value == "" or value == "null":
            return None
        if isinstance(value, bool):
            return value
        return bool(value)

    @staticmethod
    def parse_str(value: Any) -> Optional[str]:
        """Safely parse string values"""
        if value is None or value == "" or value == "null":
            return None
        return str(value)

    def parse_order(self, data: Dict[str, Any]) -> ShipmentOrder:
        """Parse main order data"""
        return ShipmentOrder(
            id=data["ID"],
            code=data["Code"],
            priority_id=self.parse_str(data.get("PriorityID")),
            customer_ref_code=self.parse_str(data.get("CustomerRefCode")),
            depositor_ref_code=self.parse_str(data.get("DepositorRefCode")),
            customer_order_no=self.parse_str(data.get("CustomerOrderNo")),
            depositor_order_no=self.parse_str(data.get("DepositorOrderNo")),
            warehouse_order_status_code=self.parse_str(
                data.get("WarehouseOrderStatusCode")
            ),
            customer_id=self.parse_int(data.get("CustomerID")),
            customer_code=self.parse_str(data.get("CustomerCode")),
            customer_description=self.parse_str(data.get("CustomerDescription")),
            inventory_site_id=self.parse_int(data.get("InventorySiteID")),
            inventory_site_code=self.parse_str(data.get("InventorySiteCode")),
            warehouse_id=self.parse_int(data.get("WarehouseID")),
            warehouse_code=self.parse_str(data.get("WarehouseCode")),
            warehouse_description=self.parse_str(data.get("WarehouseDescription")),
            depositor_id=self.parse_int(data.get("DepositorID")),
            depositor_code=self.parse_str(data.get("DepositorCode")),
            depositor_description=self.parse_str(data.get("DepositorDescription")),
            is_print_carrier_label_pack_list_as_label=self.parse_bool(
                data.get("IsPrintCarrierLabelPackListAsLabel")
            ),
            is_print_carrier_label_pack_list_on_same_page=self.parse_bool(
                data.get("IsPrintCarrierLabelPackListOnSamePage")
            ),
            carrier_tracking_number=self.parse_str(data.get("CarrierTrackingNumber")),
            warehouse_order_type_id=self.parse_int(data.get("WarehouseOrderTypeID")),
            warehouse_order_type_code=self.parse_str(
                data.get("WarehouseOrderTypeCode")
            ),
            is_amazon_fba=self.parse_bool(data.get("IsAmazonFBA")),
            order_date=self.parse_datetime(data.get("OrderDate")),
            planned_delivery_date=self.parse_datetime(data.get("PlannedDeliveryDate")),
            planned_ship_date=self.parse_datetime(data.get("PlannedShipDate")),
            notes=self.parse_str(data.get("Notes")),
            is_document_exist=self.parse_str(data.get("IsDocumentExist")),
            purchase_order_id=self.parse_int(data.get("PurchaseOrderID")),
            purchase_order_code=self.parse_str(data.get("PurchaseOrderCode")),
            is_imported=self.parse_bool(data.get("IsImported")),
            is_exported=self.parse_bool(data.get("IsExported")),
            is_exported4=self.parse_bool(data.get("IsExported4")),
            is_exported5=self.parse_bool(data.get("IsExported5")),
            is_backorder=self.parse_bool(data.get("IsBackorder")),
            nof_shipment_label=self.parse_int(data.get("NofShipmentLabel")),
            is_allocated=self.parse_bool(data.get("IsAllocated")),
            is_picking_started=self.parse_bool(data.get("IsPickingStarted")),
            is_picking_completed=self.parse_bool(data.get("IsPickingCompleted")),
            invoice_customer_id=self.parse_int(data.get("InvoiceCustomerID")),
            invoice_customer_party_id=self.parse_int(
                data.get("InvoiceCustomerPartyID")
            ),
            invoice_customer_description=self.parse_str(
                data.get("InvoiceCustomerDescription")
            ),
            invoice_customer_address_id=self.parse_int(
                data.get("InvoiceCustomerAddressID")
            ),
            invoice_customer_address_description=self.parse_str(
                data.get("InvoiceCustomerAddressDescription")
            ),
            total_sales_gross_price=self.parse_decimal(
                data.get("TotalSalesGrossPrice")
            ),
            total_sales_vat=self.parse_decimal(data.get("TotalSalesVat")),
            total_sales_discount=self.parse_decimal(data.get("TotalSalesDiscount")),
            instructions=self.parse_str(data.get("Instructions")),
            account_number=self.parse_str(data.get("AccountNumber")),
            driver=self.parse_str(data.get("Driver")),
            platenumber=self.parse_str(data.get("Platenumber")),
            billing_type_id=self.parse_int(data.get("BillingTypeID")),
            billing_type_description=self.parse_str(data.get("BillingTypeDescription")),
            route_id=self.parse_int(data.get("RouteID")),
            route_description=self.parse_str(data.get("RouteDescription")),
            channel_description=self.parse_str(data.get("ChannelDescription")),
            is_cancel_requested=self.parse_bool(data.get("IsCancelRequested")),
            carrier_description=self.parse_str(data.get("CarrierDescription")),
            integration_key=self.parse_str(data.get("IntegrationKey")),
            entered_by=self.parse_str(data.get("EnteredBy")),
            canceled_by=self.parse_str(data.get("CanceledBy")),
            carrier_shipping_options_id=self.parse_int(
                data.get("CarrierShippingOptionsID")
            ),
            carrier_depositor_list_id=self.parse_int(
                data.get("CarrierDepositorListID")
            ),
            nof_products=self.parse_int(data.get("NofProducts")),
            store_name=self.parse_str(data.get("StoreName")),
            linked_channel_id=self.parse_int(data.get("LinkedChannelID")),
            linked_channel_description=self.parse_str(
                data.get("LinkedChannelDescription")
            ),
            carrier_rate=self.parse_decimal(data.get("CarrierRate")),
            carrier_markup_rate=self.parse_decimal(data.get("CarrierMarkupRate")),
            carrier_package_type_id=self.parse_int(data.get("CarrierPackageTypeID")),
            customer_address_id=self.parse_int(data.get("CustomerAddressID")),
            customer_address_description=self.parse_str(
                data.get("CustomerAddressDescription")
            ),
            planned_pick_date=self.parse_datetime(data.get("PlannedPickDate")),
            actual_pick_date=self.parse_datetime(data.get("ActualPickDate")),
            actual_delivery_date=self.parse_datetime(data.get("ActualDeliveryDate")),
            project_id=self.parse_int(data.get("ProjectID")),
            project_description=self.parse_str(data.get("ProjectDescription")),
            warehouse_receipt_id=self.parse_int(data.get("WarehouseReceiptID")),
            warehouse_receipt_code=self.parse_str(data.get("WarehouseReceiptCode")),
            back_warehouse_order_code=self.parse_str(
                data.get("BackWarehouseOrderCode")
            ),
            drop_ship_master_order_id=self.parse_int(data.get("DropShipMasterOrderID")),
            drop_ship_warehouse_order_code=self.parse_str(
                data.get("DropShipWarehouseOrderCode")
            ),
            drop_ship_notes=self.parse_str(data.get("DropShipNotes")),
            is_waybill_printed=self.parse_bool(data.get("IsWaybillPrinted")),
            invoice_no=self.parse_str(data.get("InvoiceNo")),
            delivery_note_no=self.parse_str(data.get("DeliveryNoteNo")),
            is_carrier_label_printed=self.parse_bool(data.get("IsCarrierLabelPrinted")),
            channel_order_code=self.parse_str(data.get("ChannelOrderCode")),
            carrier_weight=self.parse_str(data.get("CarrierWeight")),
            client_party_id=self.parse_int(data.get("ClientPartyID")),
            po_window_warehouse_id=self.parse_int(data.get("POWindowWarehouseID")),
            ware_order_cancel_reason_id=self.parse_int(
                data.get("WareOrderCancelReasonID")
            ),
            ware_order_cancel_reason_description=self.parse_str(
                data.get("WareOrderCancelReasonDescription")
            ),
            is_gift=self.parse_bool(data.get("IsGift")),
            gift_note=self.parse_str(data.get("GiftNote")),
            order_items=self.parse_str(data.get("OrderItems")),
            extra_notes=self.parse_str(data.get("ExtraNotes")),
            extra_notes1=self.parse_str(data.get("ExtraNotes1")),
            extra_notes2=self.parse_str(data.get("ExtraNotes2")),
            extra_notes3=self.parse_str(data.get("ExtraNotes3")),
            extra_notes4=self.parse_str(data.get("ExtraNotes4")),
            extra_notes5=self.parse_str(data.get("ExtraNotes5")),
            master_edi_reference=self.parse_str(data.get("MasterEDIReference")),
            priority=self.parse_int(data.get("Priority")),
            fraud_recommendation_id=self.parse_int(data.get("FraudRecommendationID")),
            fraud_recommendation_code=self.parse_str(
                data.get("FraudRecommendationCode")
            ),
            fraud_recommendation_description=self.parse_str(
                data.get("FraudRecommendationDescription")
            ),
            order_risk_score=self.parse_decimal(data.get("OrderRiskScore")),
            is_exported2=self.parse_bool(data.get("IsExported2")),
            shipment_method_id=self.parse_int(data.get("ShipmentMethodID")),
            shipment_method_description=self.parse_str(
                data.get("ShipmentMethodDescription")
            ),
            is_address_verified=self.parse_bool(data.get("IsAddressVerified")),
            avaliable_stock_quantity=self.parse_int(data.get("AvaliableStockQuantity")),
            store=self.parse_str(data.get("Store")),
            channel_depositor_parameter_id=self.parse_int(
                data.get("ChannelDepositorParameterID")
            ),
            carrier_billing_type_id=self.parse_int(data.get("CarrierBillingTypeID")),
            carrier_billing_type_description=self.parse_str(
                data.get("CarrierBillingTypeDescription")
            ),
            is_pick_list_printed=self.parse_bool(data.get("IsPickListPrinted")),
            is_prime_order=self.parse_bool(data.get("IsPrimeOrder")),
            invoice_date=self.parse_datetime(data.get("InvoiceDate")),
            entry_date_time=self.parse_datetime(data.get("EntryDateTime")),
            cargo_discount=self.parse_decimal(data.get("CargoDiscount")),
            warehouse_ord_return_reason_id=self.parse_int(
                data.get("WarehouseOrdReturnReasonId")
            ),
            warehouse_ord_return_reason_description=self.parse_str(
                data.get("WarehouseOrdReturnReasonDescription")
            ),
            company_name=self.parse_str(data.get("CompanyName")),
            total_markup_rate=self.parse_decimal(data.get("TotalMarkupRate")),
            total_carrier_rate=self.parse_decimal(data.get("TotalCarrierRate")),
            actual_ship_date=self.parse_datetime(data.get("ActualShipDate")),
            planned_pickup_date=self.parse_datetime(data.get("PlannedPickupDate")),
            carrier_shipping_description=self.parse_str(
                data.get("CarrierShippingDescription")
            ),
            is_get_order_details=self.parse_bool(data.get("IsGetOrderDetails")),
            last_modified_date=self.parse_datetime(data.get("LastModifiedDate")),
            cancellation_date=self.parse_datetime(data.get("CancellationDate")),
            master_warehouse_order_code=self.parse_str(
                data.get("MasterWarehouseOrderCode")
            ),
            party_carrier_info_id=self.parse_int(data.get("PartyCarrierInfoID")),
            business_days_in_transit=self.parse_int(data.get("BusinessDaysInTransit")),
            supplier_id=self.parse_int(data.get("SupplierID")),
            supplier_address_id=self.parse_int(data.get("SupplierAddressID")),
            receipt_order_code=self.parse_str(data.get("ReceiptOrderCode")),
            receipt_date=self.parse_datetime(data.get("ReceiptDate")),
            warehouse_receipt_type_id=self.parse_int(
                data.get("WarehouseReceiptTypeID")
            ),
            is_auto_generate=self.parse_bool(data.get("isAutoGenerate")),
            is_use_same_lot_number=self.parse_bool(data.get("isUseSameLotNumber")),
            is_allow_changing_tax_and_duties_payor=self.parse_bool(
                data.get("IsAllowChangingTaxAndDutiesPayor")
            ),
            is_get_customer_address_info=self.parse_bool(
                data.get("IsGetCustomerAddressInfo")
            ),
            customer_email=self.parse_str(data.get("CustomerEmail")),
            warehouse_drop_ship_order_code=self.parse_str(
                data.get("WarehouseDropShipOrderCode")
            ),
            warehouse_back_order_code=self.parse_str(
                data.get("WarehouseBackOrderCode")
            ),
            warehouse_master_order_code=self.parse_str(
                data.get("WarehouseMasterOrderCode")
            ),
            warehouse_receipt_order_code=self.parse_str(
                data.get("WarehouseReceiptOrderCode")
            ),
            warehouse_order_operation_status=self.parse_str(
                data.get("WarehouseOrderOperationStatus")
            ),
            org_fba_order_id=self.parse_int(data.get("OrgFBAOrderId")),
            warehouse_fba_order_status_code=self.parse_str(
                data.get("WarehouseFBAOrderStatusCode")
            ),
            warehouse_fba_order_status_desc=self.parse_str(
                data.get("WarehouseFBAOrderStatusDesc")
            ),
            selected_order=self.parse_str(data.get("selectedOrder")),
            package_code=self.parse_str(data.get("PackageCode")),
            sscc=self.parse_str(data.get("SSCC")),
            shipment_type_id=self.parse_int(data.get("ShipmentTypeID")),
            insurance_cost=self.parse_decimal(data.get("InsuranceCost")),
            insurance_type=self.parse_str(data.get("InsuranceType")),
            is_use_saturday_delivery=self.parse_bool(data.get("IsUseSaturdayDelivery")),
            is_skip_adress_verification_stamps=self.parse_bool(
                data.get("IsSkipAdressVerificationStamps")
            ),
            is_fedex_one_rate=self.parse_bool(data.get("IsFedexOneRate")),
            taxes_and_duties_billing_type=self.parse_str(
                data.get("TaxesandDutiesBillingType")
            ),
            tax_and_duties_payor_info=self.parse_str(data.get("TaxandDutiesPayorInfo")),
            back_warehouse_order_id=self.parse_int(data.get("BackWarehouseOrderID")),
            earliest_ship_date=self.parse_datetime(data.get("EarliestShipDate")),
            latest_ship_date=self.parse_datetime(data.get("LatestShipDate")),
            earliest_delivery_date=self.parse_datetime(
                data.get("EarliestDeliveryDate")
            ),
            latest_delivery_date=self.parse_datetime(data.get("LatestDeliveryDate")),
            success=self.parse_bool(data.get("Success")),
            success_message=self.parse_str(data.get("SuccessMessage")),
            page_size=self.parse_int(data.get("PageSize")),
            selected_page_index=self.parse_int(data.get("SelectedPageIndex")),
            page_count=self.parse_int(data.get("PageCount")),
            record_count=self.parse_int(data.get("RecordCount")),
            api_fetch_timestamp=datetime.now(),
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

    def parse_order_lines(self, data: Dict[str, Any]) -> List[ShipmentOrderLine]:
        """Parse order line items from DetailInfo array"""
        lines = []
        warehouse_order_id = data["ID"]

        details = data.get("DetailInfo", [])
        if not details:
            return []

        for detail in data.get("DetailInfo", []):
            line = ShipmentOrderLine(
                id=detail["ID"],
                code=detail["Code"],
                warehouse_order_id=warehouse_order_id,
                inventory_item_id=self.parse_int(detail.get("InventoryItemID")),
                inventory_item_description=self.parse_str(
                    detail.get("InventoryItemDescription")
                ),
                inventory_item_info=self.parse_str(detail.get("InventoryItemInfo")),
                barcode=self.parse_str(detail.get("Barcode")),
                display_member=self.parse_str(detail.get("DisplayMember")),
                inventory_item_pack_type_id=self.parse_int(
                    detail.get("InventoryItemPackTypeID")
                ),
                inventory_item_pack_type_description=self.parse_str(
                    detail.get("InventoryItemPackTypeDescription")
                ),
                pack_quantity=self.parse_int(detail.get("PackQuantity")),
                insurance_amount_per_unit=self.parse_decimal(
                    detail.get("InsuranceAmountPerUnit")
                ),
                edi_reference=self.parse_str(detail.get("EDIReference")),
                unit_weight=self.parse_decimal(detail.get("UnitWeight")),
                unit_volume=self.parse_decimal(detail.get("UnitVolume")),
                allocated_cu_quantity=self.parse_int(detail.get("AllocatedCuQuantity")),
                picked_cu_quantity=self.parse_int(detail.get("PickedCuQuantity")),
                loaded_cu_quantity=self.parse_int(detail.get("LoadedCuQuantity")),
                shipped_cu_quantity=self.parse_int(detail.get("ShippedCuQuantity")),
                planned_pack_quantity=self.parse_int(detail.get("PlannedPackQuantity")),
                planned_cu_quantity=self.parse_int(detail.get("PlannedCuQuantity")),
                sorted_cu_quantity=self.parse_int(detail.get("SortedCUQuantity")),
                packed_cu_quantity=self.parse_int(detail.get("PackedCUQuantity")),
                cancelled_cu_quantity=self.parse_int(detail.get("CancelledCuQuantity")),
                free_attr1=self.parse_str(detail.get("FreeAttr1")),
                free_attr2=self.parse_str(detail.get("FreeAttr2")),
                free_attr3=self.parse_str(detail.get("FreeAttr3")),
                currency_price=self.parse_decimal(detail.get("CurrencyPrice")),
                tax_rate=self.parse_decimal(detail.get("TaxRate")),
                net_currency_price=self.parse_decimal(detail.get("NetCurrencyPrice")),
                total_weight=self.parse_decimal(detail.get("TotalWeight")),
                total_volume=self.parse_decimal(detail.get("TotalVolume")),
                line_weight=self.parse_decimal(detail.get("LineWeight")),
                supplier_id=self.parse_int(detail.get("SupplierID")),
                supplier_description=self.parse_str(detail.get("SupplierDescription")),
                notes1=self.parse_str(detail.get("Notes1")),
                notes2=self.parse_str(detail.get("Notes2")),
                notes3=self.parse_str(detail.get("Notes3")),
                sales_unit_price=self.parse_decimal(detail.get("SalesUnitPrice")),
                channel_order_detail_code=self.parse_str(
                    detail.get("ChannelOrderDetailCode")
                ),
                lot_no=self.parse_str(detail.get("LotNo")),
                expiry_date=self.parse_datetime(detail.get("ExpiryDate")),
                production_date=self.parse_datetime(detail.get("ProductionDate")),
                package_type=self.parse_str(detail.get("PackageType")),
                stock_kit_code=self.parse_str(detail.get("StockKitCode")),
                suitability_reason=self.parse_str(detail.get("SuitabilityReason")),
                quarantine_reason=self.parse_str(detail.get("QuarantineReason")),
                created_at=datetime.now(),
                updated_at=datetime.now(),
            )
            lines.append(line)

        return lines

    def parse_addresses(self, data: Dict[str, Any]) -> List[ShipmentOrderAddress]:
        """Parse address information from ThirdPartyAccount"""
        addresses = []
        warehouse_order_id = data["ID"]

        # Parse ThirdPartyAccount address
        third_party = data.get("ThirdPartyAccount", {})
        if third_party and isinstance(third_party, dict):
            address_data = third_party.get("Address", {})
            if address_data:
                address = ShipmentOrderAddress(
                    id=0,  # Will be auto-generated
                    warehouse_order_id=warehouse_order_id,
                    address_type="THIRD_PARTY",
                    account_number=self.parse_str(third_party.get("AccountNumber")),
                    country=self.parse_str(address_data.get("Country")),
                    state=self.parse_str(address_data.get("State")),
                    city=self.parse_str(address_data.get("City")),
                    customer_address=self.parse_str(
                        address_data.get("CustomerAddress")
                    ),
                    address_text=self.parse_str(address_data.get("AddressText")),
                    address_directions=self.parse_str(
                        address_data.get("AddressDirections")
                    ),
                    postal_code=self.parse_str(address_data.get("PostalCode")),
                    created_at=datetime.now(),
                    updated_at=datetime.now(),
                )
                addresses.append(address)

        return addresses

    def parse_status_mappings(
        self, data: Dict[str, Any]
    ) -> List[ShipmentOrderStatusMapping]:
        """Parse WarehouseOrderStatusID array"""
        mappings = []
        warehouse_order_id = data["ID"]

        for status_id in data.get("WarehouseOrderStatusID", []):
            if status_id:
                mapping = ShipmentOrderStatusMapping(
                    id=0,  # Will be auto-generated
                    warehouse_order_id=warehouse_order_id,
                    status_id=status_id,
                    created_at=datetime.now(),
                )
                mappings.append(mapping)

        return mappings

    def parse_carrier_mappings(
        self, data: Dict[str, Any]
    ) -> List[ShipmentOrderCarrierMapping]:
        """Parse CarrierID array"""
        mappings = []
        warehouse_order_id = data["ID"]

        for carrier_id in data.get("CarrierID", []):
            if carrier_id:
                mapping = ShipmentOrderCarrierMapping(
                    id=0,  # Will be auto-generated
                    warehouse_order_id=warehouse_order_id,
                    carrier_id=carrier_id,
                    created_at=datetime.now(),
                )
                mappings.append(mapping)

        return mappings

    def parse_channel_mappings(
        self, data: Dict[str, Any]
    ) -> List[ShipmentOrderChannelMapping]:
        """Parse ChannelID array"""
        mappings = []
        warehouse_order_id = data["ID"]

        for channel_id in data.get("ChannelID", []):
            if channel_id:
                mapping = ShipmentOrderChannelMapping(
                    id=0,  # Will be auto-generated
                    warehouse_order_id=warehouse_order_id,
                    channel_id=channel_id,
                    created_at=datetime.now(),
                )
                mappings.append(mapping)

        return mappings

    def parse_custom_status_mappings(
        self, data: Dict[str, Any]
    ) -> List[ShipmentOrderCustomStatusMapping]:
        """Parse OrderCustomStatusID array"""
        mappings = []
        warehouse_order_id = data["ID"]

        for custom_status_id in data.get("OrderCustomStatusID", []):
            if custom_status_id:
                mapping = ShipmentOrderCustomStatusMapping(
                    id=0,  # Will be auto-generated
                    warehouse_order_id=warehouse_order_id,
                    custom_status_id=custom_status_id,
                    created_at=datetime.now(),
                )
                mappings.append(mapping)

        return mappings

    def parse_fba_status_mappings(
        self, data: Dict[str, Any]
    ) -> List[ShipmentOrderFBAStatusMapping]:
        """Parse WarehouseFBAOrderStatusID array"""
        mappings = []
        warehouse_order_id = data["ID"]

        for fba_status_id in data.get("WarehouseFBAOrderStatusID", []):
            if fba_status_id:
                mapping = ShipmentOrderFBAStatusMapping(
                    id=0,  # Will be auto-generated
                    warehouse_order_id=warehouse_order_id,
                    fba_status_id=fba_status_id,
                    created_at=datetime.now(),
                )
                mappings.append(mapping)

        return mappings

    def parse_errors(self, data: Dict[str, Any]) -> List[ShipmentOrderError]:
        """Parse Errors array"""
        errors = []
        warehouse_order_id = data["ID"]

        for order_error in data.get("Errors", []):
            if order_error:
                error_obj = ShipmentOrderError(
                    id=0,  # Will be auto-generated
                    warehouse_order_id=warehouse_order_id,
                    error_message=str(order_error)
                    if isinstance(order_error, str)
                    else str(order_error.get("message", order_error)),
                    error_code=order_error.get("code")
                    if isinstance(order_error, dict)
                    else None,
                    error_field=order_error.get("field")
                    if isinstance(order_error, dict)
                    else None,
                    created_at=datetime.now(),
                )
                errors.append(error_obj)

        return errors

    def parse_response(self, json_data: str) -> Dict[str, Any]:
        """
        Parse complete API response and return all normalized data structures

        Returns:
            Dictionary containing:
            - order: ShipmentOrder
            - lines: List[ShipmentOrderLine]
            - addresses: List[ShipmentOrderAddress]
            - status_mappings: List[ShipmentOrderStatusMapping]
            - carrier_mappings: List[ShipmentOrderCarrierMapping]
            - channel_mappings: List[ShipmentOrderChannelMapping]
            - custom_status_mappings: List[ShipmentOrderCustomStatusMapping]
            - fba_status_mappings: List[ShipmentOrderFBAStatusMapping]
            - errors: List[ShipmentOrderError]
        """
        data = json.loads(json_data) if isinstance(json_data, str) else json_data

        return {
            "order": self.parse_order(data),
            "lines": self.parse_order_lines(data),
            "addresses": self.parse_addresses(data),
            "status_mappings": self.parse_status_mappings(data),
            "carrier_mappings": self.parse_carrier_mappings(data),
            "channel_mappings": self.parse_channel_mappings(data),
            "custom_status_mappings": self.parse_custom_status_mappings(data),
            "fba_status_mappings": self.parse_fba_status_mappings(data),
            "errors": self.parse_errors(data),
        }
