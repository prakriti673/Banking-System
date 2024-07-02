from __future__ import unicode_literals

from django.shortcuts import render
from django.http import Http404


from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

#for testing Bank is dependent on Branch as foreign key
class BankAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Bank.objects.all()
    serializer_class=BankSerializer

class BranchAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer

class BranchDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Branch.objects.all()
    serializer_class=BranchSerializer

class CreateAccountAPIView(APIView):
    def post(self,request):
        """
        {
            "full_name": "Joshua",
            "address": "San Deigo",
            "open_date": "2021-07-14",
            "account_type": "savings",
            "bank": 2,
            "aadhar number": "1416253487659832"
        }
        """
        client = Client.objects.create(
            name=request.data['full_name'],
            address=request.data['address'],
        )
        bank = Bank.objects.get(pk=request.data['bank'])
        
        account = Account.objects.create(
            client=client,
            open_date=request.data['open_date'],
            account_type=request.data['account_type'],
            bank = bank,
            account_no=request.data['aadhar number'],
        )

        serializer = AccountSerializer(account)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

# details about a particular bank a/c
class AccountDetailsAPIView(generics.RetrieveAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer

class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class DepositAPIView(generics.ListCreateAPIView):
    """
    Create a new deposit
    {
        "account": 1,
        "amount": 200
    }
    """
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer

class WithdrawAPIView(generics.ListCreateAPIView):
    """
    Create a new withdrawal
    {
        "account": 1,
        "amount": 200
    }
    """
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
    
class TransferAPIView(generics.ListCreateAPIView):
    
    queryset = Transfer.objects.all()
    serializer_class = TransferSerializer
    