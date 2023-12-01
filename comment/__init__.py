from pydantic import BaseModel


class CommentValidate(BaseModel):
    comment_text: str
    user_id: int
    skin_id: int


class EditCommentValidate(BaseModel):
    comment_id: int
    new_comment: str




