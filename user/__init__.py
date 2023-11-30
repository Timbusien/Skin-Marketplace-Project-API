from pydantic import BaseModel


class RegisterUserValidator(BaseModel):
    nick: str
    trade_link: str
    email: str
    password: str
    balance: int


class LoginUserValidator(BaseModel):
    email: str
    password: str


class EditUserValidator(BaseModel):
    user_id: int
    edit_type: str
    new_data: str


