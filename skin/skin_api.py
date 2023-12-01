from skin import AddSkin, EditSkin
from fastapi import APIRouter, UploadFile, Body
from database.skinservice import (add_skin_my_db, edit_skin_my_db, add_skin_photo_my_db,
                                  delete_skin_my_db, get_exact_skin_my_db, get_all_skins_my_db)

skin_router = APIRouter(prefix='/skin', tags=['Skin Management'])


@skin_router.post('/add-skin')
async def add_skin(data: AddSkin):
    result = add_skin_my_db(**data.model_dump())

    return {'message': result}


@skin_router.post('edit-skin')
async def edit_skin(data: EditSkin):
    change_skin = data.model_dump()

    result = edit_skin_my_db(**change_skin)

    if result:
        return {'message': result}
    else:
        return {'message': 'User does not exist'}


@skin_router.delete('/delete-skin')
async def delete_skin(skin_id: int):
    result = delete_skin_my_db(skin_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Skin does not exist'}


@skin_router.get('/get-skin')
async def get_exact_skin(skin_id: int):
    result = get_exact_skin_my_db(skin_id)

    if result:
        return {'message': result}
    else:
        return {'message': 'Skin not Found'}


@skin_router.get('/get-all-skins')
async def get_all_skins():
    result = get_all_skins_my_db()

    return {'message': result}


@skin_router.post('/add-skin-photo')
async def add_skin_photo(skin_id: int = Body(),
                         user_id: int = Body(),
                         photo_file: UploadFile = None):
    photo_path = f'/media/{photo_file.filename}'
    try:
        with open(f'media/{photo_file.filename}', 'wb') as file:
            skin_photo_add = await photo_file.read()
            file.write(skin_photo_add)

        result = add_skin_photo_my_db(skin_id=skin_id, skin_photo=photo_path)

    except Exception as error:
        result = error

    return {'message': result}


