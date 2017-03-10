from django.contrib import admin

# Register your models here.
from .models import Account,Credit,Debit,Transfer,Transaction,Category

admin.site.register(Account)
admin.site.register(Category)
admin.site.register(Credit)
admin.site.register(Debit)
admin.site.register(Transfer)
