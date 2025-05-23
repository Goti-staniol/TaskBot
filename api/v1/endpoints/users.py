from fastapi import APIRouter, status


router = APIRouter(prefix='api/v1/users', tags=['users'])


@router.post('/', summary='Create New User')
async def create():
    pass


@router.put('/{user_id}', summary='Update User Info')
async def update(user_id: int):
    pass


@router.delete('/{user_id}')
async def delete(user_id: int):
    pass


@router.patch('/{user_id}')
async def patch(user_id):
    pass