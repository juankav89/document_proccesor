from requests.exceptions import RequestException


class Writer:
    __db = {}  # document_root persist

    def __init__(self, **kwargs):
        self.__db = kwargs['db']

    @staticmethod
    def __set_new_data(parent_node, route, key, new_data):
        __child_node = list(filter(lambda x: x['name'] == route[0], parent_node[0]["sections"]))
        if __child_node:
            __child_node[0]['sections'].append({
                "name": key,
                "text": new_data,
                "sections": []
            })
        else:
            parent_node[0]['sections'].append({
                "name": route[0],
                "text": new_data,
                "sections": [{
                    "name": key,
                    "text": new_data,
                    "sections": []
                }]
            })

    def __add_deep_data(self, parent_node, route, key, new_data):
        __response = []
        route.pop(0)
        if len(route) == 1:
            self.__set_new_data(parent_node, route, key, new_data)
            return "ok"
        for __child_node in parent_node:
            is_node = __child_node["name"] == route[0]
            if is_node and len(route) > 1:
                __child_node = self.__add_deep_data(__child_node['sections'], route, key, new_data)
            __response.append(__child_node)
        return "ok"

    def add_document(self, input_data):
        __path_route = input_data["path"].split(".")
        if len(__path_route) == 1:
            self.__db.append({
                "name": __path_route[0],
                "text": input_data["text"],
                "sections": [{
                    "name": input_data["name"],
                    "text": input_data["text"],
                    "sections": []
                }]
            })
            return "ok"
        return self.__add_deep_data(self.__db, __path_route, input_data["name"], input_data["text"])
