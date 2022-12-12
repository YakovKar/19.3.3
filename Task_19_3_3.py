import json
import requests
#POST /pet/{petId}/uploadImage
def post_upload():
    base_url = 'https://petstore.swagger.io/v2'
    headers = {'accept': 'application/json'}
    petId = 9223372036854774888
    image = 'someanimal.jpeg'
    files = {'file': (image, open(image, 'rb'), 'image/jpeg')}
    res_post_upload = requests.post(url=f'{base_url}/pet/{petId}/uploadImage', headers=headers, files=files)
    print('POST /pet/{petId}/uploadImage  Uploads an image')
    print('  Статус запроса:', res_post_upload.status_code)
    print('  Ответ сервера body:', res_post_upload.json(), '\n')

#post_upload()

#POST /pet
def post_new_pet():
    base_url = 'https://petstore.swagger.io/v2'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    new_pet = {
          "id": 994234234234232434,
          "category": {
            "id": 7,
            "name": "Riazha"
          },
          "name": "kitty",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 13,
              "name": "Cat"
            }
          ],
          "status": "available"
        }
    res_post_new = requests.post(url=f'{base_url}/pet', headers=headers, data=json.dumps(new_pet))
    print('  Статус запроса:', res_post_new.status_code)
    print('  Ответ сервера body:', res_post_new.json(), '\n')

#post_new_pet()

#PUT /pet
def put_pet():
    base_url = 'https://petstore.swagger.io/v2'
    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    input = {
          "id": 9223372036854774999,
          "category": {
            "id": 0,
            "name": "Bob Marley"
          },
          "name": "chiller",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "Megarasta"
            }
          ],
          "status": "available"
        }
    res_put = requests.put(url=f'{base_url}/pet', data=json.dumps(input), headers=headers)
    print('  Статус запроса:', res_put.status_code)
    print('  Ответ сервера body:', res_put.json(), '\n')

#put_pet()

#GET /pet/findByStatus
def get_status():
    base_url = 'https://petstore.swagger.io/v2'
    res_get = requests.get(url=f'{base_url}/pet/findByStatus', params={'status': 'sold'})
    print('  Статус запроса:', res_get.status_code)
    print('  Ответ сервера body:', res_get.json(), '\n')

#get_status()

#GET /pet/{petId}
def get_petid():
    base_url = 'https://petstore.swagger.io/v2'
    petId = 9234324327245343
    res_get = requests.get(url=f'{base_url}/pet/{petId}')
    print('  Статус запроса:', res_get.status_code)
    print('  Ответ сервера body:', res_get.json(), '\n')

#get_petid()

#POST /pet/{petId}
def post_petid():
    base_url = 'https://petstore.swagger.io/v2'
    petId = 9234324327245343
    name_stat = {'name': 'Mija', 'status': 'available'}
    res_post_new_data = requests.post(url=f'{base_url}/pet/{petId}', data=name_stat)
    print('  Статус запроса:', res_post_new_data.status_code)
    print('  Ответ сервера body:', res_post_new_data.json(), '\n')

#post_petid()

#DELETE /pet/{petId}
def delete_pet():
    base_url = 'https://petstore.swagger.io/v2'
    petId = 9223372036854775038
    res_del = requests.delete(url=f'{base_url}/pet/{petId}')
    print('  Статус запроса:', res_del.status_code)
    print('  Ответ сервера body:', res_del.json(), '\n')

#delete_pet()












