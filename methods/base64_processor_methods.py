import base64
import os


class Base64ProcessorsMethods:
    @staticmethod
    def return_file_base64_string(file_name):
        path = os.path.join(
            os.getcwd(), 'data', 'downloadable_data', file_name)
        try:
            with open(path, 'rb') as file:
                base64_data = base64.b64encode(file.read())
                base64_string = base64_data.decode('utf-8')
                return base64_string
        except FileNotFoundError:
            assert False, \
                '\nФайл не найден'
        except Exception as e:
            assert False, \
                f'\nПроизошла ошибка {e}'
