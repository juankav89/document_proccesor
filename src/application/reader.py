from requests.exceptions import RequestException


class Reader:
    __db = {}  # document_root persist

    def __init__(self, **kwargs):
        self.__db = kwargs['db']

    def __next_node(self, parent_node, key):
        key.pop(0)
        __sections = parent_node['sections']
        child_node = list(filter(lambda x: x['name'] == key[0], __sections))

        if not __sections or not child_node:
            return {"statusCode": 400, "body": "Data not found"}

        if len(key) == 1:
            return child_node

        return self.__next_node(child_node[0], key)

    def get_document(self, args: dict):
        __data = self.__db
        if "section" in args and args['section'] == "root_document":
            return __data
        __json_route = args['section'].split(".")
        if len(__json_route) <= 1:
            raise RequestException("Not valid 'section' query param")
        return self.__next_node(parent_node=__data, key=__json_route)
