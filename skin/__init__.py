from pydantic import BaseModel


class AddSkin(BaseModel):
    user_id: int
    skin_name: str
    flot: float
    cost_skin: int
    exterior: str


class SkinEdit(BaseModel):
    skin_id: int
    user: int


class EditSkin(BaseModel):
    skin_id: int
    edit_type: str
    new_data: str







