import threading, time, json, urllib, requests

from api.http_clients.http_post_client import HttpPostClient

import py_eureka_client.eureka_client as eureka_client

class Job:
    """Parent class for all jobs"""
    def do_job(self):
        pass

class JobCoreService(Job):
    """Job for core service"""
    def do_job(self):
        print('doing job')
        # response = eureka_client.do_service_async("CORESERVICE", "api/v1/projects/1/bugs",
        #                             on_success= success_callback, on_error=error_callback)
        get_response = requests.get("https://ims-core-service.herokuapp.com/api/v1/projects/1/bugs")
        # for i in response.json():
        #     print(i)
        num_of_bugs = f"{len(get_response.json())}"
        data = {
          "user_uuid": ["253535GDF"],
          "body": [
            {
                "year": "2019",
                "TotalnumOfBugsCreated": num_of_bugs,
                "monthsOfTheYear": {
                    "december": num_of_bugs
                }
            }
          ],
          "type": ["email"],
          "applied_template_id": "30"
        }
        headers = {'Content-type': 'application/json; charset=utf-8', 'Accept': 'text/json'}

        # with open("api/jobs/dummy.json", "r") as f:
        #     data["body"]  = f.read()

        post_response = requests.post("https://ims-notification.herokuapp.com/api/v1/notifications", data=json.dumps(data), headers=headers)
        # try
        #     res = eureka_client.do_service("NOTIFICATION", "/api/v1/notifications", prefer_https=HttpPostClient, data=data)
        #     print("http status code" + res)
        # except requests.exceptions. as e:
        #     print(e)
        # print(json.dumps(data))
        print(post_response.raise_for_status)


def success_callback(data):
    print(data)
    # with open("dummy.json", "w") as f:
    #     print(f.read())

def error_callback(error):
    print(error)
