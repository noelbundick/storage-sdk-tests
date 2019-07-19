# storage-sdk-tests

## Setup

```
RG=storage-tests
export AZURE_STORAGE_ACCOUNT=storagetest1

az group create -n $RG -l westus2
az storage account create -n $AZURE_STORAGE_ACCOUNT -g $RG

az storage share create -n testshare
az storage file upload -s testshare --source data/loremipsum.txt

az storage container create -n testcontainer
az storage blob upload -c testcontainer -n loremipsum.txt -f data/loremipsum.txt
```

## Python

Setting up your environment

```bash
git clone https://github.com/noelbundick/storage-sdk-tests
cd storage-sdk-tests/python

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -U pip
python -m pip install -r requirements.dev.txt
```

Go to the Azure Portal and generate a SAS token for your storage account

```bash
SAS_TOKEN='?sv=2018-03-28&ss=bfqt&srt=sco&sp=rwdlacup&se=2019-07-20T02:18:27Z&st=2019-07-19T18:18:27Z&spr=https&sig=1yf9VJv7Eic2GmpMOQ3imzbsteVubUWWAE1M6R4nJsU%3D'
pytest --storage-account=$AZURE_STORAGE_ACCOUNT --sas-token=$SAS_TOKEN
```
