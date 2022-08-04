import asyncio
import sys
import threading
from multiprocessing import Process
from core.settings import get_logger

logger = get_logger('JobThread')


class ProgramKilled(Exception):
    pass


def signal_handler(signum, frame):
    raise ProgramKilled


class JobThread(Process):
    """
          Class Job that launches the new tasks and gets its status
          ...
          Attributes
          ----------
          execute: obj: required
            execute represents the function to be executed in each process
      """

    def __init__(self, name, execute, *args, **kwargs) -> None:
        super().__init__(name, args, kwargs)
        self.killed = False
        self.name = name
        self.daemon = False
        self.stopped = threading.Event()
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        """stop cancels the processes and waits for all to finish"""
        self.stopped.set()
        return "termino"

    def run(self):
        """wait to execute again that all processes have been terminated in case of any error"""
        if self.killed:
            sys.exit(1)
        else:
            self.execute()

    def start(self):
        self.__run_backup = self.run
        self.run = self.__run
        threading.Thread.start(self)

    def __run(self):
        self.__run_backup()
        self.run = self.__run_backup

    def globaltrace(self, frame, event, arg):
        if event == 'call':
            return self.localtrace
        else:
            return None

    def localtrace(self, frame, event, arg):
        if self.killed:
            if event == 'line':
                raise SystemExit()
        return self.localtrace

    def kill(self):
        self.killed = True


class JobThreads(threading.Thread):
    """
          Class Job that launches the new tasks and gets its status
          ...
          Attributes
          ----------
          execute: obj: required
            execute represents the function to be executed in each process
      """

    def __init__(self, name, execute, *args, **kwargs) -> None:
        threading.Thread.__init__(self)
        super().__init__(*args, **kwargs)
        self._stop_event = threading.Event()
        self.name = name
        self.daemon = False
        self._stop_event = threading.Event()
        self.execute = execute
        self.args = args
        self.kwargs = kwargs

    def stop(self):
        """stop cancels the processes and waits for all to finish"""
        self._stop_event.set()

    def stopped(self):
        return self._stop_event.is_set()

    def run(self):
        """wait to execute again that all processes have been terminated in case of any error"""
        asyncio.run(self.execute())
