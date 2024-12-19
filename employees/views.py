from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Employee
from .serializers import EmployeeSerializer
import django_filters

class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.CharFilter(field_name='department', lookup_expr='exact')
    role = django_filters.CharFilter(field_name='role', lookup_expr='exact')

    class Meta:
        model = Employee
        fields = ['department', 'role']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = EmployeeFilter
    search_fields = ['name', 'email']
    ordering_fields = ['date_joined', 'name']
    ordering = ['date_joined']
