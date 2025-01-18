class JsonRequestData:
    @staticmethod
    def return_json_body_sign_xml(thumbprint, xml_body, sign_attachment, mr):
        return {
            "thumbprint": thumbprint,
            "xml": xml_body,
            "needSignAttachments": sign_attachment,
            "mr": mr
        }

    @staticmethod
    def return_json_body_sign_data(thumbprint, data):
        return {
            "thumbprint": thumbprint,
            "data": data
        }
