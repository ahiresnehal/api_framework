import requests
import json
from pageobjects.delete_resource import Del_res
from pageobjects.get_resource import Get_res
from pageobjects.post_resource import Post_res
from pageobjects.put_resource import Put_res
from utilities.customLogger import LogGen

with open('/home/snehal/PycharmProjects/api_framework/configurations/config.json', "r") as f1:
    data = json.load(f1)

GET_URL = data["getURL"]
POST_URL = data["postURL"]
PUT_URL = data["putURL"]
DELETE_URL = data["deleteURL"]


logger = LogGen.loggen()


def test_get_001():
    logger.info("***************Test_get_001****************")
    logger.info("*************Verifying status code********************")
    g = Get_res(GET_URL)
    response=g.get_res()
    print(response)
    print(type(response))
    print(response.status_code)
    assert response.status_code == 200


def test_get_002():
    logger.info("***************Test_get_002****************")
    logger.info("*************Verifying reason********************")
    g = Get_res(GET_URL)
    response = g.get_res()
    print(response.reason)
    assert response.reason == "OK"

def test_post_001():
    logger.info("***************Test_post_001****************")
    logger.info("*************Verifying content-length********************")
    po = Post_res(POST_URL)
    response = po.post_res()
    print(response.status_code)
    assert response.status_code == 201

def test_post_002():
    logger.info("***************Test_post_002****************")
    logger.info("*************Verifying text corresponding to the status code********************")
    po = Post_res(POST_URL)
    response = po.post_res()
    print(response.status_code)
    assert response.status_code == 201

def test_put_001():
    logger.info("***************Test_put_001****************")
    logger.info("*************Verifying status code********************")
    pu = Put_res("https://reqres.in/api/users/2")
    response = pu.put_res()
    assert response.status_code == 200

def test_put_002():
    logger.info("***************Test_put_002****************")
    logger.info("*************verifying response is redirected or not********************")
    pu = Put_res(PUT_URL)
    response = pu.put_res()
    print(response.status_code)
    assert response.status_code == 200

def test_del_001():
    logger.info("***************Test_del_001****************")
    logger.info("*************Verifying status code********************")
    d = Del_res(DELETE_URL)
    response = d.del_res()
    print(response.status_code)
    assert response.status_code == 204

def test_del_002():
    logger.info("***************Test_del_002****************")
    logger.info("*************Verifying status code is less than 400 or not********************")
    d = Del_res(DELETE_URL)
    response = d.del_res()
    print(response.ok)
    assert response.ok == True