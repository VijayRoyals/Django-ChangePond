from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import portfolio_detail,Comment,VlogAuthor,TagLine

admin.site.register(Comment)
admin.site.register(VlogAuthor)
admin.site.register(TagLine)


@admin.register(portfolio_detail)
class UserAdmin(admin.ModelAdmin):
    list_display = ('content', 'img_title')
