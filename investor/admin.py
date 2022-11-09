from django.contrib import admin

# Register your models here.
from .models import Risk, Interest, InvestmentSize, Period, Investor


class RiskAdmin(admin.ModelAdmin):
    list_display = ['Risk', 'is_verified']


admin.site.register(Risk, RiskAdmin)
admin.site.register(Investor)
admin.site.register(Interest)
admin.site.register(InvestmentSize)
admin.site.register(Period)
