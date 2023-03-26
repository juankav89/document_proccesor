from requests.exceptions import RequestException


class Writer:
    __db = {}  # document_root persist

    def __init__(self, **kwargs):
        self.__db = kwargs['db']

    def add_document(self, input_data):

        pass
