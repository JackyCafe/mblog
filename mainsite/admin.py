from django.contrib import admin

# Register your models here.
from mainsite.models import Post


def upper_case_name(obj):
    return ("%s" % (obj.owner)).upper()
upper_case_name.short_description = 'Name'


def lower_case_name(obj):
    return ("%s" % (obj.owner)).lower()
lower_case_name.short_description = 'Name'

class PostDisplay(admin.ModelAdmin):
    list_display = ('title',lower_case_name,'decade_date')

admin.site.register(Post,PostDisplay)