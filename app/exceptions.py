from fastapi import HTTPException, status


class SubscriptionException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserIsNotFoundException(SubscriptionException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Error: user you want to subscribe does not exist'


class DublicatedSubscriptionException(SubscriptionException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Error: this subscription already exists'


class AsyncPgErrors(Exception):
    pass


class DublicateSubscriptionError(AsyncPgErrors):
    """Error: this subscription already exists"""
    pass


class UserNotFoundError(AsyncPgErrors):
    """Error: user you want to subscribe does not exist"""
    pass
