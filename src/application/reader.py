from requests.exceptions import RequestException


class Reader:
    __db = {}  # document_root persist

    def __init__(self, **kwargs):
        self.__db = kwargs['db']

    def __next_node(self, parent_node: dict, route: list) -> dict:
        check_last_key = len(route) == 1
        print(route[0])
        child_node = list(filter(lambda x: x['name'] == route[0], parent_node))

        if not child_node:
            return {"statusCode": 400, "body": f"'{route[0]}' does not exist"}
        if check_last_key and route[0] == child_node[0]["name"]:
            return child_node[0]
        if check_last_key:
            return {"statusCode": 400, "body": f"'{route[0]}' does not exist"}

        route.pop(0)
        return self.__next_node(child_node[0]['sections'], route)

    def get_document(self, args: dict):
        __data = self.__db
        __route = args['section'].split(".")
        return self.__next_node(parent_node=__data, route=__route)
