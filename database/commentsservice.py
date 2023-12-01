from database.models import Comment
from datetime import datetime
from database import get_database


def add_comment_my_db(user_id, comment_text, skin_id):
    my_db = next(get_database())
    new_comment = Comment(skin_id=skin_id, comment_text=comment_text, user_id=user_id)

    my_db.add(new_comment)
    my_db.commit()

    return 'The skin comment added Successfully'


def edit_comment_my_db(comment_id, new_comment):
    my_db = next(get_database())
    edit_comment = my_db.query(Comment).filter_by(comment_id=comment_id).first()

    if edit_comment:
        edit_comment.comment_text = new_comment
        my_db.commit()
        return 'Comment changed Successfully'
    else:
        return False


def delete_comment_my_db(comment_id):
    my_db = next(get_database())
    delete_comment = my_db.query(Comment).filter_by(comment_id=comment_id).first()

    if delete_comment:
        my_db.delete(delete_comment)
        my_db.commit()
        return 'Comment deleted Successfully'
    else:
        return False


def get_comment_my_db(skin_id):
    my_db = next(get_database())
    skin_comment = my_db.query(Comment).filter_by(skin_id=skin_id).first()

    return skin_comment



