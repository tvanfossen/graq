import threading
import time

from queue import Queue
from utils import *
from graq.application_handler import ApplicationHandler

app_id = "grand_rapids_air_quality"
access_key = "ttn-account-v2.gt9fpNCFxGWjTaVYOFZexj3XMElpbnVSrShVdTlC1Ho"


if __name__ == "__main__":
    q = Queue()

    threading.Thread(name="welcome msg", target=display_terminal_welcome).start()

    ost_app_id = "grand_rapids_air_quality"
    ost_access_key = "ttn-account-v2.gt9fpNCFxGWjTaVYOFZexj3XMElpbnVSrShVdTlC1Ho"

    app_handler = ApplicationHandler(ost_app_id, ost_access_key, "ost AQ application")

    while 1:
        time.sleep(1)
        ret = prompt_parser(input("GRLora:\t"))


