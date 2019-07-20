# 196390

from urllib.parse import unquote
from azure.storage.blob import BlobClient


CONTAINER_NAME = "testcontainer"
FILE_NAME = "loremipsum.txt"


def test_upload_file_with_leading_slash(storage_account, sas_token):
    client = BlobClient(
        f"https://{storage_account}.blob.core.windows.net/",
        credential=sas_token,
        container=CONTAINER_NAME,
        blob="/folder1/nestedfolder2/nestedfolder3/helloworld.txt",
    )
    with open(
        "/mnt/c/code/noelbundick/storage-sdk-tests/data/loremipsum.txt", "rb"
    ) as data:
        client.upload_blob(data, overwrite=True)

    assert "//folder1" not in client.url
    decoded_url = unquote(client.url)
    assert "//folder1" not in decoded_url


def test_upload_file_without_leading_slash(storage_account, sas_token):
    client = BlobClient(
        f"https://{storage_account}.blob.core.windows.net/",
        credential=sas_token,
        container=CONTAINER_NAME,
        blob="folder1/nestedfolder2/nestedfolder3/helloworld.txt",
    )
    with open(
        "/mnt/c/code/noelbundick/storage-sdk-tests/data/loremipsum.txt", "rb"
    ) as data:
        client.upload_blob(data, overwrite=True)

    assert "//folder1" not in client.url
    decoded_url = unquote(client.url)
    assert "//folder1" not in decoded_url
