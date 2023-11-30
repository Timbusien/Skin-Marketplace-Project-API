from pydantic import BaseModel


class CreateTradeValidator(BaseModel):
    skin_to: int
    skin_from: int
    skin_cost: int
    status: bool
    skin_name: str


class CancelTradeValidator(BaseModel):
    skin_to: int
    skin_from: int
    skin_cost: int
    status: bool
    skin_name: str
    trade_id: int




