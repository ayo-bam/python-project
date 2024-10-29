class Website:
    def __init__(self, url, request):
        if not self.is_valid_url(url):
            raise ValueError("Invalid URL")
        if not isinstance(request, Request):
            raise TypeError("Request object must be an instance of the Request class")
        self.url = url
        self.request = request

    def is_valid_url(self, url):
        return url.startswith("http://") or url.startswith("https://")


url = "https://www.example.com"
request_obj = Request()
website = Website(url, request_obj)
