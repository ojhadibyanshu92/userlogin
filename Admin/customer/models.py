from django.db import models
from django.utils import timezone
from django_countries.fields import CountryField


class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    street_1 = models.CharField(max_length=255)
    street_2 = models.CharField(max_length=255, blank=True, default='')
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=20)
    country = CountryField()
    postal_code = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} ({self.email})'

    @property
    def admin_name(self):
        *first,last=self.name.split()
        rest=' '.join(first)
        return f'{last}, {first} ({self.email})'


class Purchase(models.Model):
    customer = models.ForeignKey(Customer, related_name='purchases',on_delete=models.CASCADE)
    placed_at = models.DateTimeField('Placed',default=timezone.now) #placed is just use like verbosre name to change the column name in django admin
    shipped_at = models.DateTimeField(blank=True, null=True)
    discount_code = models.CharField('Discount',blank=True, default='', max_length=20)
    total = models.DecimalField('total_amount',max_digits=9, decimal_places=2)
    shipped = models.BooleanField(default=False)
    items = models.ManyToManyField('products.Product', through='PurchaseItem')

class PurchaseItem(models.Model):
    product = models.ForeignKey('products.Product',on_delete=models.CASCADE)
    purchase = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    purchase_placed_at=models.DateTimeField(blank=True,null=True)
    quantity = models.IntegerField(default=1)

class PurchaseSummary(PurchaseItem):
    class Meta:
        proxy=True
        verbose_name="Purchase summary"
        verbose_name_plural="purchase summaries"
