from data_user_profile_get_model import DataUserProfileGetModel


class UserProfileGet:
    def __init__(self, status: str, data: DataUserProfileGetModel):
        self.status = status
        self.data = data.__dict__

    def __str__(self):
        return self.__dict__
