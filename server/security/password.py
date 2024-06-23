from argon2 import PasswordHasher
import argon2
import string
import secrets


class Password:

    def __init__(self):
        """
        初始化Argon2 ID
        """
        self.__ph = PasswordHasher(
            type=argon2.low_level.Type.ID,
            time_cost=2,
            memory_cost=1024,
            parallelism=2,
            hash_len=16,
            salt_len=16,
        )

    def calculate(self, password: str):
        """
        计算散列值
        :param password: 密码
        :return: 散列值
        """
        return self.__ph.hash(password)

    def verify(self, hashed: str, password: str):
        """
        验证密码
        :param hashed: 散列值
        :param password: 密码
        :return:
        """
        try:
            self.__ph.verify(hashed, password)
        except argon2.exceptions.VerifyMismatchError:
            return False
        except argon2.exceptions.InvalidHash:
            return False
        else:
            # 再次散列密码
            return self.__ph.hash(password)

    @staticmethod
    def generate(length=32):
        """
        生成随机密码
        :param length: 密码长度
        :return: 随机密码
        """
        # 包含大写字母、小写字母和数字
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        punctuation = string.punctuation
        # 首尾不包含特殊字符
        first = secrets.choice(lower + upper + digits)
        latest = secrets.choice(lower + upper + digits)
        # 生成密码
        password = first + ''.join(secrets.choice(lower + upper + digits + punctuation) for i in range(length - 2)) + latest
        return password
