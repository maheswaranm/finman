from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.home_view),
    url(r'^home',views.home_view),
    url(r'^account/(?P<account_id>[0-9]+)',views.account_view),
    url(r'^account/manage',views.account_manage),
    url(r'^account/new',views.account_new),
    url(r'^profile/changeuser',views.change_user),
    url(r'^profile/changepass',views.change_pass),
    url(r'^categories/manage',views.category_manage),
    url(r'^transaction/all',views.transaction_all),
    url(r'^credit/new',views.credit_new),
    url(r'^debit/new',views.debit_new),
    url(r'^transfer/new',views.transfer_new),
    url(r'^transaction/update/(?P<transaction_id>[0-9]+)',views.transaction_update),
]
