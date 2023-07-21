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
STATUS:200<br>
RESPONSE_BODY:<br>
{<br>
    "email": "string",<br>
    "name": "string"<br>
}<br>

<h4>PATCH:http://127.0.0.1:8000/api/account/user/manage/</h4><br>

This API endpoint is used to update the user object partially<br>

Request Body:
Addd the authorization token to the header for authentication purpose<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
and the user's information in the body of the request:<br>

{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "stringt"<br>
}<br>

RESPONSES:<br>
STATUS:200<br>

Response Body:<br>
The Response contains the user information with updated fields<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>


<h4>PUT:http://127.0.0.1:8000/api/account/user/manage/</h4><br>

This API endpoint is used to update the entire user object<br>

Request Body:
Addd the authorization token to the header for authentication purpose<br>

{<br>
'Authorization':"Token usertoken"<br>
}<br>
and the user's information in the body of the request:<br>

{<br>
  "email": "user@example.com",<br>
  "name": "string",<br>
  "password": "stringt"<br>
}<br>

RESPONSES:<br>
STATUS:200<br>

Response Body:<br>
The Response contains the user information with updated fields<br>
{<br>
  "email": "user@example.com",<br>
  "name": "string"<br>
}<br>

<h1>GOOGLE Authentication End Points</h1><br>
<h4>GET:http://127.0.0.1:8000/api/account/auth/google/</h4><br>
REQUEST BODY:<br>
No parameters<br>

Responses:<br>
STATUS:200<br>

Response Body:<br>

When the user requested to the above endpoint he will be redirected to Google authentication page<br>


<h1>GET:http://127.0.0.1:8000/auth/complete/google-oauth2/</h1><br>

When the user authentication completes the Google wil redirect the user to the above url with user information as query params,<br>
based on whether the user exist the django authentication system will sent him the authtoken if the user did not exist it will create<br>
the user on the user information and sent the authtoken<br>

Responses:<br>
STATUS:200<br>

Response Body:<br>
{<br>
"token":"string",<br>
"name":"string",<br>
}<br>





















