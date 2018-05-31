class DataHandler:
    def __init__(self, q, ):
        self.q = q

        while 1:
            msg = q.get()
            print(msg)
            # dev_id, port, metadata, payload_fields

            # Parse queue message

            if msg['port'] == 1:
                # sensor readings, diagnostic, confirm GPS location/update GPS location
                print("checking sensor diagnostic")
                dev_id = msg['dev_id']
                timestamp = msg['metadata']['time']

                if self.check_field(dev_id, "dev_id") == 0:
                    # if the device exists, check if the same timestamp already exists
                    if self.check_field(timestamp, "time") == 1:
                        print("device already present an")
                    else:
                        # Assume the entry is a duplicate and discard
                        print("Discard msg")
                else:
                    # create new entry for device
                    print("placeholder for push")
                    self.create_new_entry(msg)

            elif msg['port'] == 2:
                # Reading actual data from sensor
                print("Reading actual data")
                dev_id = msg['dev_id']
                timestamp = msg['metadata']['time']
                for i in msg['payload_fields']:
                    print("checking: " + i)
                    # Check all fields against data in SQL server

                    # Need to create standardized naming conventions for database

    def create_new_entry(self, msg):
        print("creating new entry")

    def push(self, entry):
        print("placeholder push")

    def check_field(self, field, type):
        return 1

    def OST_handler(self):
        


# end