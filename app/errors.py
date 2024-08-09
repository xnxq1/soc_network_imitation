from fastapi import HTTPException


class BaseCustomError(Exception):
    message = "Unknown"
    status_code = 500
    def __init__(self):
        raise HTTPException(status_code=self.status_code, detail=self.message)
