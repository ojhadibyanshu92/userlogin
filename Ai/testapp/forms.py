from django import forms
from . models import *

class CityForm(forms.ModelForm):
    class Meta:
        model = CityMaster
        fields ='__all__'
class StateForm(forms.ModelForm):
    class Meta:
        model = StateMaster
        fields ='__all__'
class CountryForm(forms.ModelForm):
    class Meta:
        model = CountryMaster
        fields = '__all__'

class BillingForm(forms.ModelForm):
    class Meta:
        model =BillingAddressMaster
        fields ='__all__'

class CustomerForm(forms.ModelForm):
    class Meta:
        model =CustomerMaster
        fields='__all__'

class UnitLocationForm(forms.ModelForm):
    class Meta:
        model = UnitLocationMaster
        fields ='__all__'

class EmployeeMasterForm(forms.ModelForm):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'

class MachineListForm(forms.ModelForm):
    class Meta:
        model = MachinesListMaster
        fields = '__all__'

class DeliveryAddressForm(forms.ModelForm):
    class Meta:
        model = DeliveryAddressMaster
        fields = '__all__'

class VendorForm(forms.ModelForm):
    class Meta:
        model = VendorMaster
        fields = '__all__'

class CustomerContactForm(forms.ModelForm):
    class Meta:
        model = CustomerContactMaster
        fields = '__all__'

class OrgDesiMasterForm(forms.ModelForm):
    class Meta:
        model = OrganizationDesignationMasterList
        fields = '__all__'

class EmployeeCategoryForm(forms.ModelForm):
    class Meta:
        model = EmployeeCategoryMaster
        fields ='__all__'

class VendorContactForm(forms.ModelForm):
    class Meta:
        model = VendorContactMaster
        fields = '__all__'

class MaterialCategoryForm(forms.ModelForm):
    class Meta:
        model = MaterialCategoryMaster
        fields = '__all__'

class MaterialSubCategoryForm(forms.ModelForm):
    class Meta:
        model = MaterialSubCategoryMaster
        fields = '__all__'

class PurchaseMaterialForm(forms.ModelForm):
    class Meta:
        model = PurchaseMaterialMaster
        fields = '__all__'

class ProductMasterForm(forms.ModelForm):
    class Meta:
        model = ProductMaster
        fields = '__all__'

class ProductArtWorkForm(forms.ModelForm):
    class Meta:
        model = ProductArtWork
        fields = '__all__'

class BafForm(forms.ModelForm):
    class Meta:
        model = Baf
        fields = '__all__'

class BafDetailForm(forms.ModelForm):
    class Meta:
        model = BafDetail
        fields ='__all__'

class ProductRateForm(forms.ModelForm):
    class Meta:
        model = ProductRate
        fields = '__all__'

class ProductCategoryForm(forms.ModelForm):
    class Meta:
        model = ProductCategoryMaster
        fields = '__all__'

class PlateDetailForm(forms.ModelForm):
    class Meta:
        model = PlateDetail
        fields = '__all__'

class PlateRequestForm(forms.ModelForm):
    class Meta:
        model = PlateRequest
        fields = '__all__'

class PlateTransferForm(forms.ModelForm):
    class Meta:
        model = PlateTransferEntry
        fields = '__all__'

class TermConditionForm(forms.ModelForm):
    class Meta:
        model = TermsConditionMaster
        fields = '__all__'


class QuotationForm(forms.ModelForm):
    class Meta:
        model = QuotationEntry
        fields = '__all__'

class QuotationProductForm(forms.ModelForm):
    class Meta:
        model = QuotationProductList
        fields ='__all__'

class OrderBookingForm(forms.ModelForm):
    class Meta:
        model = OrderBooking
        fields = '__all__'

class OrderBookingDetailForm(forms.ModelForm):
    class Meta:
        model = OrderBookingDetail
        fields = '__all__'

