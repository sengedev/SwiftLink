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


if __name__ == '__main__':
    import time
    username = 'testuser'
    password = 'testpassword'
    base_url = 'http://localhost:8000'
    swift_link = SwiftLink(username, password, base_url)
    # 创建用户
    create_user = swift_link.user_create()
    if create_user:
        print("创建用户成功")
    else:
        print("创建用户失败")
    # 用户认证
    auth = swift_link.user_auth()
    if auth:
        print("用户认证成功")
    else:
        print("用户认证失败")
    # 修改密码
    change_passwd = swift_link.change_password('newpassword')
    if change_passwd:
        print("修改密码成功")
    else:
        print("修改密码失败")
    # 添加短链接
    create_bili = swift_link.create_short_link('bili', 'https://bilibili.com')
    print(f"添加“BiliBili” {'成功' if create_bili else '失败'}")
    create_baidu = swift_link.create_short_link('baidu', 'https://www.baidu.com')
    print(f"添加“Baidu” {'成功' if create_baidu else '失败'}")
    # 获取所有短链接
    shortlinks = swift_link.get_shortlinks()
    print(f"所有短链接：{shortlinks}")
    # 将baidu改为google
    edit = swift_link.update_short_link('baidu', 'google', 'https://www.google.com')
    if edit == True:
        print("修改短链接成功")
    else:
        print(f"修改短链接失败，错误代码：{edit}")
    # 删除bilibili
    delete = swift_link.delete_short_link('bili')
    if delete == True:
        print("删除短链接成功")
    else:
        print(f"删除短链接失败，错误代码：{delete}")
    # 获取所有短链接
    shortlinks = swift_link.get_shortlinks()
    print(f"所有短链接：{shortlinks}")
