from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.


# class GoogleBooksAdmin(admin.ModelAdmin):
#     list_display = ('bookid', 'category')
#     search_fields = ('bookid', 'category__name')

# admin.site.register(GoogleBooks, GoogleBooksAdmin)

# class CategoryBookAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)

class Sub_CategoryAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('details',)

admin.site.register(Sub_Category, Sub_CategoryAdmin)

admin.site.register([Course, Category,Quiz,Question,Choice])
