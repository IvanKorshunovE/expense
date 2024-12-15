from pydantic import BaseModel, Field, conint

class ExpensesPerCategoryInputDTO(BaseModel):
    """
    DTO for validating input to ExpensesPerCategoryUseCase.
    """
    month: conint(ge=1, le=12) = Field(description="Month (1-12)")
    year: int = Field(description="Year in YYYY format")
    user_id: int = Field(description="User ID (must be provided)")

    class Config:
        json_schema_extra = {
            "example": {
                "month": 12,
                "year": 2024,
                "user_id": 5
            }
        }
