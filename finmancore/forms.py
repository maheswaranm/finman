import floppyforms.__future__ as forms
from django.contrib.auth.models import User

from finmancore.models import Account,Credit,Debit,Transfer,Category


class DatePicker(forms.DateTimeInput):
    template_name = 'datepicker.html'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['label','currency']

class CreditForm(forms.ModelForm):
    class Meta:
        model = Credit
        exclude = []
        widgets = {
            'time_of_transaction':DatePicker
        }

class DebitForm(forms.ModelForm):
    class Meta:
        model = Debit
        exclude = []
        widgets = {
            'time_of_transaction':DatePicker
        }

class TransferForm(forms.ModelForm):
    class Meta:
        model = Transfer
        exclude = []
        widgets = {
            'time_of_transaction':DatePicker
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = []

class UserNameChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
