import requests


class SwiftLink:

    def __init__(self, username, password, base_url):
        self.__session = requests.Session()
        self.__session.auth = (username, password)
        self.__base_url = base_url

    def user_auth(self):
        response = self.__session.get(f'{self.__base_url}/user')
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return False
        except requests.exceptions.RequestException:
            return False
        return True

    def user_create(self):
        try:
            response = self.__session.post(f'{self.__base_url}/user')
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return False
        except requests.exceptions.RequestException:
            return False
        return True

    def change_password(self, password=None):
        headers = {'new-password': password}
        try:
            response = self.__session.put(url=f'{self.__base_url}/user', headers=headers)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return False
        except requests.exceptions.RequestException:
            return False
        # 更新Session
        self.__session.auth = (self.__session.auth[0], password)
        return response.json()

    def get_shortlinks(self):
        try:
            response = self.__session.get(f"{self.__base_url}/shortlinks")
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        except requests.exceptions.RequestException as e:
            return e
        return response.json()

    def create_short_link(self, route, url):
        params = {"route": route, "url": url}
        try:
            response = self.__session.post(f"{self.__base_url}/shortlink", params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            return False
        except requests.exceptions.RequestException as e:
            return False
        return True

    def delete_short_link(self, route):
        params = {"route": route}
        try:
            response = self.__session.delete(f"{self.__base_url}/shortlink", params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        except requests.exceptions.RequestException as e:
            return e
        return True

    def update_short_link(self, route, new_route, new_url):
        params = {"route": route, "new_route": new_route, "new_url": new_url}
        try:
            response = self.__session.put(f"{self.__base_url}/shortlink", params=params)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            return e
        except requests.exceptions.RequestException as e:
            return e
        return True
