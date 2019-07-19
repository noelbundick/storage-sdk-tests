def pytest_addoption(parser):
    parser.addoption("--storage-account", required=True)
    parser.addoption("--sas-token", required=True)


def pytest_generate_tests(metafunc):
    storage_account = metafunc.config.getoption("storage_account")
    sas_token = metafunc.config.getoption("sas_token")
    metafunc.parametrize("storage_account,sas_token", [(storage_account, sas_token)])
