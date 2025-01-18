from .connect_methods import ConnectMethods


class ParameterizationMethods:
    @staticmethod
    def return_valid_xml_data_for_contract_test():
        return [
            ('AckRequest.xml', True, 0),
            ('AckRequest.xml', True, 1),
            ('AckRequest.xml', True, 2),
            ('AckRequest.xml', False, 0),
            ('AckRequest.xml', False, 1),
            ('AckRequest.xml', False, 2),
            ('AckRequestWithSign.xml', True, 0),
            ('AckRequestWithSign.xml', True, 1),
            ('AckRequestWithSign.xml', True, 2),
            ('AckRequestWithSign.xml', False, 0),
            ('AckRequestWithSign.xml', False, 1),
            ('AckRequestWithSign.xml', False, 2),
            ('GetRequestRequest.xml', True, 0),
            ('GetRequestRequest.xml', True, 1),
            ('GetRequestRequest.xml', True, 2),
            ('GetRequestRequest.xml', False, 0),
            ('GetRequestRequest.xml', False, 1),
            ('GetRequestRequest.xml', False, 2),
            ('GetRequestRequestWithSign.xml', True, 0),
            ('GetRequestRequestWithSign.xml', True, 1),
            ('GetRequestRequestWithSign.xml', True, 2),
            ('GetRequestRequestWithSign.xml', False, 0),
            ('GetRequestRequestWithSign.xml', False, 1),
            ('GetRequestRequestWithSign.xml', False, 2),
            ('GetRequestResponse.xml', True, 2),
            ('GetRequestResponse.xml', False, 2),
            ('GetRequestResponseWithSign.xml', True, 2),
            ('GetRequestResponseWithSign.xml', False, 2),
            ('GetResponseRequest.xml', True, 0),
            ('GetResponseRequest.xml', True, 1),
            ('GetResponseRequest.xml', True, 2),
            ('GetResponseRequest.xml', False, 0),
            ('GetResponseRequest.xml', False, 1),
            ('GetResponseRequest.xml', False, 2),
            ('GetResponseRequestWithSign.xml', True, 0),
            ('GetResponseRequestWithSign.xml', True, 1),
            ('GetResponseRequestWithSign.xml', True, 2),
            ('GetResponseRequestWithSign.xml', False, 0),
            ('GetResponseRequestWithSign.xml', False, 1),
            ('GetResponseRequestWithSign.xml', False, 2),
            ('SendRequestRequest.xml', True, 0),
            ('SendRequestRequest.xml', True, 1),
            ('SendRequestRequest.xml', True, 2),
            ('SendRequestRequest.xml', False, 0),
            ('SendRequestRequest.xml', False, 1),
            ('SendRequestRequest.xml', False, 2),
            ('SendRequestRequestWithSign.xml', True, 0),
            ('SendRequestRequestWithSign.xml', True, 1),
            ('SendRequestRequestWithSign.xml', True, 2),
            ('SendRequestRequestWithSign.xml', False, 0),
            ('SendRequestRequestWithSign.xml', False, 1),
            ('SendRequestRequestWithSign.xml', False, 2),
            ('SendResponseRequest.xml', True, 0),
            ('SendResponseRequest.xml', True, 1),
            ('SendResponseRequest.xml', True, 2),
            ('SendResponseRequest.xml', False, 0),
            ('SendResponseRequest.xml', False, 1),
            ('SendResponseRequest.xml', False, 2),
            ('SendResponseRequestWithSign.xml', True, 0),
            ('SendResponseRequestWithSign.xml', True, 1),
            ('SendResponseRequestWithSign.xml', True, 2),
            ('SendResponseRequestWithSign.xml', False, 0),
            ('SendResponseRequestWithSign.xml', False, 1),
            ('SendResponseRequestWithSign.xml', False, 2)
        ]

    @staticmethod
    def return_valid_xml_data_with_attach_for_contract_test():
        return [
            ('SendRequestRequestAttachCONTENT.xml', 'file_100kb_size', True, 2),
            ('SendRequestRequestAttachCONTENT.xml', 'file_1mb_size', True, 2),
            ('SendRequestRequestAttachCONTENT.xml', 'file_5mb_size', True, 2),
            ('SendRequestRequestAttachCONTENT.xml', 'file_100kb_size', False, 2),
            ('SendRequestRequestAttachCONTENT.xml', 'file_1mb_size', False, 2),
            ('SendRequestRequestAttachCONTENT.xml', 'file_5mb_size', False, 2),
            ('SendResponseRequestAttachCONTENT.xml', 'file_100kb_size', True, 2),
            ('SendResponseRequestAttachCONTENT.xml', 'file_1mb_size', True, 2),
            ('SendResponseRequestAttachCONTENT.xml', 'file_5mb_size', True, 2),
            ('SendResponseRequestAttachCONTENT.xml', 'file_100kb_size', False, 2),
            ('SendResponseRequestAttachCONTENT.xml', 'file_1mb_size', False, 2),
            ('SendResponseRequestAttachCONTENT.xml', 'file_5mb_size', False, 2)
        ]

    @staticmethod
    def return_incorrect_login_password():
        return [
            ('incorrectlogin', ConnectMethods.BASIC_AUTH_PASSWORD),
            (ConnectMethods.BASIC_AUTH_USER, 'incorrectpassword'),
            (ConnectMethods.BASIC_AUTH_USER.upper(), ConnectMethods.BASIC_AUTH_PASSWORD),
            (ConnectMethods.BASIC_AUTH_USER, ConnectMethods.BASIC_AUTH_PASSWORD.upper())
        ]

    @staticmethod
    def return_incorrect_thumbprint_and_after_attributes():
        return [
            ('1200644d4d43d17d931ae9e5d6000200644d4d', 'AckRequest.xml', True, 2),
            ('1200644d4d43d17d931ae9e5d6000200644d4d', 'AckRequest.xml', False, 2),
            ('', 'AckRequest.xml', True, 2),
            ('', 'AckRequest.xml', False, 2)
        ]

    @staticmethod
    def return_incorrect_thumbprint_and_file_name():
        return [
            ('1200644d4d43d17d931ae9e5d6000200644d4d', 'file_100kb_size'),
            ('', 'file_100kb_size')
        ]

    @staticmethod
    def return_incorrect_xml_after_attributes():
        return [
            ('invalid_format_file_empty.txt', True, 2),
            ('invalid_format_file_empty.txt', True, 1),
            ('invalid_format_file_empty.txt', True, 0),
            ('invalid_format_file_empty.txt', False, 2),
            ('invalid_format_file_empty.txt', False, 1),
            ('invalid_format_file_empty.txt', False, 0),
            ('invalid_format_file_json.json', True, 2),
            ('invalid_format_file_json.json', True, 1),
            ('invalid_format_file_json.json', True, 0),
            ('invalid_format_file_json.json', False, 2),
            ('invalid_format_file_json.json', False, 1),
            ('invalid_format_file_json.json', False, 0),
        ]

    @staticmethod
    def return_incorrect_need_sign_attachments_after_attributes():
        return [
            ('AckRequest.xml', -1, 2),
            ('AckRequest.xml', 3, 1),
            ('AckRequest.xml', 'string', 0),
            ('AckRequest.xml', [], 0)
        ]

    @staticmethod
    def return_incorrect_mr_after_attributes():
        return [
            ('AckRequest.xml', True, -1),
            ('AckRequest.xml', True, 3),
            ('AckRequest.xml', False, -1),
            ('AckRequest.xml', False, 3)
        ]

    @staticmethod
    def return_incorrect_data_string():
        return [
            'incorrect_data_string'
        ]

    @staticmethod
    def return_correct_file_name():
        return [
            'file_5mb_size',
            'file_1mb_size',
            'file_100kb_size'
        ]
