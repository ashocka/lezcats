import requests


def get_facebook_events(page_id, access_token):
    url = f"https://graph.facebook.com/v10.0/{page_id}/events/attending"
    params = {
        'access_token': access_token
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        events = response.json()['data']
    else:
        events = []

    return events
