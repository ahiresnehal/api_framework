import requests
import json



class Get_res:
    def __init__(self,url):
        self.url = url

    def get_res(self):
        response = requests.get(self.url)
        #print(response)
        #print(response.content)
        return response



        # Display Requests
        #print(response)
        # Display Requests Contenet
        #print(response.content)
        # print Response header
        # print(response.headers)
        # Parse response to JSON format
        #json_response = json.loads(response.text)
        #print(json_response)
        # Fetch value using JSON Path
        #pages = jsonpath.jsonpath(json_response, 'total_pages')
        #print(pages[0])



    #http://restapi.adequateshop.com/api/Tourist?page=2