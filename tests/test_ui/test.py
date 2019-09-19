import pytest

@pytest.mark.usefixtures('driver_init')
class BasicTest:
    pass


class Test_URL(BasicTest):
    def test_open_url(self):
        self.driver.get("http://0.0.0.0:5000/")
        print(self.driver.title)
        assert self.driver.title == 'Format Number'
