from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Account,Transaction

# Create your views here.
@login_required(login_url='/login')
def home_view(request):
    accounts = Account.objects.all()
    transactions = Transaction.objects.all().select_subclasses().order_by('-time_of_transaction')[:20]
    context = {'accounts': accounts, 'transactions':transactions}
    return render(request,'home.html',context)

@login_required(login_url='/login')
def account_view(request,account_id):
    accounts = Account.objects.all()
    transactions = Account.objects.getTransactionsForAccount(account_id)
    this_account = Account.objects.get(pk=account_id)
    context = {'accounts': accounts, 'transactions':transactions,'this_account':this_account}
    return render(request,'accounts.html',context)

@login_required(login_url='/login')
def account_manage(request):
    return HttpResponse('account manage page')

@login_required(login_url='/login')
def account_new(request):
    return HttpResponse('new account page')

@login_required(login_url='/login')
def change_user(request):
    return HttpResponse('change user view')

@login_required(login_url='/login')
def change_pass(request):
    return HttpResponse('change pass view')

@login_required(login_url='/login')
def category_manage(request):
    return HttpResponse('category manage page')

@login_required(login_url='/login')
def transaction_new(request):
    return HttpResponse('new transaction page')

@login_required(login_url='/login')
def transaction_all(request):
    accounts = Account.objects.all()
    transactions = Transaction.objects.all().select_subclasses().order_by('-time_of_transaction')
    context = {'accounts': accounts, 'transactions':transactions}
    return render(request,'transactions.html',context)

@login_required(login_url='/login')
def credit_new(request):
    return HttpResponse('new credit page')

@login_required(login_url='/login')
def debit_new(request):
    return HttpResponse('new debit page')

@login_required(login_url='/login')
def transfer_new(request):
    return HttpResponse('new transfer page')
