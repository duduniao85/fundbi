from django.contrib import admin
from StaticReport.models import  Weeklyquote
#Register your models here.
#user admin console to edit the content of tables of database
class WeeklyQuoteAdmin(admin.ModelAdmin):
    list_display = ('secucode','closedate')
admin.site.register(Weeklyquote,WeeklyQuoteAdmin)

