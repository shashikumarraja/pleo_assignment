"""
contains load tests for app.py module apis
"""
import os
import json
from locust import HttpLocust, TaskSet, task, events

class FormatMoney(TaskSet):
    """ Contains task set which are single-stage i.e non-conversation queries """

    def on_start(self):
        pass

    def validate_response(self, response):
        if response.status_code in [200]:
            response.success()
        else:
            response.failure("%d Error code" % (response.status_code))

    @task()
    def test_format_money_api(self):
        with self.client.get(self.locust.host, catch_response=True, timeout=10) as response:
            self.validate_response(response)

class TestLoad(HttpLocust):
    task_set = FormatMoney
    # the minimum and maximum time respectively, in milliseconds, that a simulated user will wait between executing each task
    min_wait = int(os.environ['min_wait']) if 'min_wait' in os.environ else 1
    max_wait = int(os.environ['max_wait']) if 'max_wait' in os.environ else 1