import threading
import time
import ttn

from queue import Queue
from utils import *

app_id = "grand_rapids_air_quality"
access_key = "ttn-account-v2.gt9fpNCFxGWjTaVYOFZexj3XMElpbnVSrShVdTlC1Ho"


def data_pipe():
    print()


if __name__ == "__main__":
    q = Queue()

    threading.Thread(name="welcome msg", target=display_terminal_welcome).start()

    while 1:
        time.sleep(1)
        ret = prompt_parser(input("GRLora:\t"))


