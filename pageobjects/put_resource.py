
import requests
import json


class Put_res:
    def __init__(self,url):
        self.url = url

    def put_res(self):

        # Read input json file
        file = open('/home/snehal/PycharmProjects/api_framework/testData/new.json')
        json_input = file.read()
        request_json = json.loads(json_input)

        # Make put request with json input body
        response = requests.put(self.url, request_json)


        return response






