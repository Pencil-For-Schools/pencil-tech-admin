import requests

class APIRequest:
    """
    Simple class with methods to build a url and make a call to the external api.
    """

    def build_url(self, base_url, resource, trailing_slash=False, resource_id=None):
        """base method to build the url for base api calls in the integrations app.
            Trailing slash denotes the trailing slash after the resource
        Args:
            base_url (string): _description_
            resource (string): _description_
            trailing_slash (bool): _description_
            id (int): _description_
        """
        url = f'{base_url}/{resource}'
        if resource_id:
            url += f'/{resource_id}'
        elif trailing_slash:
            url += '/'

        return url

    def call_api(self, url, method, params=None, headers=None, body=None, auth=None, data=None):
        """base method to call to the external api
        Args:
            url (string): url typically returned from self.build_url
            method (string)): POST | PUT | PATCH | DELETE
            params (dict, optional): Defaults to None.
            headers (dict, optional): Defaults to None.
            body (dict, optional): Defaults to None.
            auth (tuple, optional): Defaults to None. Typically Client ID and Client secret
        """
        response = requests.request(method, url, auth=auth, data=data, params=params, json=body, headers=headers, timeout=3)

        return response
