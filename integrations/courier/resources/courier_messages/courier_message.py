import json
from integrations.base import APIRequest
from integrations.courier.config import CourierConfigMixin

class CourierMessage(CourierConfigMixin, APIRequest):

    def __init__(self, payload_type=None, payload_data={}, message_type=None):
        super().__init__()
        self.payload_type = payload_type
        self.payload_data = payload_data
        self.message_type = message_type
        self.body = None
        self.get_payload_via_payload_type()

    def get_payload_via_payload_type(self):        
        json_text = ''

        with open(f'integrations/courier/resources/courier_messages/message_payloads/{self.payload_type}.json', 'r') as file:
            json_text = file.read()

            for k in self.payload_data.keys():
                json_text = json_text.replace(f"[{k}]", self.payload_data[k])
            json_text = json_text.replace("[TEMPLATE_ID]", self.message_id_map[self.message_type])
        self.body = json.loads(json_text)
        print(self.body)

        return self.body

    def send_courier_automation(self):
        url = 'https://api.courier.com/automations/invoke'
        self.call_api(url, 'POST', headers=self.headers, body=self.body)

    def send_courier_message(self):
        url = 'https://api.courier.com/send'
        self.call_api(url, 'POST', headers=self.headers, body=self.body)
