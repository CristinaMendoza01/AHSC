import requests
from getAuthorizationGUI import authcode
from callAPI import callAPI

# Obtain the authorization code that the user has entried
authorization_code = authcode
# Set the access token obtained after authentication
access_token = callAPI(authorization_code)
# print("Hola:", access_token)
def retrieveSound(soundId):
    # Set the API endpoint URL for retrieving a sound by its ID
    sound_url = "https://freesound.org/apiv2/sounds/{sound_id}/"

    # Set the headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Make the authenticated request to retrieve the sound details
    response = requests.get(sound_url.format(sound_id=soundId), headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        sound_data = response.json()
        # Get the URL of the sound preview
        sound_preview = sound_data["previews"]["preview-lq-mp3"]
    else:
        print("Error occurred while retrieving the sound.")

    return response.json()
