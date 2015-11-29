from charlesbot.base_plugin import BasePlugin
from charlesbot.config import configuration
import asyncio


class Jira(BasePlugin):

    def __init__(self):
        super().__init__("Jira")
        self.load_config()

    def load_config(self):  # pragma: no cover
        config_dict = configuration.get()
        self.token = config_dict['jira']['config_key']

    def get_help_message(self):
        help_msg = []
        help_msg.append("!command - Does a really neat thing!")
        return "\n".join(help_msg)

    @asyncio.coroutine
    def process_message(self, message):
        self.log.info("Processing message %s" % message)
