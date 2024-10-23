import json

import pytest
from app.database import Base, async_session_maker, engine
from app.config import settings
from app.users.models import Users
from app.subscription.models import Subscriptions
from app.corporate_emails.models import CorporateEmail


@pytest.fixture(autouse=True)
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_sql(model: str):
        with open(f'app/tests/mock_{model}.sql', 'r') as file:
            return json.load(file)

    users = open_mock_sql('users')
    subscriptions = open_mock_sql('subscriptions')
    corporate_emails = open_mock_sql('corporate_emails')

    async with async_session_maker() as session:
        ...
