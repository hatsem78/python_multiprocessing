import asyncio
import time

from core.settings import get_logger

logger = get_logger('ProducerInfo')


class ProducerInfo:

    def __init__(self, site_id, force_flag):
        super(ProducerInfo, self).__init__()
        self.site_id = site_id
        self.FORCE_EMMITION_FLAG = force_flag

    def main(self):
        asyncio.run(self.start_main())

    @staticmethod
    async def start_main():
        # run for ever
        while True:
            # block for a moment
            time.sleep(1)
            # report a message
            print('Task is running', flush=True)
