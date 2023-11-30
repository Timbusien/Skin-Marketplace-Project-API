from database.models import Skin, SkinPhoto
from datetime import datetime
from database import get_database


def add_skin_my_db(skin_name, flot, exterior, cost_skin):
    my_db = next(get_database())
    new_skin = Skin(skin_name=skin_name,
                    flot=flot,
                    cost_skin=cost_skin,
                    exterior=exterior,
                    skin_date=datetime.now())

    my_db.add(new_skin)
    my_db.commit()

    return 'Skin added Successfully'


def edit_skin_my_db(skin_id, edit_type, new_data):
    my_db = next(get_database())
    exact_skin = my_db.query(Skin).filter_by(skin_id=skin_id).first()

    if exact_skin:
        if edit_type == 'skin_name':
            exact_skin.skin_name = new_data
        elif edit_type == 'flot':
            exact_skin.flot = new_data
        elif edit_type == 'exterior':
            exact_skin.exterior = new_data
        my_db.commit()

        return 'Skin info changed successfully'
    else:
        return 'Skin in not Found'


def add_skin_photo_my_db(skin_id, skin_photo):
    my_db = next(get_database())
    new_skin_photo = SkinPhoto(skin_id=skin_id, skin_photo=skin_photo)

    my_db.add(new_skin_photo)
    my_db.commit()

    return 'Photo of skin successfully added'


def delete_skin_my_db(skin_id):
    my_db = next(get_database())
    check_skin = my_db.query(Skin).filter_by(skin_id=skin_id).first()
    skin_photo_check = my_db.query(SkinPhoto).filter_by(skin_id=skin_id).first()

    if check_skin:
        my_db.delete(check_skin)
        my_db.commit()
        my_db.delete(skin_photo_check)
        my_db.commit()

    return 'Skin deleted successfully'


def get_exact_user_skin_my_db(user_id):
    my_db = next(get_database())
    exact_user_skin = my_db.query(Skin).filter_by(user_id=user_id).first()

    return exact_user_skin


def get_exact_skin(skin_id):
    my_db = next(get_database())
    exact_skin = my_db.query(Skin).filter_by(skin_id=skin_id).first()

    if exact_skin:
        return exact_skin
    else:
        return False


def get_all_skins():
    my_db = next(get_database())
    all_skins = my_db.query(Skin).all()

    return all_skins
