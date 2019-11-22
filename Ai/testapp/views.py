from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from .models import *
from  .forms import *
from django.http.response import HttpResponse

def home(request):
    count = User.objects.count()
    return render(request,'home.html',{'count':count})
def signup(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

def home1(request):
    if request.user.is_superuser:
        return redirect('/admin')
    elif (request.user.has_perm('testapp.delete_statemaster') and request.user.has_perm('testapp.delete_statemaster')
              and request.user.has_perm('testapp.add_statemaster') and request.user.has_perm('testapp.change_statemaster')):
        return redirect('/state')
    else:
        return render(request, 'registration/login.html')

def city_view(request):
    if request.method=='POST':
        cform=CityForm(request.POST)
        if cform.is_valid():
            cform.save()
            cform = CityForm()
            return render(request, 'city.html', {'cform': cform})
        else:
            return HttpResponse('user invalid data')
    else:
        cform=CityForm()
        return render(request,'city.html',{'cform':cform})

def state_view(request):
    if request.method=='POST':
        sform=StateForm(request.POST)
        if sform.is_valid():
            sform.save()
            sform = StateForm()
            return render(request, 'state.html', {'sform': sform})
        else:
            return HttpResponse('user invalid data')
    else:
        sform=StateForm()
        return render(request,'state.html',{'sform':sform})

def country_view(request):
    if request.method=='POST':
        countryform = CountryForm(request.POST)
        if countryform.is_valid():
            countryform.save()
            countryform = CountryForm()
            return render(request,'country.html',{'countryform':countryform})
        else:
            return HttpResponse('User Invalid Data')
    else:
        countryform = CountryForm()
        return  render(request,'country.html',{'countryform':countryform})




def billing_view(request):
    if request.method=='POST':
        bform=BillingForm(request.POST)
        if bform.is_valid():
            bform.save()
            bform=BillingForm()
            return render(request,'billing.html',{'bform':bform})
        else:
            return HttpResponse('Billing invalid data')
    else:
        bform=BillingForm()
        return render(request,'billing.html',{'bform':bform})

def customer_view(request):
    if request.method=='POST':
        custform=CustomerForm(request.POST)
        if custform.is_valid():
            custform.save()
            custform=CustomerForm()
            return render(request,'customer.html',{'custform':custform})
        else:
            return HttpResponse('Customer Invalid data')
    else:
        custform=CustomerForm()
        return render(request,'customer.html',{'custform':custform})

def unit_location_view(request):
    if request.method=='POST':
        ulf = UnitLocationForm(request.POST)
        if ulf.is_valid():
            ulf.save()
            ulf=UnitLocationForm()
            return render(request,'unitlocation.html',{'uil':ulf})
        else:
            return HttpResponse('Please Fill All The Fields')
    else:
        ulf = UnitLocationForm()
        return render(request,'unitlocation.html',{'ulf':ulf})

def employee_view(request):
    if request.method=='POST':
        empform = EmployeeMasterForm(request.POST)
        if empform.is_valid():
            empform.save()
            empform = EmployeeMasterForm()
            return render(request,'employeeform.html',{'empform':empform})
        else:
            return HttpResponse('Employee Form Is Invalid')
    else:
        empform = EmployeeMasterForm()
        return render(request,'employeeform.html',{'empform':empform})

def machine_list_view(request):
    if request.method=='POST':
        machineform = MachineListForm(request.POST)
        if machineform.is_valid():
            machineform.save()
            machineform = MachineListForm()
            return render(request,'machinelistform.html',{'machineform':machineform})
        else:
            return HttpResponse('Invalid Machine List Form')
    else:
        machineform = MachineListForm()
        return render(request,'machinelistform.html',{'machineform':machineform})

def delivery_address_view(request):
    if request.method=='POST':
        deliveryform = DeliveryAddressForm(request.POST)
        if deliveryform.is_valid():
            deliveryform.save()
            deliveryform = DeliveryAddressForm()
            return render(request,'deliveryaddressform.html',{'deliveryform':deliveryform})
        else:
            return HttpResponse('Invalid Delivery Address')
    else:
        deliveryform = DeliveryAddressForm()
        return render(request,'deliveryaddressform.html',{'deliveryform':deliveryform})

def vendor_master_view(request):
    if request.method =='POST':
        vendorform = VendorForm(request.POST)
        if vendorform.is_valid():
            vendorform.save()
            vendorform = VendorForm()
            return render(request,'vendor.html',{'vendorform':vendorform})
        else:
            return HttpResponse('Invalid Data Entry')
    else:
        vendorform = VendorForm()
        return render(request,'vendor.html',{'vendorform':vendorform})


def customer_contact(request):
    if request.method=='POST':
        ccform = CustomerContactForm(request.POST)
        if ccform.is_valid():
            ccform.save()
            ccform = CustomerContactForm()
            return  render(request,'customercontact.html',{'ccform':ccform})
        else:
            return HttpResponse('Please Fill All The Fields')
    else:
        ccform = CustomerContactForm()
        return render(request,'customercontact.html',{'ccform':ccform})

def org_desi_master(request):
    if request.method=='POST':
        desigform = OrgDesiMasterForm(request.POST)
        if desigform.is_valid():
            desigform.save()
            desigform = OrgDesiMasterForm()
            return render(request,'orgdesiform.html',{'desiform':desigform})
        else:
            return  HttpResponse('Please Fill All The Fields')
    else:
        desiform = OrgDesiMasterForm()
        return render(request,'orgdesiform.html',{'desiform':desiform})

def emp_category_view(request):
    if request.method=='POST':
        empcatform = EmployeeCategoryForm(request.POST)
        if empcatform.is_valid():
            empcatform.save()
            empcatform = EmployeeCategoryForm()
            return render(request,'employeecategory.html',{'empcatform':empcatform})
        else:
            return  HttpResponse('Please Fill All The Fields')
    else:
        empcatform = EmployeeCategoryForm()
        return render(request,'employeecategory.html',{'empcatform':empcatform})

def vendor_contact_view(request):
    if request.method=='POST':
        venform = VendorContactForm(request.POST)
        if venform.is_valid():
            venform.save()
            venform = VendorContactForm()
            return render(request,'vendorcontact.html',{'venform':venform})
        else:
            return HttpResponse('Invalid Vendor Contact Detail')
    else:
        venform = VendorContactForm()
        return render(request, 'vendorcontact.html', {'venform': venform})

def material_category(request):
    if request.method=='POST':
        matcatform = MaterialCategoryForm(request.POST)
        if matcatform.is_valid():
            matcatform.save()
            matcatform = MaterialCategoryForm()
            return render(request,'materialcategory.html',{'matcatform':matcatform})
        else:
            return HttpResponse('Invalid Data')
    else:
        matcatform = MaterialCategoryForm()
        return render(request,'materialcategory.html',{'matcatform':matcatform})

def material_sub_category(request):
    if request.method=='POST':
        matscatform = MaterialSubCategoryForm(request.POST)
        if matscatform.is_valid():
            matscatform.save()
            matscatform = MaterialSubCategoryForm()
            return render(request,'materialsubcategory.html',{'matscatform':matscatform})
        else:
            return HttpResponse('Invalid Data')
    else:
        matscatform = MaterialSubCategoryForm()
        return render(request,'materialsubcategory.html',{'matscatform':matscatform})

def purchase_meterial_view(request):
    if request.method=='POST':
        pmform = PurchaseMaterialForm(request.POST)
        if pmform.is_valid():
            pmform.save()
            pmform = PurchaseMaterialForm()
            return render(request,'purchasematerial.html',{'pmform':pmform})
        else:
            return HttpResponse('Invalid data')
    else:
        pmform = PurchaseMaterialForm()
        return render(request, 'purchasematerial.html', {'pmform':pmform})

def product_master_view(request):
    if request.method =='POST':
        promasterform = ProductMasterForm(request.POST)
        if promasterform.is_valid():
            promasterform.save()
            promasterform = ProductMasterForm()
            return render(request,'productmaster.html',{'promasterform':promasterform})
        else:
            return HttpResponse('Invalid data')
    else:
        promasterform = ProductMasterForm()
        return render(request,'productmaster.html',{'promasterform':promasterform})

def product_artwork_view(request):
    if request.method=='POST':
        productart = ProductArtWorkForm(request.POST)
        if productart.is_valid():
            productart.save()
            productart = ProductArtWorkForm()
            return render(request,'productartwork.html',{'productart':productart})
        else:
            return HttpResponse('Invalid Entry Of Data')
    else:
        productart = ProductArtWorkForm()
        return render(request,'productartwork.html',{'productart':productart})

def baf_view(request):
    if request.method == 'POST':
        baf = BafForm(request.POST)
        if baf.is_valid():
            baf.save()
            baf = BafForm()
            return render(request,'baf.html',{'baf':baf})
        else:
            return HttpResponse('Invalid Baf Detail')
    else:
        baf = BafForm()
        return render(request,'baf.html',{'baf':baf})

def baf_detail_view(request):
    if request.method == 'POST':
        bafdetail = BafDetailForm(request.POST)
        if bafdetail.is_valid():
            bafdetail.save()
            bafdetail = BafDetailForm()
            return render(request,'bafdetail.html',{'bafdetail':bafdetail})
        else:
            return HttpResponse('Invalid Baf Detail')
    else:
        bafdetail = BafDetailForm()
        return render(request,'bafdetail.html',{'bafdetail':bafdetail})

def product_rate_view(request):
    if request.method=='POST':
        prate = ProductRateForm(request.POST)
        if prate.is_valid():
            prate.save()
            prate = ProductRateForm()
            return render(request,'productrate.html',{'prate':prate})
        else:
            return HttpResponse('Invalid Product Rate detail')
    else:
        prate = ProductRateForm()
        return render(request,'productrate.html',{'prate':prate})

def product_category_view(request):
    if request.method == 'POST':
        pcm = ProductCategoryForm(request.POST)
        if pcm.is_valid():
            pcm.save()
            pcm = ProductCategoryForm()
            return render(request,'productcategory.html',{'pcm':pcm})
        else:
            return HttpResponse('Invalid Product Category ')
    else:
        pcm = ProductCategoryForm()
        return render(request,'productcategory.html',{'pcm':pcm})

def plate_detail_view(request):
    if request.method == 'POST':
        pdv = PlateDetailForm(request.POST)
        if pdv.is_valid():
            pdv.save()
            pdv = PlateDetailForm()
            return render(request,'platedetail.html',{'pdv':pdv})
        else:
            return HttpResponse('Invalid Data')
    else:
        pdv = PlateDetailForm()
        return render(request,'platedetail.html',{'pdv':pdv})

def plate_request_view(request):
    if request.method =='POST':
        prv = PlateRequestForm(request.POST)
        if prv.is_valid():
            prv.save()
            prv = PlateRequestForm()
            return render(request,'platerequest.html',{'prv':prv})
        else:
            return HttpResponse('Plate Request Data Is Invalid')
    else:
        prv = PlateRequestForm()
        return render(request,'platerequest.html',{'prv':prv})

def plate_transfer_view(request):
    if request.method == 'POST':
        ptv = PlateTransferForm(request.POST)
        if ptv.is_valid():
            ptv.save()
            ptv = PlateTransferForm()
            return render(request,'platetrasfer.html',{'ptv':ptv})
        else:
            return HttpResponse('Invalid Plate Transfer Entry')
    else:
        ptv = PlateTransferForm()
        return render(request,'platetrasfer.html',{'ptv':ptv})

def term_condition_view(request):
    if request.method == 'POST':
        tcv = TermConditionForm(request.POST)
        if tcv.is_valid():
            tcv.save()
            tcv = TermConditionForm()
            return render(request,'termcondition.html',{'tcv':tcv})
        else:
            return render(request,'termcondition.html',{'tcv':tcv})
    else:
        tcv = TermConditionForm()
        return render(request, 'termcondition.html', {'tcv': tcv})

def quotation_view(request):
    if request.method =='POST':
        qv = QuotationForm(request.POST)
        if qv.is_valid():
            qv.save()
            qv = QuotationForm()
            return render(request,'quotation.html',{'qv':qv})
        else:
            return HttpResponse('Invalid Quotation Form')
    else:
        qv = QuotationForm()
        return render(request, 'quotation.html', {'qv': qv})

def quotation_product_view(request):
    if request.method == 'POST':
        qpv = QuotationProductForm(request.POST)
        if qpv.is_valid():
            qpv.save()
            qpv = QuotationProductForm()
            return render(request,'quotaionproduct.html',{'qpv':qpv})
        else:
            return HttpResponse('Invalid Quotation Data')
    else:
        qpv = QuotationProductForm()
        return render(request, 'quotaionproduct.html', {'qpv': qpv})

def order_booking_view(request):
    if request.method == 'POST':
        obv = OrderBookingForm(request.POST)
        if obv.is_valid():
            obv.save()
            obv = OrderBookingForm()
            return render(request,'orderbooking.html',{'obv':obv})
        else:
            return HttpResponse('Invalid Data Entry')
    else:
        obv = OrderBookingForm()
        return render(request, 'orderbooking.html', {'obv': obv})

def order_booking_detail_view(request):
    if request.method == 'POST':
        obdv = OrderBookingForm(request.POST)
        if obdv.is_valid():
            obdv.save()
            obdv = OrderBookingDetailForm()
            return render(request,'orderbookingdetail.html',{'obdv':obdv})
        else:
            return HttpResponse('Invalid Data Entry')
    else:
        obdv = OrderBookingDetailForm()
        return render(request, 'orderbookingdetail.html', {'obdv': obdv})