


import requests


def get_place_image(place_name):
    """
    Returns an image URL from Wikipedia.
    """

    try:

        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{place_name.replace(' ', '_')}"

        response = requests.get(url, timeout=10)

        data = response.json()

        if "originalimage" in data:
            return data["originalimage"]["source"]

    except Exception:
        pass

    return "https://upload.wikimedia.org/wikipedia/commons/6/65/No-Image-Placeholder.svg"