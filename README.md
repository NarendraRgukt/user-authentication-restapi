# user-authentication-restapi
Here are the various end points that I created in this project<br>
POST-http://127.0.0.1:8000/api/account/create/user/<br>
Body Request:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "string"<br>
}<br>
Responses:<br>
HTTP_201_CREATED<br>

Response Body:<br>
{
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>
