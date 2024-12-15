from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from api.data_transfer_objects import ExpensesPerCategoryInputDTO
from api.filters import ExpenseFilter
from api.models import Expense
from api.repository import ExpenseDjangoRepository
from api.serializers import ExpenseSerializer, ExpensesPerCategorySerializer
from api.use_case import ExpensesPerCategoryUseCase


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.select_related("category", "user")
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExpenseFilter

    def get_serializer_class(self):
        if self.action == "expenses_per_category":
            return ExpensesPerCategorySerializer
        return ExpenseSerializer

    @action(detail=False, methods=["get"], url_path="expenses-per-category")
    def expenses_per_category(self, request, *args, **kwargs):

        user_id = request.query_params.get("user_id")
        month = request.query_params.get("month")
        year = request.query_params.get("year")

        input_data = ExpensesPerCategoryInputDTO(month=month, year=year, user_id=user_id)

        use_case = ExpensesPerCategoryUseCase(expense_repository=ExpenseDjangoRepository())
        result = use_case.execute(input_data)

        serializer = self.get_serializer(result, many=True)
        return Response(serializer.data)
