import os


class ConnectMethods:
    BASE_API_URL = os.environ.get('BASE_API_URL') or ''
    PATCH_URL_XML = 'http://' + BASE_API_URL + '/api/sign/xml'
    PATCH_URL_DATA = 'http://' + BASE_API_URL + '/api/sign/data'

    BASIC_AUTH_USER = os.environ.get('BASIC_AUTH_USER') or ''
    BASIC_AUTH_PASSWORD = os.environ.get('BASIC_AUTH_PASSWORD') or ''

    THUMBPRINT = os.environ.get('THUMBPRINT') or ''
