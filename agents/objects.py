from pydantic import BaseModel, Field


class Answer(BaseModel):
    answer: str = Field(description="The answer to the question")
    conversation: bool = Field(
        description="This is the indicator to know if conversation should still continue or no"
        "If agent has made the decision of the refund then this should be False."
        "If the conversation is still need more talk then it's True.", default=True
    )


class PurchaseItem(BaseModel):
    name: str = Field(
        description="The name of the item purchased")
