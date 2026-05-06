from django.contrib import admin
from .models import *

admin.site.register(BankStatement)
admin.site.register(InternalLedger)
admin.site.register(Reconciliation)
admin.site.register(NormalizedLedger)