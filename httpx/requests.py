from pprint import pprint

import httpx


def get_github_events(url: str) -> dict:
    response = httpx.get(url)
    response.raise_for_status()
    return response.json()


def send_coordinates(coordinates: dict, url: str) -> dict:
    response = httpx.post(url, json=coordinates)
    response.raise_for_status()
    return response.json()


def main() -> None:
    # github_events = get_github_events('https://api.github.com/events')
    # pprint(github_events)
    point_coordinates = {'lon': 44, 'lat': 23}
    coordinates_service_result = send_coordinates(
        point_coordinates,
        'https://httpbin.org/post'
    )
    pprint(coordinates_service_result)


if __name__ == '__main__':
    main()
