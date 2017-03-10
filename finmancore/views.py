from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from .models import Account

# Create your views here.
@login_required(login_url='/login')
def home_view(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request,'home.html',context)

@login_required(login_url='/login')
def account_view(request,account_id):
    return HttpResponse('account page for '+account_id)

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
