class Message:
    E000000 = 'unauthorized'
    E000001 = '{0}を力してください。'
    E000002 = 'パラメーター「{}」が正しくありませ。'
    E000003 = '{0}項目は数値を力してください。'
    E000004 = '{0}項目は{1}文字以内で入力してください。'
    DEFAULT_ERROR_MESSAGE = 'Have an error in the server'


class MessageResponse:
    __name = ''

    # Setter cho name
    def setName(self, name):
        self.__name = name
        self.MESSAGE_SUCCESS_CREATED = f'Successfully added {name}!'
        self.MESSAGE_SUCCESS_UPDATED = f'Successfully updated {name}!'
        self.MESSAGE_SUCCESS_DELETED = f'Successfully deleted {name}!'
        self.MESSAGE_SUCCESS_RESTORE = f'Successfully restore {name}!'
        self.MESSAGE_SUCCESS_GET_INFO = f'Successfully get {name} info!'
        self.MESSAGE_SUCCESS_GET_LIST = f'Successfully get {name} list!'
        self.MESSAGE_ERROR_NOT_EXIST = f'{name} does not exist!'
        self.MESSAGE_ERROR_TABLE_EXIST = f'{name} is being used in another table!'
        self.MESSAGE_ERROR_DISPOSED = f'{name} is disposed!'
        self.MESSAGE_ERROR_OPERATING = f'{name} is in operation process!'
        self.MESSAGE_ERROR_STATUS_COMPLETED_DELETED = f'Cannot delete because {name} have completed operation!'
        self.MESSAGE_ERROR_STATUS_COMPLETED_UPDATED = f'Cannot update because {name} have completed operation!'
        self.MESSAGE_ERROR_ITEM_IS_NOT_MAIN = f'The main item must be added to {name} first!'
        self.MESSAGE_ERROR_BEING_ORDERED = f'Can not delete because {name} is being ordered!'

    # Getter cho name
    def getName(self):
        return self.__name
