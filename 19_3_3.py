import requests
import json
import Config
import datetime
from Config import base_url, user_body, pet_body, users_list, updated_user_body, order

username = Config.username
password = Config.password

# USER
# Create new user
info = json.dumps(user_body, ensure_ascii=False)

res = requests.post(f'{base_url}/user', headers={'accept': 'application/json',
                                                 'Content-Type': 'application/json'},  data=info)
print('Create new user')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

# Get user by username
username = Config.user_body['username']
res = requests.get(f'{base_url}/user/{username}', headers={'accept': 'application/json'})
print('Get user by username')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

# Log user into system
res = requests.get(f'{base_url}/user/login?username={username}&password={password}', headers={'accept': 'application/json'})
print('Logs user into system')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

# Update user
username = Config.user_body['username']
info = json.dumps(updated_user_body, ensure_ascii=False)

res = requests.put(f'{base_url}/user/{username}', headers={'accept': 'application/json',
                                                           'Content-Type': 'application/json'}, data=info)
print('Update user')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

# Delete user
username = Config.user_body['username']

res = requests.delete(f'{base_url}/user/{username}', headers={'accept': 'application/json',
                                                              'Content-Type': 'application/json'})
print('Delete user')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

#  Create a list of users with given input array
info = json.dumps(users_list, ensure_ascii=False)

res = requests.post(f'{base_url}/user/createWithArray', headers={'accept': 'application/json',
                                                                 'Content-Type': 'application/json'}, data=info)
print('Create a list of users with given input array')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers)
print('  Type:', (type(res.json())), '\n')

# Create a list of users with given input list
info = json.dumps(users_list, ensure_ascii=False)

res = requests.post(f'{base_url}/user/createWithList', headers={'accept': 'application/json',
                                                                'Content-Type': 'application/json'}, data=info)
print('Create a list of users with given input list')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers)
print('  Type:', (type(res.json())), '\n')

# Log user out of system
res = requests.get(f'{base_url}/user/logout', headers={'accept': 'application/json'})
print('Logs user into system')
print('  Статус:', res.status_code)
print('  Body:', res.json(),'\n')

# PETS
# Add a new pet to the store
body = Config.pet_body
body['name'] = 'Hat-cat'
body['category']['name'] = 'Cats'
body['tags'][0]['name'] = 'Cat'
body['tags'].append({"id": 0, "name": "striped_cat"})
body['status'] = 'available'
body = json.dumps(body)

info = json.dumps(pet_body, ensure_ascii=False)

res = requests.post(f'{base_url}/pet', headers={'accept': 'application/json',
                                                'Content-Type': 'application/json'}, data=info)
print('Add a new pet to the store')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

pet_id = res.json()['id']

# Find pet by status
status = 'available'

res = requests.get(f'{base_url}/pet/findByStatus?status={status}', headers={'accept': 'application/json'})

print('Find pet by status')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  :', res.headers, '\n')

# Find pet by ID
petId = pet_id

res = requests.get(f'{base_url}/pet/{petId}', headers={'accept': 'application/json'})

print('Find pet by ID')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')


# Upload image
petId = pet_id
image = 'hat.jpg'
content = {'file': (image, open(image, 'rb'), 'image/jpg')}

res = requests.post(f'{base_url}/pet/{petId}/uploadImage', headers={'accept': 'application/json'}, files=content)

print('Upload an image')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# Update pet
body = Config.pet_body
body['name'] = 'MrDog'
body['category']['name'] = 'Dogs'
body['tags'][0]['name'] = 'Dog'
body['tags'].append({"id": 0, "name": "woofwoof"})
body['status'] = 'sale'
body = json.dumps(body)

info = json.dumps(pet_body, ensure_ascii=False)

res = requests.put(f'{base_url}/pet', headers={'accept': 'application/json',
                                               'Content-Type': 'application/json'}, data=info)

print('Update pet')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

# Update pet with form data
petId = pet_id
name = 'Petya3'
status = 'new_test_status'
form_data = f'name={name}&status={status}'
res = requests.post(f'{base_url}/pet/{petId}', headers={'accept': 'application/json',
                                               'Content-Type': 'application/x-www-form-urlencoded'}, data=form_data)
print('Update pet with form data')
print('  Статус:', res.status_code)
print('  Body:', res.json())
print('  Headers:', res.headers, '\n')

# Delete Pet
petId = pet_id

res = requests.delete(f'{base_url}/pet/{petId}', headers={'accept': 'application/json',
                                                'api_key': 'special-key'})

print('Delete a pet')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# STORE
# Place an order
time = datetime.datetime.today()
body = Config.order
body['shipDate'] = time.isoformat()
info = json.dumps(order, ensure_ascii=False)
res = requests.post(f'{base_url}/store/order', headers={'accept': 'application/json',
                                                        'Content-Type': 'application/json'}, data=info)
print('Place an order')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

order_id = res.json()['id']

# Find purchase order by ID
orderId = order_id

res = requests.get(f'{base_url}/store/order/{orderId}', headers={'accept':'application/json'})
print('Find purchase order by ID')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# Return pet inventories by status
res = requests.get(f'{base_url}/store/inventory', headers={'accept':'application/json'})
print('Return pet inventories by status')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')

# Delete order
orderId = order_id

res = requests.delete(f'{base_url}/store/order/{orderId}', headers={'accept':'application/json'})

print('Delete Order')
print('  Статус запроса:', res.status_code)
print('  Ответ сервера body:', res.json(), '\n')