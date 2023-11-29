import os
from pathlib import Path
from fastapi import APIRouter, UploadFile, HTTPException
from user import LoginUserValidator, RegisterUserValidator, EditUserValidator
from database.userservice import (login_user_my_db, register_user_my_db, edit_user_my_db, get_all_users, get_exact_user,
                                  delete_user_photo, add_profile_photo_my_db)

user_router = APIRouter(prefix='/user', tags=['User Management'])


@user_router.post('/register')
async def register_user(data: RegisterUserValidator):
    result = register_user_my_db(**data.model_dump())

    if result:
        return {'message': result}
    else:
        return {'message': 'User exist'}


@user_router.post('/login')
async def login_user(data: LoginUserValidator):
    result = login_user_my_db(**data.model_dump())

    return result


@user_router.put('/edit')
async def edit_user(data: EditUserValidator):
    change_data = data.model_dump()
    result = edit_user_my_db(**change_data)

    if result:
        return {'message': result}
    else:
        return {'message': 'This '}


@user_router.get('/get-user')
async def get_user(user_id: int = 0):
    if user_id == 0:
        result = get_all_users()
        return {'message': result}
    else:
        result = get_exact_user(user_id)
        return {'message': result}

upload_folder = ''


@user_router.post('/add-avatar')
async def add_user_profile_photo(photo_file: UploadFile, user_id: int):
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)

    return {'message': 'Success'}


@user_router.put('/edit-avatar')
async def edit_user_avatar(new_photo_file: UploadFile):
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()
        file.write(user_photo)

    return {'message': 'Successfully changed'}


@user_router.delete('/delete-avatar')
async def delete_user_avatar(filename: str):
    file_path = os.path.join(upload_folder, filename)

    if not Path(file_path).is_file():
        raise HTTPException(status_code=404, detail='File not found')
    os.remove(file_path)

    return {'message': 'Deleted successfully'}




