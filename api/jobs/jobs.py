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
        # print('doing job')
        get_response = requests.get("https://ims-api-gateway.herokuapp.com/coreservice/api/v1/projects/1/bugs")
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
          "type": "email",
          "applied_template_id": "30"
        }
        headers = {'Content-type': 'application/json; charset=utf-8', 'Accept': 'text/json'}

        post_response = requests.post("https://ims-notification.herokuapp.com/api/v1/notification", data=json.dumps(data))
        # print(post_response)
