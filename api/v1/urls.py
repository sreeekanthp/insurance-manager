from django.urls import path

from api.v1.views import CustomerAPIView
from api.v1.views import InsurancePolicyAPIView


urlpatterns = [
    path('create_customer/', CustomerAPIView.as_view(), name='create-customer'),
    path('create_policy/', InsurancePolicyAPIView.as_view(), name='create-policy'),
]
