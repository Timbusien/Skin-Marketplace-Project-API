from datetime import datetime
from database.models import User
from database import get_database


def register_user_my_db(nick, trade_link, email, password):
    my_db = next(get_database())
    new_user = User(nick=nick,
                    trade_link=trade_link,
                    email=email,
                    password=password,
                    register_date=datetime.now())
    my_db.add(new_user)
    my_db.commit()

    return 'SUCCESS, user have been registered'


def login_user_db(email, password):
    my_db = next(get_database())
    check = my_db.query(User).filter_by(email=email).first()

    if check:
        if check.password == password:
            return check
        elif check.password != password:
            return 'Password incorrect'
    else:
        return 'Data Error'


def edit_user_my_db(user_id, edit_type, new_data):
    my_db = next(get_database())
    exact_user = my_db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_type == 'email':
            exact_user.email = new_data
        elif edit_type == 'nick':
            exact_user.nick = new_data
        elif edit_type == 'trade_link':
            exact_user.trade_link = new_data
        elif edit_type == 'password':
            exact_user.password = new_data

        my_db.commit()

        return 'data changed successfully'

    else:
        return 'User is not found'


def add_profile_photo_my_db(user_id, profile_photo):
    my_db = next(get_database())
    check = my_db.query(User).filter_by(user_id=user_id).first()

    if check:
        check.profile_photo = profile_photo
        return 'Profile photo added Successfully'
    else:
        return False


def delete_user_photo(user_id):
    my_db = next(get_database())
    check = my_db.query(User).filter_by(user_id=user_id).first()

    if check:
        check.profile_photo = 'None'
        my_db.commit()
        return 'Profile photo deleted Successfully'
    else:
        return False


def get_all_users():
    my_db = next(get_database())
    all_users = my_db.query(User).all()

    return all_users


def get_exact_user(user_id):
    my_db = next(get_database())
    user_inventory = my_db.query(User).filter_by(user_id=user_id).first()

    return user_inventory
