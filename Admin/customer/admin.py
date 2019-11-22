from django.contrib import admin
from django.db.models import Count,Sum
from . import forms

from django.utils import timezone
from . models import *

class PurchasreItemInLine(admin.TabularInline):
    model = PurchaseItem

class BigOrderFilter(admin.SimpleListFilter):#custom filter True not working
    title = 'big order'
    parameter_name = 'big_order'

    def lookups(self, request, model_admin):
        return (
            ('1','True'),
            ('0','False'),
        )
    def queryset(self, request, queryset):
        if self.value() =='1':
            return queryset.annotate(Count('items')).filter(items_count_gte=2)
        return queryset

class CustomerAdmin(admin.ModelAdmin):
    form = forms.CustomerForm
    list_display = ['admin_name','name']
    save_as = True
    save_on_top = True  # to take save button at top of admin site
    search_fields=['name']


def ship(modeladmin,request,queryset):
    queryset.update(
        shipped=True,
        shipped_at=timezone.now()
    )
ship.short_description='Mark Purchases as shipped now'


class PurchaseAdmin(admin.ModelAdmin):
    actions = [ship]
    date_hierarchy = 'placed_at' #to filter item date ,month and year wise
    inlines = [PurchasreItemInLine]
    list_display = ['customer','placed_at','shipped_at','shipped','total']
    list_editable = ['shipped']
    list_filter = ['shipped','placed_at','shipped_at',BigOrderFilter]
    ordering = ['placed_at']
    search_fields = ['customer__name','items__name']

    fieldsets = (
        (None,{
            'fields':(
                ('customer','total','shipped'),
                'discount_code'
            )
        }),
        ('Dates',{
            'classes':('collapse',),
            'fields':('placed_at','shipped_at')
        })
    )

#
# class PurchesSumerryAdmin(admin.ModelAdmin):
#     date_hierarchy = 'placed_at'
# admin.site.register(PurchaseSummary,PurchesSumerryAdmin)
@admin.register(PurchaseSummary)
class PurchasesSummaryAdmin(admin.ModelAdmin):
    date_hierarchy = 'purchase_placed_at'
    def changelist_view(self,request,extra_context=None):
        response = super().changelist_view(request,extra_context)
        try:
            qs=response.context_data['cl'].queryset
        except(AttributeError,KeyError):
            return response
        metrics={
            'total': Sum('quantity'),
            'total_sales':Sum('product__price'),
        }
        response.context_data['summary']=list(
            qs.values('product__name').annotate(**metrics).order_by('-quantity')
        )
        response.context_data['summary_total']=dict(
            qs.aggregate(**metrics)
        )
        return response

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Purchase,PurchaseAdmin)
admin.site.register(PurchaseItem)
