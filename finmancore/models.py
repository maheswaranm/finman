from django.db import models
from model_utils.managers import InheritanceManager

# Create your models here.
class Account(models.Model):
    label = models.CharField(max_length=100)
    currency = models.CharField(max_length=3)
    balance = models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return "<Account : "+self.label+">"

class Category(models.Model):
    label = models.CharField(max_length=50)
    parent = models.ForeignKey("self",related_name="parent_category",default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return "<Category : "+self.label+">"

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    time_of_transaction = models.DateTimeField()
    category = models.ForeignKey(Category,default=None, blank=True, null=True)
    is_reconciled = models.BooleanField(default=False)
    currency = models.CharField(max_length=3,default=None, blank=True, null=True)

    #This is so I can find type when displaying on template
    @property
    def type_of_transaction(self):
        return self.__class__.__name__

    objects = InheritanceManager()

class Transfer(Transaction):
    from_account = models.ForeignKey(Account,related_name='from_account')
    to_account = models.ForeignKey(Account,related_name='to_account')

    def __str__(self):
        return "<Transfer :"+str(self.id)+" from "+str(self.from_account)+" to "+str(self.to_account)+">"

class Credit(Transaction):
    from_account = models.CharField(max_length=500)
    to_account = models.ForeignKey(Account,related_name='credited_account')

    def __str__(self):
        return "<Credit "+str(self.id)+" from "+str(self.from_account)+" to "+str(self.to_account)+">"

class Debit(Transaction):
    from_account = models.ForeignKey(Account,related_name='debited_account')
    to_account =  models.CharField(max_length=500)

    def __str__(self):
        return "<Debit "+str(self.id)+" from "+str(self.from_account)+" to "+str(self.to_account)+">"
