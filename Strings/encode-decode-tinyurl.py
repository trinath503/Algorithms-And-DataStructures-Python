
import random


class Codec(object):
    def __init__(self):
        self.__random_length = 6
        self.__tiny_url = "'http://tinyurl.com/'"
        self.__alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__lookup = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        def getRand():
            rand = []
            for _ in range(self.__random_length):
                rand += self.__alphabet[random.randint(0, len(self.__alphabet)-1)]
            print(rand)
            return "".join(rand)

        key = getRand()
        while key in self.__lookup:
            key = getRand()
        self.__lookup[key] = longUrl
        return self.__tiny_url + key

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.__lookup[shortUrl[len(self.__tiny_url):]]



c =Codec()
print(c.encode('http://tinyurl.com/'))
