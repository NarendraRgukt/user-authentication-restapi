# user-authentication-restapi
Here are the various end points that I created in this project<br>
POST-http://127.0.0.1:8000/api/account/create/user/<br>
This endpoint is used to create user by providing the user details<br>
Body Request:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "string"<br>
}<br>
Responses:<br>
HTTP_201_CREATED<br>

Response Body:<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>


<h4>POST-http://127.0.0.1:8000/api/account/user/token/</h4><br>
This is used to generate the token for the user which can be used for the authentication<br>

Request Body:<br>

{<br>
  "email": "user@example.com",<br>
  
  "password": "string"<br>
}<br>

Responses:<br>

STATUS_200_OK<br>

Response Body:<br>

{<br>
    "token": "string"<br>
}<br>


<h4>GET-http://127.0.0.1:8000/api/account/user/manage/</h4><br>
It will retrieve the user information 
Request Body:<br>
In the headers of the request with the field name of authorization sending user's token<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
RESPONSES:<br>
STATUS:200
RESPONSE_BODY:<br>
{<br>
    "email": "string",<br>
    "name": "string"<br>
}<br>














