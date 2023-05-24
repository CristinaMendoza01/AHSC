import requests

# Set the access token obtained after authentication
access_token = "hyEcUHASVdnVrvslwoFtB6N00ZV7jR" # Caduca en un cierto tiempo

def retrieveSound(soundId):
    # Set the API endpoint URL for retrieving a sound by its ID
    sound_url = "https://freesound.org/apiv2/sounds/{sound_id}/"

    # Set the sound ID of the sound you want to play
    # sound_id = "9429"  # Replace with the actual sound ID

    # Set the headers with the access token
    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    # Make the authenticated request to retrieve the sound details
    response = requests.get(sound_url.format(sound_id=soundId), headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        sound_data = response.json()
        print(sound_data)
        # Get the URL of the sound preview
        sound_preview = sound_data["previews"]["preview-lq-mp3"]
        # print(sound_preview)

    else:
        print("Error occurred while retrieving the sound.")

    return response.json()
