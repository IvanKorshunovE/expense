from api.models import Expense
from django.db.models import Sum


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
        qs = Expense.objects.filter(date__year=year, date__month=month, user_id=user_id)
        return qs.values("category__name").annotate(total_amount=Sum("amount"))
