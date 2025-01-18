import os

from data.json_request_data import JsonRequestData

from .base64_processor_methods import Base64ProcessorsMethods
from .connect_methods import ConnectMethods
from .request_send_methods import RequestSendMethods
from .xml_processor_methods import XmlProcessorMethods


class BaseMethods:
    @staticmethod
    def send_patch_request_xml_and_specified_attributes_with_auth(thumbprint, xml_name, need_sign_attachments, mr):
        json_body = JsonRequestData.return_json_body_sign_xml(
            thumbprint, BaseMethods.get_path_and_read_file(xml_name), need_sign_attachments, mr)
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json(
            ConnectMethods.PATCH_URL_XML, json_body)
        return response

    @staticmethod
    def send_patch_request_xml_and_specified_attributes_with_not_auth_headers():
        json_body = JsonRequestData.return_json_body_sign_xml(
            ConnectMethods.THUMBPRINT, BaseMethods.get_path_and_read_file('AckRequest.xml'), False, 2)
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json_with_not_auth(
            ConnectMethods.PATCH_URL_XML, json_body)
        return response

    @staticmethod
    def send_patch_request_data_and_specified_attributes_with_not_auth_headers():
        json_body = JsonRequestData.return_json_body_sign_data(
            ConnectMethods.THUMBPRINT, Base64ProcessorsMethods.return_file_base64_string('file_100kb_size'))
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json_with_not_auth(
            ConnectMethods.PATCH_URL_DATA, json_body)
        return response

    @staticmethod
    def send_patch_request_xml_and_specified_attributes_with_specified_auth_headers(login, password):
        json_body = JsonRequestData.return_json_body_sign_xml(
            ConnectMethods.THUMBPRINT, BaseMethods.get_path_and_read_file('AckRequest.xml'), False, 2)
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json_with_specified_log_and_pass(
            ConnectMethods.PATCH_URL_XML, json_body, login, password)
        return response

    @staticmethod
    def send_patch_request_data_and_specified_attributes_with_specified_auth_headers(login, password):
        json_body = JsonRequestData.return_json_body_sign_data(
            ConnectMethods.THUMBPRINT, Base64ProcessorsMethods.return_file_base64_string('file_100kb_size'))
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json_with_specified_log_and_pass(
            ConnectMethods.PATCH_URL_DATA, json_body, login, password)
        return response

    @staticmethod
    def send_patch_request_xml_and_specified_attributes_and_attach_file_with_auth(
            thumbprint, xml_name, file_name, need_sign_attachments, mr):
        xml_file = XmlProcessorMethods.replace_value_in_xml_document(
            xml_name, 'Content', Base64ProcessorsMethods.return_file_base64_string(file_name))
        json_body = JsonRequestData.return_json_body_sign_xml(
            thumbprint, xml_file, need_sign_attachments, mr)
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json(
            ConnectMethods.PATCH_URL_XML, json_body)
        return response

    @staticmethod
    def send_patch_request_data_and_specified_thumbprint_and_file_name(thumbprint, file_name):
        json_body = JsonRequestData.return_json_body_sign_data(
            thumbprint, Base64ProcessorsMethods.return_file_base64_string(file_name))
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json(
            ConnectMethods.PATCH_URL_DATA, json_body)
        return response

    @staticmethod
    def send_patch_request_data_and_specified_thumbprint_and_string(thumbprint, data_string):
        json_body = JsonRequestData.return_json_body_sign_data(thumbprint, data_string)
        response = RequestSendMethods.send_patch_request_with_specified_url_and_json(
            ConnectMethods.PATCH_URL_DATA, json_body)
        return response

    @staticmethod
    def should_be_status_code_200(response):
        assert response.status_code == 200, \
            '\nСтатус ответа не в порядке:' \
            f'\nВ этом тесте статус ответа: {response.status_code}' \
            '\nОжидаемое значение 200' \
            '\nСодержание ответа:' \
            f'\n{response.text}'

    @staticmethod
    def should_be_status_code_400(response):
        assert response.status_code == 400, \
            '\nСтатус ответа не в порядке:' \
            f'\nВ этом тесте статус ответа: {response.status_code}' \
            '\nОжидаемое значение 400' \
            '\nСодержание ответа:' \
            f'\n{response.text}'

    @staticmethod
    def should_be_status_code_401(response):
        assert response.status_code == 401, \
            '\nСтатус ответа не в порядке:' \
            f'\nВ этом тесте статус ответа: {response.status_code}' \
            '\nОжидаемое значение 401'

    @staticmethod
    def should_be_status_code_500(response):
        assert response.status_code == 500, \
            '\nСтатус ответа не в порядке:' \
            f'\nВ этом тесте статус ответа: {response.status_code}' \
            '\nОжидаемое значение 500' \
            '\nСодержание ответа:' \
            f'\n{response.text}'

    @staticmethod
    def should_be_specified_error_message_in_response(response, error_message):
        assert error_message in response.text, \
            '\nОписание характера ошибки в ответе не в порядке:' \
            f'\nОжидалось, что описание будет включать подстроку: {error_message} ' \
            '\nОднако в ответе представлено:' \
            f'\n{response.text}'

    @staticmethod
    def should_be_not_empty_string_in_response(response):
        assert len(response.text) > 0, \
            '\nС подписью файла что-то не в порядке:' \
            f'\nОжидалось, что ответом будет файл CryptoPro в специфичной кодировке,' \
            '\nоднако в ответе не вернулось ничего.'

    @staticmethod
    def get_path_and_read_file(file_name):
        file_path = os.path.join(
            os.getcwd(), 'data', 'files_data', file_name)
        with open(file_path, encoding='utf-8') as file:
            return file.read()
