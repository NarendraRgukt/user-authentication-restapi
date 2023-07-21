# user-authentication-restapi
Here are the various end points that I created in this project<br>
POST-http://127.0.0.1:8000/api/account/create/user/<br>
Body Request:<br>
{
  "email": "user@example.com",
  "name": "string",
  "password": "stringt"
}
Responses:<br>
HTTP_201_CREATED

Response Body:<br>
{
  "email": "user@example.com",
  "name": "string"
}
