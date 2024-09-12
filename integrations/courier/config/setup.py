import environ

class CourierConfigMixin:
    """
    base class to load environment variables for the Courier API
    """
    def __init__(self):
        env = environ.Env()
        self.auth_token = env("COURIER_AUTH_TOKEN")
        self.message_id_map = env.dict(
            'COURIER_MESSAGE_ID_MAP',
            cast={'value': str},
            default={}
        )
        self.headers = {
            'Authorization': f'Bearer {self.auth_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
