from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests
import csv

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "refined-sunup-382223",
  "private_key_id": "f20f4d099fd1150f9a9c32fdff681d16f1ce399c",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDGC2Z1So16gLXu\n4KxYbJ5Y+u1aXbd5h8vJnCxrbNdDLq68tDNUP5gGQHz2tSCihYVPZpCp2fcYHvUA\n0Qy4bqpVE311TAOgcD2VOU/vNDuZy6s+o61VrmLIjvctEVNaYWneHwozY8oG+c8I\nagDlnYK/Mbv3wVhps/nWR+1VTiueVYu7TZY5z2MrbYFLEelrpUZ4XOY0PiaRa0HK\nUOsME/4AzR/rBJ8bQOoXcxIEioXHpzdlH7e6b5zGA7gzDtjEnHm37Vlq/r26uXoW\nnnrMH/FNp3oh5Y5/rlZpTDDZfkW8mLw5BbVdVOtIbPHKAwWj17jXIWoCHNpv+V86\naxlYlDhFAgMBAAECggEACPx98O8J1efuuXDg6R8+nSd/qyTK/Tz78oE/Y7171AzT\neXUMyjMbhRcahIBKA43e83AiOs7M3z+SWu/hbaH54SPiArdJB9fn93QzDBXY6Xzc\nH5rCM/vWeCbCkP0zBMwcR2utpRDPWzstGYLj2QdpZh8N2itgBWXY/Y/kdUU3hfbj\nsylE4if6sKvJ3JXkYAtKw9bHdGzWGO88VjqQ5uIxIcZ7Ul0ZFSKuOoozKuu2xSrF\nGWlpqrqFfkfUqoNDLHgnC5IkC55UqcX/va7/yT2DvJBnNjakWHjpnJF4pqEqyVbM\nLkhUYeOJgX8ClaZzR6LdZP9hI5Xx93OTcQKWmy54wQKBgQD67J0+wB8hdoxzlCBE\n52OYVLkwKYaPXH0RuiHI/v/l9z+yB/vDJwsTOhIfEWMjW/2Kwmsz6A4AeyLHWhMm\nIC6eoYKv8xw2dO0V3rmKruMcn8g6/NR/w9OXhkPQYstIMx2WiCATRm10AJ3tPqVd\neLDJcbubC0KFKJ2CBFCrSRhmBQKBgQDKDPQhjGyVlcK6DJ8Lwu9KT38vYoWdjclB\nOBJ0djml2KU+z5B+RYobtw4HnypAfbzOQh1tGrMHgkTe02/QBVsm+aXQowvj6hSo\n8VjgryDlzbvMXBwt3aSMAuYue1IK5sUokWjxreKs+WHlY4a56p4kEkdt/Z/7wfFG\nz4dMRRDdQQKBgQDizplbrQD2mFdf6VY5sgVeHca+d+p/DxSlv17mdUgNL63NWFYD\nEfl6yZSzrF22CmJk2FNaObjeSm8nTo3cel5pWIfuTosD1jCvAgEoD+iNaQft+baC\nPhm17tDBPWuNuVZXSHfltFUe86fMWEHU+VCi5UC0ZjscbZfhe9EG4i1BmQKBgAtE\ns6zXTwr8ojKMF6apRX0od9hlrzv9N1cq0GSsX0Svk2+wVcelCzHGgMLODqYwHQKH\nz2pRTeDCVCL1OcwpME85JxU+sqAQYvyVETberYADfFDGZk/sh4vDcaDwAcBX5HEB\nww+Peg/ZjKslZNMjkZRDbLZmqbB5vYIMeug3BdzBAoGBALr7U4K2zQT0gfHXrZE3\nRQxd6lRuLyV6rA3sSlyr1398/CbWLPZtDe8x4xKjKM8Qa4RFyCb1ACY53fx47nT1\nqTtMqWFoM/iJ24O/VWG3VtKBpauWjLEc18MPnAzD10VuAOlSJ71JOG3yw6DIteqM\nEWv1FKCOSOlv2/1rJMs4DopB\n-----END PRIVATE KEY-----\n",
  "client_email": "servi-o@refined-sunup-382223.iam.gserviceaccount.com",
  "client_id": "110001377144186716902",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/servi-o%40refined-sunup-382223.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}

try:

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('atividade4') ### Nome do seu bucket
  blob = bucket.blob('artist-names.csv')

  pages = []
  names = "Name \n"

  for i in range(1, 5):
    url = 'https://web.archive.org/web/20121007172955/https://www.nga.gov/collection/anZ' + str(i) + '.htm'
    pages.append(url)

  for item in pages:
    page = requests.get(item)
    soup = BeautifulSoup(page.text, 'html.parser')

    last_links = soup.find(class_='AlphaNav')
    last_links.decompose()

    artist_name_list = soup.find(class_='BodyText')
    artist_name_list_items = artist_name_list.find_all('a')

    for artist_name in artist_name_list_items:
      names = names + artist_name.contents[0] + "\n"

    blob.upload_from_string(names, content_type="text/csv")

except Exception as ex:
  print(ex) 
