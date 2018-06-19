class DataHandler:
    from pg import DB

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
                self.dev_id = msg['dev_id']
                self.timestamp = msg['metadata']['time']

                if self.check_field(self.dev_id, "dev_id") == 0:
                    # if the device exists, check if the same timestamp already exists
                    if self.check_field(self.timestamp, "time") == 1:
                        print("device present and timestamp is new ")
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
                    # Based on OST naming conventions as UoM and Simms can be modified going into it

    def create_new_entry(self, msg):
        print("creating new table for device")


    def push(self, entry):
        print("placeholder push to sql database")

    def check_field(self, field, type):
        if type == "dev_id":
            print("Check if table for device exists")
        elif type == "time":
            print("check if timestamp for self.dev_id exists")
        else:
            print("Checking standard fields of device id")
        return 1




# end