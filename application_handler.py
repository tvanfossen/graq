import ttn

from graq.utils import *

class ApplicationHandler:
    def __init__(self, ttn_app_id, ttn_key, application_id):
        self.ttn_app_id = ttn_app_id
        self.ttn_key = ttn_key
        self.application_id = application_id
        self.app_connect()

    def app_connect(self):
        def uplink_callback(msg, client):
            print("Received uplink from ", msg.dev_id)
            msg_dict = dictify(msg)
            print(msg_dict)
            # Handle message incoming from

        self.handler = ttn.HandlerClient(self.ttn_app_id, self.ttn_key)

        self.mqtt_client = self.handler.data()
        self.mqtt_client.set_uplink_callback(uplink_callback)
        self.mqtt_client.connect()

    def app_close(self):
        self.mqtt_client.close(self)
