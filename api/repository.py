from django.db import models
from django.db.models.functions import Coalesce

from api.models import Expense, Category


class ExpenseDjangoRepository:
    """
    Repository for interacting with the Expense model.
    """

    def get_expenses_per_category(self, month, year, user_id):
        """
        Fetch total expenses grouped by category for a given month and year.

        Args:
            month (int): The month to filter expenses.
            year (int): The year to filter expenses.
            user_id (int, optional): The ID of the user to filter expenses.

        Returns:
            QuerySet: A QuerySet containing category names and total expenses.
        """
        expense_subquery = Expense.objects.filter(
            date__year=year, date__month=month, user_id=user_id, category_id=models.OuterRef("pk")
        ).values("category").annotate(
            total_amount=models.Sum("amount")
        ).values("total_amount")
        return Category.objects.annotate(
            total_amount=Coalesce(
                models.Subquery(expense_subquery),
                models.Value(0)
            )
        )
