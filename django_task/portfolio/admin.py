from django.contrib import admin

# Register your models here.
from .models import portfolio_detail

@admin.register(portfolio_detail)
class UserAdmin(admin.ModelAdmin):
    list_display = ('content', 'img_title')
