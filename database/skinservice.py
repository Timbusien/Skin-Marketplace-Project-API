from database.models import Skin, SkinPhoto
from datetime import datetime
from database import get_database


def add_skin_my_db(skin_name, flot, exterior):
    my_db = next(get_database())
    new_skin = Skin(skin_name=skin_name,
                    flot=flot,
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

        return 'skin info changed successfully'
    else:
        return 'Skin in not Found'

