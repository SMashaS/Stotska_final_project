from data_user_settings_get_model import DataUserSettingsGetModel


class UserSettingsGet:
    def __init__(self, status: str, data: DataUserSettingsGetModel):
        self.status = status
        self.data = data.__dict__

    def __str__(self):
        return self.__dict__
