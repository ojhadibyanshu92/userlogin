from django.db import models

class CityMaster(models.Model):
    city_code = models.AutoField(primary_key=True,)
    city_name = models.CharField(max_length=150,null=True)
    def __str__(self):
        return '%s %s' % (self.city_code, self.city_name)


class StateMaster(models.Model):
    state_code = models.AutoField(primary_key=True,)
    state_name = models.CharField(max_length=257)
    def __str__(self):
        return '%s %s' % (self.state_code, self.state_name)

class CountryMaster(models.Model):
    country_code = models.AutoField(primary_key=True,)
    country_name = models.CharField(max_length=152)
    def __str__(self):
        return '%s %s' % (self.country_code, self.country_name)

class OrganizationDesignationMasterList(models.Model):
    designation_code = models.AutoField(primary_key=True,)
    designation = models.CharField(max_length=200)
    def __str__(self):
        return '%s %s' %(self.designation_code,self.designation)

class EmployeeCategoryMaster(models.Model):
    employee_category_code = models.AutoField(primary_key=True,)
    employee_category = models.CharField(max_length=212)
    def __str__(self):
        return '%s %s' %(self.employee_category_code,self.employee_category)

class UnitLocationMaster(models.Model):
    location_code = models.AutoField(primary_key=True,)
    location_name = models.CharField(max_length=150)
    location_type= models.CharField(max_length=158)
    operation_head = models.CharField(max_length=175)
    quality_head = models.CharField(max_length=198)
    address1 = models.CharField(max_length=250)
    address2 = models.CharField(max_length=185)
    city_code = models.ForeignKey(CityMaster,on_delete=models.CASCADE)
    state_code = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    country_code= models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
    gst_number = models.CharField(max_length=150)
    location_pan= models.CharField(max_length=350)
    def __str__(self):
        return '%s %s' % (self.location_code, self.location_name)

class EmployeeMaster(models.Model):
    employee_code = models.AutoField(primary_key=True,)
    employee_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    educational_qualification = models.CharField(max_length=500)
    date_of_joining = models.DateField()
    unit_location_code = models.ForeignKey(UnitLocationMaster,on_delete=models.CASCADE)
    designation_code = models.ForeignKey(OrganizationDesignationMasterList,on_delete=models.CASCADE,default='')
    employee_category_code = models.ForeignKey(EmployeeCategoryMaster,on_delete=models.CASCADE,default='')
    def __str__(self):
        return '%s %s ' % (self.employee_code, self.employee_name)

class MachinesListMaster(models.Model):
     machine_id = models.AutoField(primary_key=True,)
     machine_code = models.CharField(max_length=150)
     machine_number = models.IntegerField()
     location_code = models.ForeignKey(UnitLocationMaster,on_delete=models.CASCADE)
     capacity = models.CharField(max_length=158)
     make = models.CharField(max_length=150)
     optimal_speed = models.CharField(max_length=150)
     mfg_date = models.DateField()
     installation_date = models.DateField()
     remark = models.TextField()
     line_no = models.IntegerField()
     plate_dimension = models.CharField(max_length=50)
     def __str__(self):
         return str(self.machine_id)

class CustomerContactMaster(models.Model):
    customer_contact_id = models.AutoField(primary_key=True)
    person_first_name = models.CharField(max_length=50)
    person_last_name = models.CharField(max_length=50)
    person_mobile_no = models.BigIntegerField()
    person_email = models.EmailField()
    person_designation = models.CharField(max_length=50)
    office_location = models.CharField(max_length=50)
    remark = models.CharField(max_length=65)
    department = models.CharField(max_length=50)
    def __str__(self):
        return '%s %s ' % (self.customer_contact_id, self.person_first_name,)

class CustomerMaster(models.Model):
    customer_id = models.AutoField(primary_key=True,)
    customer_name = models.CharField(max_length=90)
    customer_code = models.CharField(max_length=90)
    customer_address1 = models.CharField(max_length=50)
    customer_address2 = models.CharField(max_length=50)
    customer_address3 = models.CharField(max_length=50)
    customer_city = models.ForeignKey(CityMaster,on_delete=models.CASCADE)
    customer_state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    customer_country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
    customer_email = models.EmailField()
    customer_gst_number = models.CharField(max_length=60)
    customer_pan_number = models.CharField(max_length=64)
    customer_tin_number = models.CharField(max_length=50)
    customer_ecc_number = models.CharField(max_length=70)
    customer_excise_range = models.CharField(max_length=50)
    customer_excise_div = models.CharField(max_length=50)
    customer_excise_collector = models.CharField(max_length=50)
    customer_office_contact = models.CharField(max_length=70)
    CUSTOMER_TYPE = (
        ('M', 'Manufacturer'),
        ('T', 'Trader'),
        ('A','Agent'),
        ('C','Contractor'),
    )
    customer_type = models.CharField(max_length=50,choices=CUSTOMER_TYPE)
    COMPANY_STATUS =(
        ('private','Private'),
        ('public_limited','Public_limited'),
        ('partnership','Partnership')
    )
    company_status = models.CharField(max_length=120,choices=COMPANY_STATUS)
    SSI_STATUS =(
        ('micro','Micro'),
        ('small','Small'),
        ('medium','Medium'),
        ('others','Others')
    )
    ssi_status = models.CharField(max_length=50,choices=SSI_STATUS)
    # contact_person1 = models.CharField(max_length=50)
    # contact_person2 = models.CharField(max_length=50)
    # contact_person3 = models.CharField(max_length=50)
    # billing_address_id = models.IntegerField()
    # delivery_address_id = models.ForeignKey(DeliveryAddressMaster,on_delete=models.CASCADE)
    # customer_type = models.CharField(max_length=60)
    website = models.URLField()
    phone_number = models.BigIntegerField()
    def __str__(self):
        return '%s %s' % (self.customer_name, self.customer_id)

class DeliveryAddressMaster(models.Model):
    delivery_address_id = models.AutoField(primary_key=True,)
    delivery_address1 = models.CharField(max_length=85)
    delivery_address2 = models.CharField(max_length=85)
    delivery_address3 = models.CharField(max_length=85)
    city_code = models.ForeignKey(CityMaster,on_delete=models.CASCADE)
    state_code = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    country_code = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
    customer_contact_id = models.ForeignKey(CustomerContactMaster,on_delete=models.CASCADE)
    gst_number = models.CharField(max_length=85)
    pan_number = models.CharField(max_length=90)
    remark = models.CharField(max_length=550)
    customer_id = models.ForeignKey(CustomerMaster,on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.delivery_address_id, self.delivery_address1)

class VendorMaster(models.Model):
    vendor_id = models.AutoField(primary_key=True,)
    vendor_name = models.CharField(max_length=154)
    vendor_code = models.CharField(max_length=50)
    vendor_address1 = models.CharField(max_length=100)
    vendor_address2 = models.CharField(max_length=100)
    vendor_address3 = models.CharField(max_length=100)
    vendor_city = models.ForeignKey(CityMaster,on_delete=models.CASCADE)
    vendor_state = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    vendor_country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
    vendor_email = models.EmailField()
    vendor_gst_number = models.CharField(max_length=60)
    vendor_pan_number = models.CharField(max_length=70)
    vendor_office_contact = models.CharField(max_length=250)
    # contact_person1 = models.ForeignKey(ContactPersonMaster,on_delete=models.CASCADE,related_name='contact_person1')
    # contact_person2 = models.ForeignKey(ContactPersonMaster,on_delete=models.CASCADE,related_name='contact_person2')
    # contact_person3 = models.ForeignKey(ContactPersonMaster,on_delete=models.CASCADE,related_name='contact_person3')
    def __str__(self):
        return '%s %s ' % (self.vendor_id, self.vendor_name,)

class VendorContactMaster(models.Model):
    vendor_contact_id = models.IntegerField()
    person_first_name = models.CharField(max_length=50)
    person_last_name = models.CharField(max_length=50)
    person_mobile = models.BigIntegerField()
    person_email = models.EmailField()
    person_designation = models.CharField(max_length=50)
    office_location = models.CharField(max_length=50)
    remark = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    vendor_id = models.ForeignKey(VendorMaster,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.vendor_contact_id, self.person_first_name,)



class BillingAddressMaster(models.Model):
    billing_address_id = models.AutoField(primary_key=True,)
    billing_address1 = models.CharField(max_length=65)
    billing_address2 = models.CharField(max_length=65)
    billing_address3 = models.CharField(max_length=65)
    city_code = models.ForeignKey(CityMaster,on_delete=models.CASCADE)
    state_code = models.ForeignKey(StateMaster,on_delete=models.CASCADE)
    country_code = models.ForeignKey(CountryMaster,on_delete=models.CASCADE)
    customer_contact = models.ForeignKey(CustomerContactMaster,on_delete=models.CASCADE,default='')
    gst_number = models.CharField(max_length=250)
    pan_number = models.CharField(max_length=62)
    remark = models.CharField(max_length=85)
    customer_id = models.ForeignKey(CustomerMaster,on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.billing_address_id, self.billing_address1,)


class MaterialCategoryMaster(models.Model):
    material_category_id = models.AutoField(primary_key=True,)
    material_category = models.CharField(max_length=250)
    material_category_code = models.CharField(max_length=250)
    def __str__(self):
        return '%s %s ' %(self.material_category_id,self.material_category,)

class MaterialSubCategoryMaster(models.Model):
    material_sub_category_id = models.AutoField(primary_key=True)
    material_sub_category = models.CharField(max_length=250)
    material_sub_category_code = models.CharField(max_length=250)
    material_category_id = models.ForeignKey(MaterialCategoryMaster,on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' %(self.material_sub_category_id,self.material_sub_category,)

class PurchaseMaterialMaster(models.Model):
    purchase_material_id = models.AutoField(primary_key=True,)
    specification_id = models.IntegerField()
    material_code = models.CharField(max_length=500)
    material_sub_category_id = models.ForeignKey(MaterialSubCategoryMaster,on_delete=models.CASCADE)
    description = models.TextField()
    def __str__(self):
        return '%s %s' %(self.purchase_material_id,self.material_code)



class ProductMaster(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    product_code = models.CharField(max_length=10)
    product_category_id = models.CharField(max_length=50)
    customer_id = models.ForeignKey(CustomerMaster,on_delete=models.CASCADE)
    customer_specification_number = models.CharField(max_length=50)
    customer_product_code = models.CharField(max_length=50)
    product_registered_by = models.CharField(max_length=50)
    product_description = models.CharField(max_length=50)
    product_diameter = models.CharField(max_length=50)
    product_length_height = models.CharField(max_length=50)
    is_specification_supplied = models.BooleanField()
    is_sample = models.BooleanField()
    checked_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='checked_by')
    approved_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='approved_by')
    product_specification_location_directory = models.FileField()
    customer_specification_date = models.DateField()

    def __str__(self):
        return '%s %s' %(self.product_id,self.product_name)

class ProductRate(models.Model):
    product_rate_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    rate_wef_date = models.DateField()
    rate_wet_date = models.DateField()
    rate_per_thousand = models.CharField(max_length=50)
    def __str__(self):
        return '%s %s ' %(self.product_rate_id,self.product_id)

class ProductArtWork(models.Model):
    art_work_revision_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    customer_art_work_no = models.CharField(max_length=50)
    pgi_art_work_no = models.CharField(max_length=50)
    art_work_revision_no = models.CharField(max_length=50)
    wef_date = models.DateField()
    baf_no = models.CharField(max_length=50)
    wet_date = models.DateField()
    is_new = models.BooleanField()
    RECEIPT_FROM =(
        ('email','Email'),
        ('download','Download'),
        ('hardcopy','Hard_Copy'),
        ('tube','Tube'),
        ('carton','Carton'),
        ('verbal','Verbal')
    )
    art_work_receipt_from = models.CharField(max_length=50,choices=RECEIPT_FROM)
    art_work_file_format = models.CharField(max_length=50)
    art_work_received_date = models.DateField()
    art_work_location_directory = models.FileField()
    is_baf_requested = models.BooleanField()
    checked_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='art_work_checked_by')
    approved_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='art_work_pproved_by')
    prepared_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='art_work_prepared_by')
    def __str__(self):
        return '%s %s ' %(self.art_work_revision_id,self.product_id)
class ProductCategoryMaster(models.Model):
    product_category_id = models.AutoField(primary_key=True)
    product_category = models.CharField(max_length=50)

    def __str__(self):
        return self.product_category

class Baf(models.Model):
    baf_id = models.AutoField(primary_key=True)
    checked_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='baf_checked_by')
    approved_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='baf_approved_by')
    baf_number = models.CharField(max_length=50)
    final_approved_date = models.DateField()
    final_approved_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE)
    is_plate_requested = models.BooleanField()
    remark = models.CharField(max_length=40)
    colour1 = models.CharField(max_length=50)
    colour2 = models.CharField(max_length=50)
    colour3 = models.CharField(max_length=50)
    colour4 = models.CharField(max_length=50)
    colour5 = models.CharField(max_length=50)
    baf_stage = models.CharField(max_length=50)

    def __str__(self):
        return '%s  ' %(self.baf_id)

class PlateRequest(models.Model):
    plate_request_no = models.AutoField(primary_key=True)
    baf_no = models.ForeignKey(Baf,on_delete=models.CASCADE)
    baf_revision_no = models.CharField(max_length=50)
    request_type = models.CharField(max_length=40)
    vendor_id = models.ForeignKey(VendorMaster,on_delete=models.CASCADE)
    reason_for_plate = models.CharField(max_length=40)
    total_no_plate = models.CharField(max_length=50)
    po_number = models.IntegerField()
    pgi_site =models.ForeignKey(UnitLocationMaster,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.plate_request_no,self.baf_no,)

class BafDetail(models.Model):
    baf_detail_id = models.AutoField(primary_key=True)
    baf_id = models.ForeignKey(Baf,on_delete=models.CASCADE)
    baf_issue_date = models.DateField()
    baf_receive_date = models.DateField()
    customer_approval_auth_id = models.ForeignKey(CustomerMaster,on_delete=models.CASCADE)
    remark_from_ccs = models.CharField(max_length=50)
    received_baf_location_directory = models.FileField()
    baf_revision_no = models.CharField(max_length=40)

    def __str__(self):
        return '%s %s ' % (self.baf_detail_id, self.baf_id,)

class PlateDetail(models.Model):
    plate_detail_no = models.AutoField(primary_key=True)
    line_number = models.ForeignKey(MachinesListMaster,on_delete=models.CASCADE)
    plate_dimension = models.CharField(max_length=50)
    number_of_plate_request = models.CharField(max_length=10)
    plate_request_number = models.ForeignKey(PlateRequest,on_delete=models.CASCADE)
    colour1 = models.CharField(max_length=50)
    colour2 = models.CharField(max_length=50)
    colour3 = models.CharField(max_length=50)
    colour4 = models.CharField(max_length=50)
    colour5 = models.CharField(max_length=50)
    plate_id1 = models.IntegerField()
    plate_id2 = models.IntegerField()
    plate_id3 = models.IntegerField()
    plate_id4 = models.IntegerField()
    plate_id5 = models.IntegerField()
    plate_processed_date = models.DateField()
    plate_prepared_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='plate_prepared_by')
    plate_checked_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='plate_checked_by')

    def __str__(self):
        return '%s %s' % (self.plate_detail_no, self.line_number,)

class PlateTransferEntry(models.Model):
    plate_entry_id = models.AutoField(primary_key=True)
    baf_no = models.ForeignKey(Baf,on_delete=models.CASCADE)
    no_of_plate_send= models.CharField(max_length=50)
    plate_dispatched_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='plate_dispatched_by')
    plate_send_via = models.CharField(max_length=50)
    description_of_plate = models.CharField(max_length=50)
    plate_received_by = models.ForeignKey(EmployeeMaster,on_delete=models.CASCADE,related_name='plate_received_by')
    plate_received_date = models.DateField()
    def __str__(self):
        return '%s %s' % (self.plate_entry_id, self.baf_no,)


class TermsConditionMaster(models.Model):
    term_condition_id = models.AutoField(primary_key=True)
    term_and_condition = models.TextField()
    def __str__(self):
        return '%s %s' %(self.term_condition_id,self.term_and_condition)


class QuotationEntry(models.Model):
    quotation_id = models.AutoField(primary_key=True)
    quotation_reference_number = models.CharField(max_length=50)
    customer_id = models.ForeignKey(CustomerMaster,on_delete=models.CASCADE,related_name='quotations_customer_id')
    pgi_site_id = models.IntegerField()
    term_condition = models.ForeignKey(TermsConditionMaster,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.quotation_id,self.customer_id)

class QuotationProductList(models.Model):
    quotation_product_id = models.AutoField(primary_key=True)
    product_id = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    product_specification = models.CharField(max_length=50)
    product_dimension = models.CharField(max_length=50)
    product_rate = models.CharField(max_length=100)
    quotation_id = models.ForeignKey(QuotationEntry,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.quotation_product_id,self.product_id,)

class OrderBooking(models.Model):
    po_booking_number = models.AutoField(primary_key=True)
    po_received_on = models.DateField()
    po_received_mod = models.CharField(max_length=50)
    quotation_reference_number = models.ForeignKey( QuotationEntry,on_delete=models.CASCADE)
    customer_code = models.ForeignKey(CustomerMaster,on_delete=models.CASCADE)
    location_code = models.ForeignKey(UnitLocationMaster,on_delete=models.CASCADE)
    po_number = models.IntegerField()
    po_date = models.DateField()
    po_tally_booking_reference_number = models.CharField(max_length=50)
    po_tally_booking_date = models.DateField()
    delivery_address_id = models.ForeignKey(DeliveryAddressMaster,on_delete=models.CASCADE)
    billing_address_id = models.ForeignKey(BillingAddressMaster,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' %(self.po_booking_number,self.po_received_on,)


class OrderBookingDetail(models.Model):
    po_booking_detail_number = models.AutoField(primary_key=True)
    po_booking_number = models.ForeignKey(OrderBooking,on_delete=models.CASCADE)
    product_code = models.ForeignKey(ProductMaster,on_delete=models.CASCADE)
    order_quantity = models.CharField(max_length=50)
    marketing_remark = models.CharField(max_length=50)
    delivery_address_id = models.ForeignKey(DeliveryAddressMaster,on_delete=models.CASCADE)
    billing_address_id = models.ForeignKey(BillingAddressMaster,on_delete=models.CASCADE)
    development_charge = models.CharField(max_length=50)
    rate_per_thousand = models.CharField(max_length=50)
    rate_effect_from = models.DateField()

    def __str__(self):
        return '%s %s' %(self.po_booking_number,self.po_booking_detail_number,)

class DeliverySchedule(models.Model):
    po_delivery_schedule_number = models.AutoField(primary_key=True)
    order_delivery_quantity = models.IntegerField()
    requested_delivery_date = models.DateField()
    proposed_delivery_date = models.DateField()
    po_booking_detail_number = models.ForeignKey(OrderBookingDetail,on_delete=models.CASCADE,related_name='schedule_po_booking_detail_number')

    def __str__(self):
        return '%s %s ' %(self.po_delivery_schedule_number,self.order_delivery_quantity)

