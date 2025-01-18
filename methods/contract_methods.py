import re

from data.preinstalled_data import PreInstalledData

from .xml_processor_methods import XmlProcessorMethods


class ContractMethods:
    @staticmethod
    def should_be_response_specified_scheme_and_contain_sign_elements(response, mr):
        XmlProcessorMethods.should_be_response_corresponds_specified_xml_scheme(response, 'xmlsoap_scheme.xsd')
        ContractMethods.should_be_specified_tag_in_response_and_value_equal_specified_pattern(
            response, 'SignatureValue', PreInstalledData.SIGNATURE_VALUE_PATTERN)
        if mr == 2:
            ContractMethods.should_be_specified_tag_in_response_and_value_equal_specified_pattern(
                response, 'X509Certificate', PreInstalledData.X_509_CERTIFICATE_PATTERN)
        else:
            ContractMethods.should_be_specified_tag_in_response_and_value_equal_specified_pattern(
                response, 'BinarySecurityToken', PreInstalledData.BINARY_SECURITY_TOKEN_PATTERN)

    @staticmethod
    def should_be_attachment_signed_if_installed_true(response, need_sign_attachments):
        if need_sign_attachments:
            ContractMethods.should_be_specified_tag_in_response_and_value_equal_specified_pattern(
                response, 'SignaturePKCS7', PreInstalledData.SIGNATURE_PKCS7_PATTERN)
        else:
            ContractMethods.should_not_be_specified_tag_in_response(response, 'SignaturePKCS7')

    @staticmethod
    def should_be_specified_tag_in_response_and_value_equal_specified_pattern(response, tag_name, pattern):
        tag_value = XmlProcessorMethods.get_value_from_response_or_return_false(
            response, tag_name)
        if tag_value:
            assert re.match(pattern, tag_value.replace(' ', '').replace('\n', '')), \
                '\nОтвет не соответствует контракту:' \
                f'\nЗначение элемента подписи: {tag_name} не соответствует регулярному выражению:' \
                f'\nШаблон выражения  : {pattern}' \
                f'\nЗначение элемента : {tag_value}'
        else:
            assert False, \
                "\nОтвет не соответствует контракту:" \
                f"\nXML-файл в ответе от сервиса не содержит элемента подписи : {tag_name}"

    @staticmethod
    def should_not_be_specified_tag_in_response(response, tag_name):
        assert XmlProcessorMethods.should_not_be_present_specified_tag_in_response(response, tag_name), \
            '\nОтвет не соответствует ожидаемому:' \
            f'\nЭлемент подписи вложения : {tag_name} присутствует в ответном XML-файле, однако в этом тесте' \
            '\nустановлено значение для "needSignAttachments": false, и вложение не должно быть подписано.'
