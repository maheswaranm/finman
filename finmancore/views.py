from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import logging

from .models import Account,Transaction
from .forms import AccountForm, CreditForm, DebitForm, TransferForm

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
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request,'manage_accounts.html',context)

@login_required(login_url='/login')
def account_new(request):
    accounts = Account.objects.all()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = AccountForm()
    context={'accounts': accounts,'form':form,'form_action':'/account/new'}
    return render(request,'create_update_form.html',context)

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
    logger = logging.getLogger('test')

    accounts = Account.objects.all()
    if request.method == "POST":
        form = CreditForm(request.POST)
        if form.is_valid():
            logger.info('saving')
            form.save()
            return redirect('/')
        else:
            logger.info('errors')
    else:
        form = CreditForm()
    context={'accounts': accounts,'form':form, 'form_action':'/credit/new'}
    return render(request,'create_update_form.html',context)

@login_required(login_url='/login')
def debit_new(request):
    logger = logging.getLogger('test')

    accounts = Account.objects.all()
    if request.method == "POST":
        form = DebitForm(request.POST)
        if form.is_valid():
            logger.info('saving')
            form.save()
            return redirect('/')
        else:
            logger.info('errors')
    else:
        form = DebitForm()
    context={'accounts': accounts,'form':form, 'form_action':'/debit/new'}
    return render(request,'create_update_form.html',context)

@login_required(login_url='/login')
def transfer_new(request):
    logger = logging.getLogger('test')

    accounts = Account.objects.all()
    if request.method == "POST":
        form = TransferForm(request.POST)
        if form.is_valid():
            logger.info('saving')
            form.save()
            return redirect('/')
        else:
            logger.info('errors')
    else:
        form = TransferForm()
    context={'accounts': accounts,'form':form, 'form_action':'/transfer/new'}
    return render(request,'create_update_form.html',context)

@login_required(login_url='/login')
def transaction_update(request,transaction_id):
    accounts = Account.objects.all()
    this_transaction = Transaction.objects.select_subclasses().get(pk=transaction_id)

    print(this_transaction)

    if request.method == "POST":
        if this_transaction.type_of_transaction == 'Credit':
            form = CreditForm(request.POST,instance=this_transaction);
        if this_transaction.type_of_transaction == 'Debit':
            form = DebitForm(request.POST,instance=this_transaction);
        if this_transaction.type_of_transaction == 'Transfer':
            form = TransferForm(request.POST,instance=this_transaction);
        if form.is_valid():
            print('saving')
            form.save()
            return redirect('/')
    else:
        if this_transaction.type_of_transaction == 'Credit':
            form = CreditForm(instance=this_transaction);
        if this_transaction.type_of_transaction == 'Debit':
            form = DebitForm(instance=this_transaction);
        if this_transaction.type_of_transaction == 'Transfer':
            form = TransferForm(instance=this_transaction);

    context={'accounts': accounts,'form':form, 'form_action':'/transaction/update/'+str(this_transaction.id)}
    return render(request,'create_update_form.html',context)
