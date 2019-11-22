from django.contrib import admin
from . models import *
class UnitLocationAdmin(admin.ModelAdmin):
    list_display = ('location_name','location_type','operation_head','city_code','state_code','country_code')

class EmpMasterAdmin(admin.ModelAdmin):
    list_display = ('employee_code','employee_name','unit_location_code','designation_code')

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_name','customer_id','customer_email','customer_city','customer_state','customer_country')

class ContactCustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_contact_id','person_first_name','person_last_name','person_mobile_no','person_email')

class VendorMasterAdmin(admin.ModelAdmin):
    list_display = ('vendor_id','vendor_name','vendor_code','vendor_city','vendor_state','vendor_email')

class BillingAddressMasterAdmin(admin.ModelAdmin):
    list_display = ('billing_address_id','city_code','state_code','gst_number','pan_number')

class MachineListMasterAdmin(admin.ModelAdmin):
    list_display = ('machine_id','location_code','machine_number','capacity')

class MaterialCategoryAdmin(admin.ModelAdmin):
    list_display = ('material_category_id','material_category','material_category_code')

class MaterialSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('material_sub_category_id','material_sub_category','material_sub_category_code')

class PurchaseMaterialAdmin(admin.ModelAdmin):
    list_display = ('purchase_material_id','description','material_code')

class OrgDesiMasterAdmin(admin.ModelAdmin):
    list_display = ('designation_code','designation')

class EmpCategoryMasterAdmin(admin.ModelAdmin):
    list_display = ('employee_category_code','employee_category')

class DeliveryAddressMasterAdmin(admin.ModelAdmin):
    list_display = ('delivery_address_id','delivery_address1','city_code','state_code')

class CityMasterAdmin(admin.ModelAdmin):
    list_display = ('city_code','city_name')

class StateMasterAdmin(admin.ModelAdmin):
    list_display = ('state_code','state_name')

class CountryMasterAdmin(admin.ModelAdmin):
    list_display = ('country_code','country_name')

class VendorContactAdmin(admin.ModelAdmin):
    list_display = ('vendor_contact_id','person_first_name','person_last_name','person_mobile','person_email')

class ProductMasterAdmin(admin.ModelAdmin):
    list_display = ('product_id','product_name','product_code','product_category_id','customer_id','product_diameter','product_specification_location_directory')

class ProductArtWorkAdmin(admin.ModelAdmin):
    list_display = ('art_work_revision_id','product_id','customer_art_work_no','pgi_art_work_no','wef_date','wet_date')

class BafAdmin(admin.ModelAdmin):
    list_display = ('baf_id','checked_by','approved_by','final_approved_date','is_plate_requested','baf_stage')

class BafDetailAdmin(admin.ModelAdmin):
    list_display = ('baf_detail_id', 'baf_id' ,'baf_issue_date','customer_approval_auth_id','baf_revision_no')

class ProductRateAdmin(admin.ModelAdmin):
    list_display = ('product_rate_id','product_id','rate_wef_date','rate_wet_date','rate_per_thousand')


class PlateRequestAdmin(admin.ModelAdmin):
    list_display = ('plate_request_no','baf_no','baf_revision_no','request_type','vendor_id','po_number','pgi_site')

class PlateDetailAdmin(admin.ModelAdmin):
    list_display = ('plate_detail_no','line_number','plate_dimension','number_of_plate_request','plate_processed_date')

class PlateTransferEntryAdmin(admin.ModelAdmin):
    list_display = ('plate_entry_id','baf_no','no_of_plate_send','plate_dispatched_by','plate_send_via','description_of_plate','plate_received_date')

class TermConditionMasterAdmin(admin.ModelAdmin):
    list_display = ('term_condition_id','term_and_condition')

class QuotationEntryAdmin(admin.ModelAdmin):
    list_display = ('quotation_id','quotation_reference_number','customer_id','pgi_site_id','term_condition')

class QuotationProductListAdmin(admin.ModelAdmin):
    list_display = ('quotation_product_id','product_id','product_specification','product_dimension','product_rate','quotation_id')

class OrderBookingAdmin(admin.ModelAdmin):
    list_display = ('po_booking_number','po_received_on','po_received_mod','quotation_reference_number','customer_code','location_code','delivery_address_id')

class OrderBookingDetailAdmin(admin.ModelAdmin):
    list_display = ('po_booking_detail_number','po_booking_number','product_code','order_quantity','marketing_remark','rate_per_thousand')


class DeliveryScheduleAdmin(admin.ModelAdmin):
    list_display = ('po_delivery_schedule_number','order_delivery_quantity','requested_delivery_date','proposed_delivery_date','po_booking_detail_number')





admin.site.register(CountryMaster,CountryMasterAdmin)
admin.site.register(StateMaster,StateMasterAdmin)
admin.site.register(EmployeeMaster,EmpMasterAdmin)
admin.site.register(MachinesListMaster,MachineListMasterAdmin)
admin.site.register(UnitLocationMaster,UnitLocationAdmin)
admin.site.register(CustomerMaster,CustomerAdmin)
admin.site.register(CityMaster,CityMasterAdmin)
admin.site.register(CustomerContactMaster,ContactCustomerAdmin)
admin.site.register(VendorMaster,VendorMasterAdmin)
admin.site.register(BillingAddressMaster,BillingAddressMasterAdmin)
admin.site.register(MaterialCategoryMaster,MaterialCategoryAdmin)
admin.site.register(MaterialSubCategoryMaster,MaterialSubCategoryAdmin)
admin.site.register(PurchaseMaterialMaster,PurchaseMaterialAdmin)
admin.site.register(OrganizationDesignationMasterList,OrgDesiMasterAdmin)
admin.site.register(EmployeeCategoryMaster,EmpCategoryMasterAdmin)
admin.site.register(DeliveryAddressMaster,DeliveryAddressMasterAdmin)
admin.site.register(VendorContactMaster,VendorContactAdmin)
admin.site.register(ProductMaster,ProductMasterAdmin)
admin.site.register(ProductArtWork,ProductArtWorkAdmin)
admin.site.register(Baf,BafAdmin)
admin.site.register(BafDetail,BafDetailAdmin)
admin.site.register(ProductRate,ProductRateAdmin)
admin.site.register(PlateRequest,PlateRequestAdmin)
admin.site.register(PlateDetail,PlateDetailAdmin)
admin.site.register(PlateTransferEntry,PlateTransferEntryAdmin)
admin.site.register(TermsConditionMaster,TermConditionMasterAdmin)
admin.site.register(QuotationEntry,QuotationEntryAdmin)
admin.site.register(QuotationProductList,QuotationProductListAdmin)
admin.site.register(OrderBooking,OrderBookingAdmin)
admin.site.register(OrderBookingDetail,OrderBookingDetailAdmin)
admin.site.register(DeliverySchedule,DeliveryScheduleAdmin)

