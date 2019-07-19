# 202489

from azure.storage.blob import BlobClient

CONTAINER_NAME = "testcontainer"
FILE_NAME = "loremipsum.txt"


def test_get_blob_by_full_url(storage_account, sas_token):
    client = BlobClient(
        f"https://{storage_account}.blob.core.windows.net/{CONTAINER_NAME}/{FILE_NAME}",
        credential=sas_token,
    )
    content = client.download_blob().content_as_text()
    assert len(content) > 0
