import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    prazo = django_filters.DateFilter(field_name='prazo', lookup_expr='exact')
    
    class Meta:
        model = Task
        fields = ['status', 'responsavel', 'prazo']