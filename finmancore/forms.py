from django.forms import ModelForm
from django.contrib.auth.models import User

from finmancore.models import Account,Credit,Debit,Transfer,Category

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

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        exclude = []

class UserNameChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['username']
