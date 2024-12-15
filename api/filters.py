from django_filters import rest_framework as filters

from api.models import Expense


class ExpenseFilter(filters.FilterSet):
    min_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    max_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    class Meta:
        model = Expense
        fields = ["amount", "date"]
