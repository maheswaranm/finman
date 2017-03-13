from django.forms import ModelForm

from finmancore.models import Account,Credit,Debit,Transfer

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = ['label','currency']

class CreditForm(ModelForm):
    class Meta:
        model = Credit
        exclude = []

class DebitForm(ModelForm):
    class Meta:
        model = Debit
        exclude = []

class TransferForm(ModelForm):
    class Meta:
        model = Transfer
        exclude = []
