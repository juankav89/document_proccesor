from requests.exceptions import RequestException


class Writer:
    __db = {}  # document_root persist

    def __init__(self, **kwargs):
        self.__db = kwargs['db']

    def __add_deep_data(self, parent_node, route, key, new_data):
        route.pop(0)
        response = []
        for child_node in parent_node:
            is_node = child_node["name"] == route[0]
            if is_node and len(route) > 1:
                child_node = self.__add_deep_data(child_node, route, key, new_data)
            elif is_node:
                child_node['sections'].append({"name": key, "text": new_data, "sections": []})
            response.append(child_node)

        return response

    def add_document(self, input_data):
        path_route = input_data["path"].split(".")
        new_db = self.__db
        new_db['sections'] = self.__add_deep_data(
            self.__db['sections'], path_route, input_data["name"], input_data["text"])
