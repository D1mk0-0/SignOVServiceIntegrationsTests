import pytest

from data.preinstalled_data import PreInstalledData
from methods.base_methods import BaseMethods
from methods.connect_methods import ConnectMethods
from methods.contract_methods import ContractMethods
from methods.parameterization_methods import ParameterizationMethods


class TestApiContract:
    @pytest.mark.parametrize(
        'xml_name, need_sign_attachments, mr',
        ParameterizationMethods.return_valid_xml_data_for_contract_test())
    def test_xml_response_corresponds_to_contract(self, xml_name, need_sign_attachments, mr):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_with_auth(
            ConnectMethods.THUMBPRINT, xml_name, need_sign_attachments, mr)
        BaseMethods.should_be_status_code_200(response)
        ContractMethods.should_be_response_specified_scheme_and_contain_sign_elements(response, mr)

    @pytest.mark.parametrize(
        'xml_name, attach_name, need_sign_attachments, mr',
        ParameterizationMethods.return_valid_xml_data_with_attach_for_contract_test())
    def test_xml_response_with_attachments_corresponds_to_contract(
            self, xml_name, attach_name, need_sign_attachments, mr):
        response = BaseMethods.send_patch_request_xml_and_specified_attributes_and_attach_file_with_auth(
            ConnectMethods.THUMBPRINT, xml_name, attach_name, need_sign_attachments, mr)
        BaseMethods.should_be_status_code_200(response)
        ContractMethods.should_be_response_specified_scheme_and_contain_sign_elements(response, mr)
        ContractMethods.should_be_attachment_signed_if_installed_true(response, need_sign_attachments)

    @pytest.mark.parametrize(
        'file_name', ParameterizationMethods.return_correct_file_name())
    def test_data_response_corresponds_to_contract(self, file_name):
        response = BaseMethods.send_patch_request_data_and_specified_thumbprint_and_file_name(
            ConnectMethods.THUMBPRINT, file_name)
        BaseMethods.should_be_status_code_200(response)
        BaseMethods.should_be_not_empty_string_in_response(response)
