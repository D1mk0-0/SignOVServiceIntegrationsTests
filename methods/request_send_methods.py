import requests

from .connect_methods import ConnectMethods


class RequestSendMethods:
    auth = (ConnectMethods.BASIC_AUTH_USER, ConnectMethods.BASIC_AUTH_PASSWORD)

    @staticmethod
    def send_patch_request_with_specified_url_and_json(url, json_body):
        response = requests.patch(url, json=json_body, auth=RequestSendMethods.auth)
        return response

    @staticmethod
    def send_patch_request_with_specified_url_and_json_with_not_auth(url, json_body):
        response = requests.patch(url, json=json_body)
        return response

    @staticmethod
    def send_patch_request_with_specified_url_and_json_with_specified_log_and_pass(url, json_body, login, password):
        auth = (login, password)
        response = requests.patch(url, json=json_body, auth=auth)
        return response
