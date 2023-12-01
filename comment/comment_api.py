from fastapi import APIRouter
from comment import CommentValidate, EditCommentValidate
from database.commentsservice import add_comment_my_db, edit_comment_my_db, delete_comment_my_db, get_comment_my_db

comment_router = APIRouter(prefix='/comment', tags=['Comment Management'])


@comment_router.post('/add-comment')
async def add_skin_comment(data: CommentValidate):
    result = add_comment_my_db(**data.model_dump())

    return {'message': result}


@comment_router.put('/edit-comment')
async def edit_skin_comment(data: EditCommentValidate):
    change_comment = data.model_dump()
    result = edit_comment_my_db(**change_comment)

    if result:
        return {'message': result}
    else:
        return {'message': 'Comment does not exist'}


@comment_router.delete('/delete-comment')
async def delete_skin_comment(comment_id: int):
    result = delete_comment_my_db(comment_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Comment does not exist'}


@comment_router.get('/get-comment')
async def get_comment(skin_id: int):
    result = get_comment_my_db(skin_id)

    return {'message': result}


