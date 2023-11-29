from pydantic import BaseModel


class AddSkin(BaseModel):
    user_id: int
    skin_name: str
    skin_date: str
    flot: float
    cost_skin: float
    exterior: str






