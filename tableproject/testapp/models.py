from django.db import models


# Create your models here.
class Employee_master(models.Model):
    employee_id = models.CharField(max_length=100, primary_key=True, null=False)
    employee_name = models.CharField(max_length=25, null=False)
    employee_contactno = models.BigIntegerField(default=0, null=False)
    employee_unit = models.CharField(max_length=15, null=False)
    employee_salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    employee_role = models.CharField(max_length=25, null=False)
    employee_resaddr = models.CharField(max_length=250, null=False)
    employee_joindate = models.DateField(auto_now=False, auto_now_add=False)
    employee_remarks = models.TextField(max_length=250, null=True)

    class Meta:
        ordering = ['employee_id']


class Product_master(models.Model):
    product_id = models.CharField(max_length=100, primary_key=True, null=False)
    product_name = models.CharField(max_length=250, null=False)
    product_class = models.CharField(max_length=30, null=False)
    product_specifications = models.TextField(max_length=250, null=True)
    product_cost = models.IntegerField(default=0, null=False)
    product_remarks = models.TextField(max_length=250, null=False)

    def __str__(self):
        return self.product_id

# child class of employee_master
class Unit(models.Model):
    unit_id = models.CharField(max_length=100, primary_key=True, null=False)
    unit_name = models.CharField(max_length=100, null=False, default=0)
    unit_location = models.CharField(max_length=250, null=False, default=0)
    unit_employees = models.ForeignKey(Employee_master, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.unit_id


class Stages(models.Model):
    stage_id = models.CharField(max_length=100, primary_key=True, null=False)

    def __str__(self):
        return self.stage_id

# company master is child of product master
class Company_master(models.Model):
    company_id = models.CharField(max_length=100, primary_key=True, null=False)
    company_name = models.CharField(max_length=40, null=False)
    company_location = models.CharField(max_length=250, null=False)
    company_billaddr = models.CharField(max_length=250, null=False)
    company_deladdr = models.CharField(max_length=250, null=False)
    company_website = models.URLField(max_length=200, null=True)
    company_contactno = models.BigIntegerField(default=0, null=False)
    company_email = models.EmailField(max_length=254, null=False)
    company_products = models.ForeignKey(Product_master, on_delete=models.SET_NULL, null=True)
    company_remarks = models.CharField(max_length=250, null=True)
    def __str__(self):
        return self.company_id


class Machine(models.Model):
    machine_id = models.CharField(max_length=100, primary_key=True, null=False)
    machine_name = models.TextField(max_length=40, null=False)
    machine_company = models.TextField(max_length=100, null=False)
    machine_unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    machine_handler = models.ForeignKey(Employee_master, on_delete=models.SET_NULL, null=True)
    machine_purpose = models.ForeignKey(Stages, on_delete=models.SET_NULL, null=True)
    machine_products = models.ForeignKey(Product_master, on_delete=models.SET_NULL, null=True)
    machine_status = models.TextField(max_length=100, null=False)
    machine_maintainer = models.TextField(max_length=300, null=True)
    machine_remarks = models.TextField(max_length=250, null=True)

    def __str__(self):
        return self.machine_id