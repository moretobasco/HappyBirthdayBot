import json

import pytest
from app.database import Base, async_session_maker, engine
from app.config import settings
from app.users.models import Users
from app.subscription.models import Subscriptions
from app.corporate_emails.models import CorporateEmail
from sqlalchemy import insert
import asyncio
from datetime import datetime

@pytest.fixture(scope='session', autouse=True)
async def prepare_database():
    assert settings.MODE == 'TEST'

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    def open_mock_sql(model: str):
        with open(f'app/tests/mock_{model}.json', encoding='utf-8') as file:
            return json.load(file)

    users = open_mock_sql('users')
    subscriptions = open_mock_sql('subscriptions')
    corporate_emails = open_mock_sql('corporate_emails')

    for user in users:
        user['birthday'] = datetime.strptime(user['birthday'], '%Y-%m-%d')

    async with async_session_maker() as session:
        add_users = insert(Users).values(users)
        add_subscriptions = insert(Subscriptions).values(subscriptions)
        add_corporate_emails = insert(CorporateEmail).values(corporate_emails)

        await session.execute(add_users)
        await session.execute(add_subscriptions)
        await session.execute(add_corporate_emails)

        await session.commit()


# Взято из документации к pytest-asyncio
@pytest.fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()




