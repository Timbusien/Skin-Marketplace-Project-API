from pydantic import BaseModel


class CommentValidate(BaseModel):
    comment_text: str
    skin_id: int
    user_id: int


class EditCommentValidate(BaseModel):
    new_text: str
    comment_id: int





