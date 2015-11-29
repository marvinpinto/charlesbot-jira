import asynctest
from asynctest.mock import patch


class TestJira(asynctest.TestCase):

    def setUp(self):
        patcher1 = patch('charlesbot_jira.jira.Jira.load_config')  # NOQA
        self.addCleanup(patcher1.stop)
        self.mock_load_config = patcher1.start()

        from charlesbot_jira.jira import Jira
        test_plug = Jira()  # NOQA

    def tearDown(self):
        pass

    @asynctest.ignore_loop
    def test_something(self):
        pass
