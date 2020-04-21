"""Eureka http client"""
import urllib

import py_eureka_client.http_client as http_client


# 1. Inherit the `HttpClient` class in `py_eureka_client.http_client`.
class HttpPostClient(http_client.HttpClient):
    """Eureka http post client"""

    # 2. Rewrite the `urlopen` method in your class.
    # If you want to raise an exception, please make sure that the exception is an `urllib.error.HTTPError` or `urllib.error.URLError`
    # (urllib2.HTTPError or urllib2.URLError in python 2), or it may cause some un-handled errors.
    def urlopen(self):
        # The flowing code is the default implementation, you can see what fields you can use. you can change your implementation here
        # res = urllib2.urlopen(self.request, data=self.data, timeout=self.timeout,
        #                       cafile=self.cafile, capath=self.capath,
        #                       cadefault=self.cadefault, context=self.context)
        try:
            response = urllib.request.urlopen(self.request, data=self.data)
        except urllib.error.HTTPError as e:
            print(e)
        except urllib.error.URLError as e:
            print(e)

        return response.getcode()


# 3. Set your class to `py_eureka_client.http_client`.
http_client.set_http_client_class(HttpPostClient)
