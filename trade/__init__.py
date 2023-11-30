from pydantic import BaseModel


class CreateTradeValidator(BaseModel):
    user_to: int
    user_from: int
    cost_skin: int
    skin_id: int


class CancelTradeValidator(BaseModel):
    skin_to: int
    skin_from: int
    skin_cost: int
    status: bool
    skin_name: str
    trade_id: int




