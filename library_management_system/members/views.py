from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

from .models import Member
from .serializers import MemberSerializer


class MemberPagination(PageNumberPagination):
    page_size = 3


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = MemberPagination

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = ['is_active']
    search_fields = ['name', 'email', 'phone']
    ordering_fields = ['name', 'membership_date']
