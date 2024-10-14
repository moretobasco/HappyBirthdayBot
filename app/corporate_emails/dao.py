from app.dao.base import BaseDAO
from app.corporate_emails.models import CorporateEmail


class CorporateEmailDAO(BaseDAO):
    model = CorporateEmail


