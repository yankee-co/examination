from django.db import models
from datetime import datetime

class Client(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    birth = models.DateTimeField()
    idenity_code = models.IntegerField(unique = True)
    passport = models.CharField(max_length = 50, unique = True)
    client_type = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Account(models.Model):
    iban = models.CharField(max_length = 29, unique = True)
    client = models.ForeignKey('Client', on_delete = models.CASCADE)
    balance = models.PositiveIntegerField(default = 0)
    name = models.CharField(max_length = 50)

    def __str__(self):
        return f'{self.name} / {self.balance} ({self.client}) IBAN: {self.iban}'

class TransactionType(models.Model):
    name = models.CharField(max_length = 255)
    code = models.PositiveIntegerField(unique = True)

    def __str__(self):
        return f'{self.name} / {self.code}'

class Transaction(models.Model):
    transaction_type = models.ForeignKey('TransactionType', on_delete = models.CASCADE)
    amount = models.PositiveIntegerField()
    credit_account = models.ForeignKey('Account', on_delete = models.CASCADE, related_name = 'credit_account')
    debit_account = models.ForeignKey('Account', on_delete = models.CASCADE, related_name = 'debit_account')
    created = models.DateTimeField(default = datetime.now())
    description = models.CharField(max_length = 255)

    def __str__(self):
        return f'{self.description} {self.amount}'
