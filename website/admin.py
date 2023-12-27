from django.contrib import admin
from .models import *
# Register your models here.


# class GoogleBooksAdmin(admin.ModelAdmin):
#     list_display = ('bookid', 'category')
#     search_fields = ('bookid', 'category__name')

# admin.site.register(GoogleBooks, GoogleBooksAdmin)

# class CategoryBookAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

admin.site.register([Course, Category, Sub_Category,Quiz,Question,Choice])
