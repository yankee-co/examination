from django.contrib import admin
from .models import Account, Transaction, TransactionType, Client

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    pass

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    pass

@admin.register(TransactionType)
class TransactionTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass
