from django_filters import rest_framework as filters


class ExpenseFilter(filters.FilterSet):
    min_date = filters.DateFilter(field_name="date", lookup_expr="gte")
    max_date = filters.DateFilter(field_name="date", lookup_expr="lte")

    # class Meta:
    #     model = Expense
    #     fields = ['category', 'in_stock']
