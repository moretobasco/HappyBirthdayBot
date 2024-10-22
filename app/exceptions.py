from fastapi import HTTPException, status


class SubscriptionException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserIsNotFoundException(SubscriptionException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'User you want to subscribe does not exist'


class DublicatedSubscriptionException(SubscriptionException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'This subscription already exists'


class UserException(HTTPException):
    status_code = 500
    detail = ''

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)


class UserNotExists(UserException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'This user does not exist'


class UserAlreadyExistsException(UserException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'This user already exists'


class CorporateEmailNotExists(UserException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'This email is not corporate'


class IncorrectPasswordException(UserException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Incorrect temporary password'


class ExpiredPasswordException(UserException):
    status_code = status.HTTP_409_CONFLICT
    detail = 'Your temporary password expired'


class IncorrectEmailOrPasswordException(UserException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Wrong email or password'


class TokenAbsentException(UserException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token is absent'


class TokenExpiredException(UserException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Token has expired'


class IncorrectTokenFormatException(UserException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'Wrong token format'


class UserIsNotAdmin(UserException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = 'User is not admin'


class AsyncPgErrors(Exception):
    pass


class DublicateSubscriptionError(AsyncPgErrors):
    """Error: this subscription already exists"""
    pass


class UserNotFoundError(AsyncPgErrors):
    """Error: user you want to subscribe does not exist"""
    pass


class EmailSendError(Exception):
    """Error: Failed to send message"""
