from django.contrib import admin
from . models import *
from image_cropping import ImageCroppingMixin

class ImageInLine(ImageCroppingMixin,admin.StackedInline):
    model = Image

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = (
        ('name','slug'),
        'description',
        ('price','quantity'),
        'featured',
        ('serial_number','location'),
        'categories'
    )
    radio_fields = {'featured':admin.HORIZONTAL}
    inlines = [ImageInLine]
    prepopulated_fields = {'slug':('name',)}
    filter_horizontal = ['categories']

# @admin.register(Image)#try to crop the image but dont success
# class ImageAdmin(ImageCroppingMixin,admin.ModelAdmin):
#     pass



admin.site.register(Image)# Image cropping is not working
class ImageAdmin(ImageCroppingMixin,admin.ModelAdmin):
    pass

admin.site.register(Category)
