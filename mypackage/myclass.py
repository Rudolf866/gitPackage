import uuid


class UUIDUsername:
    def __init__(self):
        pass

    def create_user_uuid(self, user_name):
        return f" {user_name} uuid: {uuid.uuid1()}"


__all__ = (
    "UUIDUsername",
)
