from django.http import HttpResponse
from django.views.generic import TemplateView
from django.shortcuts import render

from .models import Transaction

class HomePageView(TemplateView):
    def get(self, *args, **kwargs):

        data = []
        dicted = {}
        number = 0

        transactions = Transaction.objects.all()

        for transaction in transactions:

            print(transaction.amount)

            number += 1
            sender = transaction.credit_account.client.first_name + ' ' + transaction.credit_account.client.last_name
            getter = transaction.debit_account.client.first_name + ' ' + transaction.debit_account.client.last_name
            date = str(transaction.created.date()) + ' ' + str(transaction.created.time())

            dicted = {
            'number' : number,
            'type' : transaction.transaction_type.name,
            'date' : date,
            'amount' : transaction.amount / 100,
            'sender' : sender,
            'getter' : getter,
            }

            data.append(dicted)
            print(dicted)
        return render(
            request = self.request,
            template_name = 'home_page.html',
            context={
            'data' : data,
            }
            )
