from rest_framework import serializers

from .models import *

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')


class BankSerializer(serializers.ModelSerializer):
    branch=BranchSerializer()
    class Meta:
        model = Bank
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()

    class Meta:
        model = Account
        fields = ('__all__')


class AccountDetailSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    client = ClientSerializer()
    bank = BankSerializer()

    class Meta:
        model = Account
        fields = ['client','bank','balance','open_date','account_type']



class ClientManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientManager
        fields = ('__all__')


class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = ('__all__')

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = ('__all__')

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ('__all__')