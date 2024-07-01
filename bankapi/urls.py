from django.contrib import admin
from django.urls import path, include

from .views import (BankAPIView, BranchAPIView, BranchDetailAPIView, 
BankDetailAPIView, CreateAccountAPIView,
 AccountListAPIView)
urlpatterns = [
    path('banks/', BankAPIView.as_view(), name='banks'),
    path('bank/<int:pk>/', BankDetailAPIView.as_view(), name='bank-detail'),
    path('branches/', BranchAPIView.as_view(), name='branches'),
    path('branch/<int:pk>/', BranchDetailAPIView.as_view(), name='branch-detail'),
    path('create_account/', CreateAccountAPIView.as_view(), name='create-account'),
    path('accounts/', AccountListAPIView.as_view(), name='account-details'),
]
