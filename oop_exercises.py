# Question 2: Website and Request Classes

class Request:
    def download_page(self, url):
        return f"Downloading page from {url}"

class Website:
    def __init__(self, url, request):
        if not isinstance(request, Request):
            raise ValueError("request must be an instance of the Request class")
        self.url = url
        self.request = request

    def website_title(self):
        return self.request.download_page(self.url)


url = "https://example.com"
request_obj = Request()
website = Website(url, request_obj)
print(website.website_title()) 