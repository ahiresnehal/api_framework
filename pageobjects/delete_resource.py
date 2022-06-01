import requests

class Del_res():
    def __init__(self,url):
        self.url = url

    def del_res(self):
        response = requests.delete(self.url)
        return response






