class Codec:
    def __init__(self):
        self.n = 0
        self.urls = {}

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urls[self.n] = longUrl
        shortUrl = 'http://tinyurl.com/%d' % self.n
        self.n += 1
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.urls[int(shortUrl.split("/")[-1])]
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))