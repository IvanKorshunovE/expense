from api.data_transfer_objects import ExpensesPerCategoryInputDTO


class ExpensesPerCategoryUseCase:
    """
    Use case for retrieving total expenses per category for a given month and year.
    """

    def __init__(self, expense_repository):
        self.expense_repository = expense_repository

    def execute(self, input_dto: ExpensesPerCategoryInputDTO):

        month = input_dto.month
        year = input_dto.year
        user_id = input_dto.user_id

        expenses = self.expense_repository.get_expenses_per_category(month, year, user_id)
        return [
            {"category": entry["category__name"], "total_amount": entry["total_amount"]}
            for entry in expenses
        ]
