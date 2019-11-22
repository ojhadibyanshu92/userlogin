from django.contrib import admin

# Register your models here.


from .site import DashboardSite

admin.site = DashboardSite()
admin.sites.site = admin.site
admin.autodiscover()
