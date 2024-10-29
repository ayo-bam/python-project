# Question 3: MainRequest and Internet Usage with Requests Library

import requests
from bs4 import BeautifulSoup

class MainRequest:
    def download_page(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "No title found"
            return title
        except requests.exceptions.RequestException as e:
            return f"Error fetching page: {str(e)}"

class Request(MainRequest):
    pass

class Website:
    def __init__(self, url, request):
        if not isinstance(request, Request):
            raise ValueError("request must be an instance of the Request class")
        self.url = url
        self.request = request

    def website_title(self, use_internet=False):
        if not self.is_valid_url(self.url):
            raise ValueError(f"Invalid URL: {self.url}")
        
        if not use_internet:
            return "My website title"
        else:
            return self.request.download_page(self.url)

    def is_valid_url(self, url):
        return url.startswith("http://") or url.startswith("https://")

# Example usage
url = "https://www.example.com"
request_obj = Request()
website = Website(url, request_obj)
print(website.website_title(use_internet=True))
