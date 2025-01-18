import os

import xmlschema
from lxml import etree


class XmlProcessorMethods:
    @staticmethod
    def should_be_response_corresponds_specified_xml_scheme(response, xml_scheme):
        xml_scheme_path = os.path.join(os.getcwd(), 'data', 'scheme_data', xml_scheme)
        schema_file = open(xml_scheme_path)
        xml_data = etree.XML(response.content)
        with open('response.xml', 'wb') as file:
            file.write(etree.tostring(
                xml_data, xml_declaration=True, encoding='utf-8', pretty_print=True))
        xml_response_path = os.path.join(os.getcwd(), 'response.xml')
        schema = xmlschema.XMLSchema(schema_file)
        assert schema.is_valid(xml_response_path), \
            "\nОтвет не соответствует контракту:" \
            f"\nXML-файл в ответе от сервиса не соответствует указанной XML-схеме: {xml_scheme}"
        os.remove(xml_response_path)

    @staticmethod
    def get_value_from_response_or_return_false(response, resulting_value):
        xml_document = response.text
        root = etree.fromstring(xml_document.encode('utf-8'))
        value = root.find('.//{*}' + resulting_value)
        if value is not None:
            return value.text
        else:
            return False

    @staticmethod
    def should_not_be_present_specified_tag_in_response(response, resulting_value):
        xml_document = response.text
        root = etree.fromstring(xml_document.encode('utf-8'))
        value = root.find('.//{*}' + resulting_value)
        if value is None:
            return True
        else:
            return False

    @staticmethod
    def replace_value_in_xml_document(xml_name, element_name, new_value):
        xml_file_path = os.path.join(os.getcwd(), 'data', 'files_data', xml_name)
        tree = etree.parse(xml_file_path)
        elements = tree.xpath(f'//*[local-name()="{element_name}"]')
        for element in elements:
            element.text = new_value
        return etree.tostring(tree, encoding='utf-8', xml_declaration=True).decode('utf-8')
