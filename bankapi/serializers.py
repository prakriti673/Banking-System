from rest_framework import serializers

from .models import *

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('__all__')

class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('__all__')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')


class ClientManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientManager
        fields = ('__all__')


