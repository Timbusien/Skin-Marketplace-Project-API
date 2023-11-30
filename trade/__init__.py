from pydantic import BaseModel


class CreateTradeValidator(BaseModel):
    skin_to_id: int
    skin_from_id: int
    cost_skin: int
    skin_id: int


class CancelTradeValidator(BaseModel):
    skin_to_id: int
    skin_from_id: int
    cost_skin: int
    skin_id: int
    trade_id: int




