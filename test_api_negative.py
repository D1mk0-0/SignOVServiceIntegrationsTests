import pytest

from data.preinstalled_data import PreInstalledData
from methods.base_methods import BaseMethods
from methods.connect_methods import ConnectMethods
from methods.parameterization_methods import ParameterizationMethods


class TestApiNegative:
    def test_response_xml_authorization_failed_without_header_basic_auth(self):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_not_auth_headers()
        BaseMethods.should_be_status_code_401(response)

    @pytest.mark.parametrize(
        'login, password', ParameterizationMethods.return_incorrect_login_password())
    def test_response_xml_authorization_failed_if_incorrect_log_and_pass(self, login, password):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_specified_auth_headers(
            login, password)
        BaseMethods.should_be_status_code_401(response)

    def test_response_data_authorization_failed_without_header_basic_auth(self):
        response = BaseMethods.send_patch_request_data_and_specified_attributes_with_not_auth_headers()
        BaseMethods.should_be_status_code_401(response)

    @pytest.mark.parametrize(
        'login, password', ParameterizationMethods.return_incorrect_login_password())
    def test_response_data_authorization_failed_if_incorrect_log_and_pass(self, login, password):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_specified_auth_headers(
            login, password)
        BaseMethods.should_be_status_code_401(response)

    @pytest.mark.parametrize(
        'thumbprint, xml_name, need_sign_attachments, mr',
        ParameterizationMethods.return_incorrect_thumbprint_and_after_attributes())
    def test_response_xml_contains_descriptor_error(self, thumbprint, xml_name, need_sign_attachments, mr):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_auth(
            thumbprint, xml_name, need_sign_attachments, mr)
        BaseMethods.should_be_status_code_500(response)
        BaseMethods.should_be_specified_error_message_in_response(response, PreInstalledData.DESCRIPTOR_ERROR)

    @pytest.mark.parametrize(
        'thumbprint, file_name', ParameterizationMethods.return_incorrect_thumbprint_and_file_name())
    def test_data_response_contains_data_signature_error(self, thumbprint, file_name):
        response = BaseMethods.send_patch_request_data_and_specified_thumbprint_and_file_name(thumbprint, file_name)
        BaseMethods.should_be_status_code_500(response)
        BaseMethods.should_be_specified_error_message_in_response(response, PreInstalledData.DESCRIPTOR_ERROR)

    @pytest.mark.parametrize(
        'file_name, need_sign_attachments, mr', ParameterizationMethods.return_incorrect_xml_after_attributes())
    def test_response_xml_contains_an_xml_parsing_error(self, file_name, need_sign_attachments, mr):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_auth(
            ConnectMethods.THUMBPRINT, file_name, need_sign_attachments, mr)
        BaseMethods.should_be_status_code_500(response)
        BaseMethods.should_be_specified_error_message_in_response(response, PreInstalledData.XML_PARSING_ERROR)

    @pytest.mark.parametrize(
        'file_name, need_sign_attachments, mr',
        ParameterizationMethods.return_incorrect_need_sign_attachments_after_attributes())
    def test_response_xml_contains_an_error_signxmldto_dto_parameter(self, file_name, need_sign_attachments, mr):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_auth(
            ConnectMethods.THUMBPRINT, file_name, need_sign_attachments, mr)
        BaseMethods.should_be_status_code_400(response)
        BaseMethods.should_be_specified_error_message_in_response(response, PreInstalledData.SIGNXMLDTO_ERROR)

    @pytest.mark.parametrize(
        'file_name, need_sign_attachments, mr', ParameterizationMethods.return_incorrect_mr_after_attributes())
    def test_response_xml_contains_an_error_mr_version_parameter(self, file_name, need_sign_attachments, mr):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_auth(
            ConnectMethods.THUMBPRINT, file_name, need_sign_attachments, mr)
        BaseMethods.should_be_status_code_500(response)
        BaseMethods.should_be_specified_error_message_in_response(response, PreInstalledData.MP_VERSION_ERROR)

    @pytest.mark.parametrize(
        'data_string', ParameterizationMethods.return_incorrect_data_string())
    def test_data_response_contains_error_not_a_valid_base_64(self, data_string):
        response = BaseMethods.send_patch_request_data_and_specified_thumbprint_and_string(
            ConnectMethods.THUMBPRINT, data_string)
        BaseMethods.should_be_status_code_500(response)
        BaseMethods.should_be_specified_error_message_in_response(response, PreInstalledData.VALID_BASE_64_ERROR)
