from django.db import models

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
    
    def balance(self):
        deposits=sum(deposit.amount for deposit in Deposit.objects.filter(account=self.id))
        withdrawals=sum(withdrawal.amount for withdrawal in Withdraw.objects.filter(account=self.id))
        total=deposits-withdrawals
        return total

    def __str__(self):
        return self.open_date


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









