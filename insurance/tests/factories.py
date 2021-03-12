import factory
from django.contrib.auth.models import User

from insurance.models import Customer


class UserFactory(factory.django.DjangoModelFactory):
    """Factory for generating django auth users"""
    class Meta:
        model = User


class CustomerFactory(factory.django.DjangoModelFactory):
    """Factory for generating customers"""
    class Meta:
        model = Customer

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('first_name')
    dob = factory.Faker('date')
