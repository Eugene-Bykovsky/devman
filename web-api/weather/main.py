import requests

URL_WEATHER_API: str = "https://wttr.in/"
LOCATIONS = ('london', 'svo', 'Череповец')
PAYLOAD_WEATHER_API: dict = {
    "n": "",
    "T": "",
    "q": "",
    "u": "",
    "lang": "en"
}


def fetch_weather_data(url: str, payload: dict, place: str) -> str:
    """Fetch weather data from API for a given place.

    Args:
        url: The base URL of the weather API.
        payload: Parameters for the API request.
        place: The location for which to fetch weather data.

    Returns: Wheather data(str) for a given place
    """
    response = requests.get(f"{url}{place}", params=payload)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    for location in LOCATIONS:
        try:
            print(fetch_weather_data(URL_WEATHER_API, PAYLOAD_WEATHER_API,
                                     location))
        except requests.exceptions.HTTPError as http_err:
            print(f"Can't get data from server for {location}. "
                  f"HTTP error:\n{http_err}")
        except requests.exceptions.RequestException as req_err:
            print(f"Can't get data from server for {location}. "
                  f"Error: {req_err}")
