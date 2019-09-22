"""
contains load tests for app.py module apis
"""
import os
import random
import logging
from locust import HttpLocust, TaskSet, task
import hypothesis.strategies as st

logger = logging.getLogger(__name__)

class FormatMoney(TaskSet):
    """ Contains task set to be executed with a specific weight of distribution during load test """

    def on_start(self):
        pass

    def validate_response(self, response):
        if response.status_code in [200]:
            response.success()
        else:
            logger.error(response.url)
            response.failure("%d Error code" % (response.status_code))

    @task(50)
    def test_home_api(self):
        with self.client.get(self.locust.host, catch_response=True, timeout=10) as response:
            self.validate_response(response)

    @task(50)
    def test_format_money_api(self):
        number = random.choice(
            [st.floats(allow_nan=False).example(), st.integers().example()])
        with self.client.get(self.locust.host + '/format_money?number=%s' % number, catch_response=True, timeout=10) as response:
            self.validate_response(response)


class TestLoad(HttpLocust):
    task_set = FormatMoney
    # the minimum and maximum time respectively, in milliseconds, that a simulated user will wait between executing each task
    min_wait = int(os.environ['min_wait']) if 'min_wait' in os.environ else 1
    max_wait = int(os.environ['max_wait']) if 'max_wait' in os.environ else 1
