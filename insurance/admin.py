from django.contrib import admin

from insurance.models import Customer
from insurance.models import InsurancePolicy

admin.site.register(Customer)
admin.site.register(InsurancePolicy)
