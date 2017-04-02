from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils import timezone


import logging

from .models import Account,Transaction, Category
from .forms import AccountForm, CreditForm, DebitForm, TransferForm, CategoryForm, UserNameChangeForm

# Create your views here.
@login_required(login_url='/login')
def home_view(request):
    accounts = Account.objects.all()
    transactions = Transaction.objects.all().select_subclasses().order_by('-time_of_transaction')[:20]

    oldest_transaction = Transaction.objects.all().order_by('time_of_transaction')[0:1].get()
    oldest_transaction_date = oldest_transaction.time_of_transaction

    net_worth = Transaction.objects.getNetWorthOverTime(None,None,oldest_transaction_date,timezone.now())
    label= [ str(value['date_created']) for value in net_worth ]
    data=[ str(value['balance']) for value in net_worth ]
    context = {'accounts': accounts, 'transactions':transactions,'net_worth':net_worth,'labels':label,'data':data}
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
    accounts = Account.objects.all()
    if request.method == 'POST':
        form = UserNameChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = UserNameChangeForm(instance = request.user)
    return render(request, 'change_user.html', {'accounts':accounts,'form': form})

@login_required(login_url='/login')
def change_pass(request):
    accounts = Account.objects.all()
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_user.html', {'accounts':accounts,'form': form})

@login_required(login_url='/login')
def category_manage(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    context={'accounts': accounts, 'categories':categories}
    return render(request,'categories.html',context)

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


@login_required(login_url='/login')
def account_update(request,account_id):
    accounts = Account.objects.all()
    this_account = accounts.get(pk=account_id)

    if request.method == "POST":
        form = AccountForm(request.POST, instance = this_account)
        if form.is_valid():
            print('saving')
            form.save()
            return redirect('/')
    else:
        form = AccountForm(instance=this_account)

    context={'accounts': accounts,'form':form, 'form_action':'/account/update/'+str(this_account.id)}
    return render(request,'create_update_form.html',context)

@login_required(login_url='/login')
def category_new(request):
    accounts = Account.objects.all()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            logger.info('errors')
    else:
        form = CategoryForm()
    context={'accounts': accounts,'form':form, 'form_action':'/category/new'}
    return render(request,'create_update_form.html',context)

@login_required(login_url='/login')
def category_update(request,category_id):
    accounts = Account.objects.all()
    this_category = Category.objects.get(pk=category_id)

    if request.method == "POST":
        form = CategoryForm(request.POST, instance = this_category)
        if form.is_valid():
            print('saving')
            form.save()
            return redirect('/')
    else:
        form = CategoryForm(instance=this_category)

    context={'accounts': accounts,'form':form, 'form_action':'/category/update/'+str(this_category.id)}
    return render(request,'create_update_form.html',context)
