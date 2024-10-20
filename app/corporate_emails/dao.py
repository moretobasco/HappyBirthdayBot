from app.dao.base import BaseDAO
from app.corporate_emails.models import CorporateEmail
from app.database import async_session_maker
from sqlalchemy import select, func, cast, and_, or_, Insert, insert, literal, update, delete


class CorporateEmailDAO(BaseDAO):
    model = CorporateEmail
