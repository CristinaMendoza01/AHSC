import requests
############### UNIQUE FOR EACH USER ########################################
client_id = "TVtgIIPBY2JjUJhwRU4n"
client_secret = "dCvdtqvTd7A4WhnDF3qSkTZafXKxVqQIxlCM85KR" # it's the API KEY
############### UNIQUE FOR EACH USER ########################################

redirect_URL = "https://freesound.org/apiv2/oauth2/authorize/"
authorization_url = f"{redirect_URL}?client_id={client_id}&response_type=code&state=xyz"
token_url = "https://freesound.org/apiv2/oauth2/access_token/"

# Prompt the user to visit the authorization URL and obtain the authorization code
print(f"Please visit the following URL and authorize the application:\n{authorization_url}")
authorization_code = input("Enter the authorization code from the redirect URL: ")

# Exchange the authorization code for an access token
data = {
    "client_id": client_id,
    "client_secret": client_secret,
    "grant_type": "authorization_code",
    "code": authorization_code,
    # "redirect_uri": "https://freesound.org"
}

response = requests.post(token_url, data=data)
print(response.json())
access_token = response.json()["access_token"]
# Use the access token for authenticated API requests
headers = {
    "Authorization": f"Bearer {access_token}"
}
response = requests.get(f"{redirect_URL}/some_endpoint", headers=headers)
