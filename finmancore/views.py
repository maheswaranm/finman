from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Account

# Create your views here.
@login_required(login_url='/login')
def home_view(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request,'home.html',context)
