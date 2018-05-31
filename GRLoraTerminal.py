import threading
import time

from queue import Queue
from graq.utils import *
from graq.application_handler import ApplicationHandler
from graq.data_handler import DataHandler

app_id = "grand_rapids_air_quality"
access_key = "ttn-account-v2.gt9fpNCFxGWjTaVYOFZexj3XMElpbnVSrShVdTlC1Ho"


def worker(app_id, key, app_name, q):
    app_handler = ApplicationHandler(app_id, key, app_name, q)


def database_worker(q):
    data_handler = DataHandler(q)


def default_start(q):
    ost_app_id = "grand_rapids_air_quality"
    ost_access_key = "ttn-account-v2.gt9fpNCFxGWjTaVYOFZexj3XMElpbnVSrShVdTlC1Ho"

    # Hard code more as needed
    threading.Thread(name="ost AQ app", target=worker, args=(ost_app_id, ost_access_key, "ost_application", q)).start()

    threading.Thread(name="data handler", target=database_worker, args=(q,)).start()


if __name__ == "__main__":
    q = Queue()
    threading.Thread(name="welcome msg", target=display_terminal_welcome).start()

    default_start(q)

    while 1:
        time.sleep(1)
        ret = prompt_parser(input("GRLora:\t"))


