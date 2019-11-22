"""Ai URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.conf import settings
from testapp import views

urlpatterns = [
    path('city/', views.city_view, name='city'),
    path('state/', views.state_view, name='state'),
    path('country/', views.country_view, name='country'),
    path('admin/', admin.site.urls),
    path('signup/', views.signup,name='signup'),
    path('customer/', views.customer_view,name='customer'),
    path('unitlocation/', views.unit_location_view,name='unitlocation'),
    path('employee/', views.employee_view,name='employee'),
    path('billing/', views.billing_view,name='billing'),
    path('delivery/', views.delivery_address_view,name='delivery'),
    path('vendor/', views.vendor_master_view,name='vendor'),
    path('machine/', views.machine_list_view,name='machine'),
    path('customercontact/', views.customer_contact,name='customercontact'),
    path('orgdesignation/', views.org_desi_master,name='orgdesignation'),
    path('empcategory/', views.emp_category_view,name='empcategory'),
    path('vendorcontact/', views.vendor_contact_view,name='vendorcontact'),
    path('meterialcategory/', views.material_category,name='meterialcategory'),
    path('meterialsubcategory/', views.material_sub_category,name='meterialsubcategory'),
    path('purchasematerial/', views.purchase_meterial_view,name='purchasematerial'),
    path('productmaster/', views.product_master_view,name='productmaster'),
    path('productartwork/', views.product_artwork_view,name='productartwork'),
    path('productrate/', views.product_rate_view,name='productrate'),
    path('productcategory/', views.product_category_view,name='productcategory'),
    path('baf/', views.baf_view,name='baf'),
    path('bafdetail/', views.baf_detail_view, name='bafdetail'),
    path('platedetail/', views.plate_detail_view,name='platedetail'),
    path('platerequest/', views.plate_request_view,name='platerequest'),
    path('platetransfer/', views.plate_transfer_view,name='platetransfer'),
    path('termcondition/', views.term_condition_view,name='termcondition'),
    path('quotation/', views.quotation_view,name='quotation'),
    path('quotationproduct/', views.quotation_product_view,name='quotationproduct'),
    path('orderbooking/', views.order_booking_view,name='orderbooking'),
    path('orderbookingdetail/', views.order_booking_detail_view,name='orderbookingdetail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home,name='home'),
    path('home1/', views.home1,name='home1'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

