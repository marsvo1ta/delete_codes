import requests
from requests import Response
from streamlit import secrets


class ApiRequest:
    def __init__(self):
        self.find_product_v2_url = secrets['FIND_PRODUCT_V2_URL']
        self.delete_url = secrets['DELETE_URL']
        self.v1_auth = self.get_v1_auth()
        self.v2_auth = {'Authorization': secrets['V2_AUTH']}
        self.anon_token_url = secrets['ANON_TOKEN_URL']
        self.login_url = secrets['LOGIN_URL']
        self.email = secrets['EMAIL']
        self.password = secrets['PASSWORD']
        self.counter = 0

    def get_v1_auth(self):
        anon_token_response = requests.get(self.anon_token_url)
        anon_token = anon_token_response.json()['token']
        header = {'Authorization': f'Bearer {anon_token}'}

        login_body = {
            "email": self.email,
            "password": self.password
        }
        login_response = requests.post(self.login_url, json=login_body, headers=header)
        customer_token = login_response.json()['token']
        auth = {'Authorization': f'Bearer {customer_token}'}
        return auth

    def find_v2(self, code: str) -> Response:
        code = code.strip()
        url = f'{self.find_product_v2_url}?country-code=ua&keyword={code}&locale=uk&size=200'
        response = requests.get(url, headers=self.v2_auth)
        return response

    def get_ids_from_v2(self, code: str) -> list[str]:
        results = self.find_v2(code).json()['results']
        lst = [i['id'] for i in results] if results else None
        return lst

    def delete_code(self, last_id: str) -> Response | None:
        if last_id:
            url = f'{self.delete_url}/{last_id}'
            response = requests.delete(url, headers=self.v1_auth)
            return response
        return None

    def bulk_delete(self, ids: list[str]) -> Response | None:
        if ids:
            for i in ids:
                self.delete_code(i)
                self.counter += 1
        return None



