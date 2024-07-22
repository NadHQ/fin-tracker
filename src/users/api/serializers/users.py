from src.core.serializer import BaseSerializer


class UsersSerializer(BaseSerializer):
    uuid: str
    name: str
    password: str
