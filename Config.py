# задаем базовый URL

base_url = 'https://petstore.swagger.io/v2'

# данные пользователя:

username = 'Ivan'
password = '123456'

# new user
user_body = {
  "id": 0,
  "username": "IvanIvanov",
  "firstName": "Ivan",
  "lastName": "Ivanov",
  "email": "ex@ya.ru",
  "password": "123",
  "phone": "9218885552",
  "userStatus": 0
}

# updated user
updated_user_body = {
  "id": 0,
  "username": "MaksPetrov",
  "firstName": "Maksim",
  "lastName": "Petrov",
  "email": "ex2222@ya.ru",
  "password": "456",
  "phone": "9217778899",
  "userStatus": 0
}

# new pet
pet_body = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

# list of users
users_list = [
  {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]

# Order
order = {
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "0",
  "status": "placed",
  "complete": True
}