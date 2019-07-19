# 233674
# https://github.com/Azure/azure-storage-python/issues/609
# Note: `make_file_url` no longer exists

from azure.storage.file import FileServiceClient
from azure.storage.file.file_client import FileClient

SHARE_NAME = "testshare"
DIRECTORY_NAME = "/"
FILE_NAME = "loremipsum.txt"


def test_file_sas_from_FileServiceClient(storage_account, sas_token):
    service = FileServiceClient(
        f"https://{storage_account}.file.core.windows.net/", credential=sas_token
    )
    share = service.get_share_client(SHARE_NAME)
    f = share.get_file_client(FILE_NAME)
    assert "??" not in f.url


def test_file_sas_from_FileClient(storage_account, sas_token):
    f = FileClient(
        f"https://{storage_account}.file.core.windows.net/",
        share=SHARE_NAME,
        file_path=FILE_NAME,
        credential=sas_token,
    )
    assert "??" not in f.url


def test_file_sas_from_FileClient_with_file_url(storage_account, sas_token):
    f = FileClient(
        f"https://{storage_account}.file.core.windows.net/{SHARE_NAME}/{FILE_NAME}",
        credential=sas_token,
    )
    assert "??" not in f.url
