from integrations.utils import get_env

class CourierConfigMixin:
    """
    base class to load environment variables for the Courier API
    """
    def __init__(self):
        env = get_env(__file__)
        self.auth_token = env("COURIER_AUTH_TOKEN")
        self.confirmation_template_id = env("COURIER_CONFIRMATION_TEMPLATE_ID")
        self.reminder_template_id = env("COURIER_REMINDER_TEMPLATE_ID")
        self.cancel_template_id = env("COURIER_CANCEL_TEMPLATE_ID")
        self.missed_template_id = env("COURIER_MISSED_TEMPLATE_ID")
        self.thank_you_template_id = env("COURIER_THANK_YOU_TEMPLATE_ID")
        self.headers = {
            'Authorization': f'Bearer {self.auth_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
