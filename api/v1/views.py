import logging

from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.serializers import CustomerSerializer, InsurancePolicySerializer

logger = logging.getLogger(__name__)


class BaseCreateAPIView(APIView):
    """Base API view to create resources"""

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = None

    def get_serializer_class(self):
        """Get serializer class to validate input data"""
        if not self.serializer_class:
            raise NotImplementedError
        return self.serializer_class

    def post(self, request, **kwargs):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error('Invalid input received for %s', serializer_class.__name__)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerAPIView(BaseCreateAPIView):
    """View to create a new customer"""
    serializer_class = CustomerSerializer


class InsurancePolicyAPIView(BaseCreateAPIView):
    """View to create a new insurance policy"""
    serializer_class = InsurancePolicySerializer
