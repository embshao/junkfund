from django.contrib import admin
from apply.models import Candidate

# Register your models here.
admin.site.register(Candidate)
admin.site.site_header = 'JunkFund Administration'