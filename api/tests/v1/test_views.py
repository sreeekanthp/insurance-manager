import copy
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate

from api.v1.views import CustomerAPIView
from api.v1.views import InsurancePolicyAPIView
from insurance.models import Customer
from insurance.models import InsurancePolicy
from insurance.tests.factories import CustomerFactory
from insurance.tests.factories import UserFactory


class CustomerAPIViewTestCase(TestCase):
    """Tests for CustomerAPIView"""

    def setUp(self):
        self.url = reverse("api:v1:create-customer")
        self.factory = APIRequestFactory()
        self.user = UserFactory()
        self.view = CustomerAPIView.as_view()

    def test_post_creates_a_new_customer(self):
        """post: create new customer"""
        # given
        data = {
            "first_name": "First",
            "last_name": "Last",
            "dob": "2020-01-01",
        }
        request = self.factory.post(self.url, data)
        force_authenticate(request, user=self.user)
        # when
        response = self.view(request)
        # then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Customer.objects.filter(**data).exists())

    def test_post_raise_validation_error(self):
        """post: raise validation errors for invalid data"""
        # given
        data = {}
        request = self.factory.post(self.url, data)
        force_authenticate(request, user=self.user)
        # when
        response = self.view(request)
        # then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_return_403_for_unauthenticated_request(self):
        """post: return 403 for unauthenticated request"""
        # given
        data = {
            "first_name": "First",
            "last_name": "Last",
            "dob": "2020-01-01",
        }
        request = self.factory.post(self.url, data)
        # when
        response = self.view(request)
        # then
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class InsurancePolicyAPIViewTestCase(TestCase):
    """Tests for InsurancePolicyAPIView"""

    def setUp(self):
        self.url = reverse("api:v1:create-policy")
        self.factory = APIRequestFactory()
        self.user = UserFactory()
        self.view = InsurancePolicyAPIView.as_view()

    def test_post_creates_a_new_insurance_policy(self):
        """post: create new insurance policy"""
        # given
        data = {
            "customer_id": CustomerFactory().id,
            "type": "personal-accident",
            "premium": 200,
            "cover": 200000,
        }
        policy_data = copy.deepcopy(data)
        policy_data["policy_type"] = policy_data.pop("type")
        request = self.factory.post(self.url, data)
        force_authenticate(request, user=self.user)
        # when
        response = self.view(request)
        # then
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(InsurancePolicy.objects.filter(**policy_data).exists())

    def test_post_raise_validation_error(self):
        """post: raise validation errors for invalid data"""
        # given
        data = {}
        request = self.factory.post(self.url, data)
        force_authenticate(request, user=self.user)
        # when
        response = self.view(request)
        # then
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_return_403_for_unauthenticated_request(self):
        """post: return 403 for unauthenticated request"""
        # given
        data = {
            "customer_id": CustomerFactory().id,
            "type": "personal-accident",
            "premium": 200,
            "cover": 200000,
        }
        request = self.factory.post(self.url, data)
        # when
        response = self.view(request)
        # then
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
