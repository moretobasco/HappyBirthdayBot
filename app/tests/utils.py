import json
import secrets
import string
from pprint import pprint
import re


def make_new_dict():
    new_list = []
    for i in range(1, 340):
        new_dict = {}
        new_dict.update(
            {
                   'user_id': 1,
                   'user_sub_id': i,
                   'notify_before_days': '[1, 2, 3]',
                   'notify_on_day': True
            },
        )
        new_list.append(new_dict)
    return json.dumps(new_list, ensure_ascii=False, indent=4)




def prepare_mock_emails(user: str, year: str):
    shablon = f'{user + year}@test.com'
    return shablon


def generate_secret_int() -> str:
    password = ''.join(secrets.choice(string.digits) for _ in range(8))
    return password


def prepare_mock_users():
    mock_users = []
    mock_corporate_emails = []
    for row in sql_users:
        new_row = []
        # for column in row:
        #     new_row.append(column)
        year: str = row[1].split('-')[0]
        mock_email = prepare_mock_emails(user=row[0], year=year)
        new_row.append(mock_email)
        # mock_corporate_emails.append(mock_email)
        # password = int(generate_secret_int())
        # new_row.append(password)
        mock_users.append(new_row)
    return mock_users


def prepare_mock_subs():
    mock_subs = []
    for i in range(1, 366):
        new_row = [i, 1, '[1, 2, 3]', True]
        mock_subs.append(new_row)
    return mock_subs








