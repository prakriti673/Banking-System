from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    branch_code = models.CharField(max_length=250)

    class Meta:
        verbose_name_plural="Branches"

    def __str__(self):
        return self.name

class Bank(models.Model):
    name = models.CharField(max_length=250)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return self.name 

class ClientManager(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str_(self):
        return self.name

class Account(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    open_date = models.CharField(max_length=250)
    account_type = models.CharField(max_length=250)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    account_no = models.CharField(max_length=16, unique=True, editable=False, validators=[
        MinLengthValidator(16),
        MaxLengthValidator(16)
    ])
    
    def clean(self):
        super().clean()
        if len(self.account_no) != 16:
            raise ValidationError("Account number must be exactly 16 characters long.")

    @property
    def balance(self):
        deposits = sum(deposit.amount for deposit in Deposit.objects.filter(account=self.id))
        withdrawals = sum(withdrawal.amount for withdrawal in Withdraw.objects.filter(account=self.id))
        return deposits - withdrawals

    
class Transfer(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)

    def __str__(self):
        return "Account Transfered to {} Branch".format(self.branch.name)

class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)


class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)









