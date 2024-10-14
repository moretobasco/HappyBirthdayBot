from app.dao.base import BaseDAO
from app.corporate_emails.models import CorporateEmailRegistry


class CorporateEmailDAO(BaseDAO):
    model = CorporateEmailRegistry


