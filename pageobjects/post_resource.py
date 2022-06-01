import requests
import json

class Post_res:
    def __init__(self,url):
        self.url = url

    def post_res(self):

        # read Input JSON file
        file = open("/home/snehal/PycharmProjects/api_framework/testData/new.json", 'r')
        json_input = file.read()
        request_json = json.loads(json_input)

        # print(request_json)

        response = requests.post(self.url, request_json)
        return response





