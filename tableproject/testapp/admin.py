from django.contrib import admin
from .models import *
from material.admin.options import MaterialModelAdmin
# from django.contrib.auth.models import Group
# admin.site.site_header='AI Square Global Solution'

# class InLineEmployeeMaster(admin.StackedInline):
#     model = Employee_master
class Employee_masterAdmin(admin.ModelAdmin):
    # inlines = [InLineEmployeeMaster]
    list_display = ('employee_id','employee_name','combine_employee_joindate_and_employee_salary','employee_contactno','employee_unit','employee_salary','employee_role')
    list_filter = ('employee_unit','employee_salary')
    list_display_links = ('employee_id','combine_employee_joindate_and_employee_salary')
    list_editable = ('employee_name',)
    search_fields = ('employee_id','employee_name',)
    def combine_employee_joindate_and_employee_salary(self,obj):
        return "{} - {}".format(obj.employee_joindate,obj.employee_salary)

# class UnitAdmin(admin.ModelAdmin):
#     list_display = ('unit_id',)



admin.site.register(Employee_master,Employee_masterAdmin)
admin.site.register(Product_master)
admin.site.register(Company_master)
admin.site.register(Unit)
admin.site.register(Stages)
admin.site.register(Machine)
# admin.site.unregister(Group)


