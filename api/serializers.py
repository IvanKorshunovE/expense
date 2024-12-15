from rest_framework import serializers

from api.models import Expense, User, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
        ]


class UserSerializer(serializers.ModelSerializer):  # perhaps name it ExpenseUserSerializer for consistency
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email"
        ]


class ExpenseSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    category = CategorySerializer()

    class Meta:
        model = Expense
        fields = [
            "id",
            "title",
            "user",
            "amount",
            "date",
            "category",
        ]


class ExpensesPerCategorySerializer(serializers.ModelSerializer):
    total_amount = serializers.FloatField()

    class Meta:
        model = Category
        fields = ["id", "name", "total_amount"]
