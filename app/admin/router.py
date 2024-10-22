# from fastapi import APIRouter
# from fastapi import Response
#
# from app.admin.auth import authenticate_user, create_access_token
# from app.exceptions import IncorrectEmailOrPasswordException
# from app.users.schemas import SAdminAuth
#
# router = APIRouter(
#     prefix='/admin_panel',
#     tags=['Admin']
# )
#
#
# @router.post('/login')
# async def login_user(response: Response, user_data: SAdminAuth):
#     user = await authenticate_user(user_data.email, user_data.password)
#     if not user:
#         raise IncorrectEmailOrPasswordException
#     access_token = create_access_token({'sub': str(user.user_id)})
#     response.set_cookie('birthday_access_token', access_token, httponly=True)
#     return access_token
