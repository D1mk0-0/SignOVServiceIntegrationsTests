class PreInstalledData:
    # Шаблоны
    SIGNATURE_VALUE_PATTERN = r'^[a-zA-Z0-9/+/=//]{80,100}$'
    X_509_CERTIFICATE_PATTERN = r'^[a-zA-Z0-9/+/=//]'
    BINARY_SECURITY_TOKEN_PATTERN = r'^[a-zA-Z0-9/+/=//]'
    SIGNATURE_PKCS7_PATTERN = r'^[a-zA-Z0-9/+/=//]'

    # Ошибки
    DESCRIPTOR_ERROR = 'Ошибка при получении дескриптора сертификата'
    XML_PARSING_ERROR = 'Ошибка при парсинге XML содержимого в запросе'
    SIGNXMLDTO_ERROR = 'Failed to read parameter "SignXmlDto dto"'
    MP_VERSION_ERROR = 'Неподдерживаемая версия МР'
    VALID_BASE_64_ERROR = 'The input is not a valid Base-64 string'
