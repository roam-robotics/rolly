"""
Minimalistic Rollbar client.
"""
import urllib.request
import functools
import json

ROLLBAR_API = 'https://api.rollbar.com/api/1/item/'


class MissingCredentials(Exception):
    """
    Raise when credentials are missing.
    """


class InvalidData(Exception):
    """
    Raise when data is of the wrong type.
    """


class Polly:
    """
    Thin, credential-holding shell for a Rollbar API request.
    """

    token = None
    environment = None

    def __init__(self, token=None, environment=None):
        if not token or not environment:
            raise MissingCredentials
        self.token = token
        self.environment = environment
        self._register_convenience_functions()

    def _send(self, payload):
        """
        Attach credentials and send the payload to Rollbar.
        """
        request = urllib.request.Request(ROLLBAR_API)
        request.add_header('X-Rollbar-Access-Token', self.token)
        request.add_header('Content-Type', 'application/json; charset=utf-8')
        data = json.dumps(payload).encode('utf-8')
        with urllib.request.urlopen(request, data) as url:
            response = url.read()
        return json.loads(response)

    def log(self, message, level='debug', data=None):
        """
        Generic log message.
        """
        if data and not isinstance(data, dict):
            raise InvalidData('data must be a dictionary')
        payload = {
            'data': {
                'environment': self.environment,
                'level': level,
                'body': {
                    'message': {
                        'body': message
                    }
                }
            }
        }
        if data:
            payload['data']['body']['message'].update(data)
        return self._send(payload)

    def _register_convenience_functions(self):
        self.critical = functools.partial(self.log, level='critical')
        self.warning = functools.partial(self.log, level='warning')
        self.error = functools.partial(self.log, level='error')
        self.debug = functools.partial(self.log, level='debug')
        self.info = functools.partial(self.log, level='info')
        self.fatal = self.critical
