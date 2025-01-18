import pytest
import os


@pytest.fixture(scope='session', autouse=True)
def stop_test_if_env_variables_are_empty(request):
    required_env_variables = ['BASE_API_URL', 'BASIC_AUTH_USER', 'BASIC_AUTH_PASSWORD', 'THUMBPRINT']
    missing_variables = [var for var in required_env_variables if not os.getenv(var)]
    if missing_variables:
        assert False, \
            f'\nСледующие обязательные переменные окружения не заданы: {", ".join(missing_variables)}' \
            '\nВсе тесты остановлены.' \
            '\nЗадайте переменные окружения с помощью команды:' \
            '\nДля Windows: $Env:ИМЯ_ПЕРЕМЕННОЙ = "значение"' \
            '\nДля Linux: export ИМЯ_ПЕРЕМЕННОЙ=значение'


# Форматирует кириллицу в консоли в корректный формат
def pytest_make_parametrize_id(val):
    return repr(val)
