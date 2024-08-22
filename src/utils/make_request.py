import requests
import sys

def make_request(config_section):
    url = config_section.get("url")
    headers = config_section.get("headers", {})
    query_params = config_section.get("query", {})

    if not url:
        print("URL was not defined in the configuration file.")
        sys.exit(1)

    response = requests.get(url, headers=headers, params=query_params)

    if response.status_code != 200:
        print(f"Error making the request to {url}. Status Code: {response.status_code}")
        sys.exit(1)

    return {
        'json': response.json(),
        'headers': response.headers
    }