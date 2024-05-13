import pytest 
import httpx


async def make_api_request(url, data):
    async with httpx.AsyncClient() as client:
        response = await client.post(url, json=data)
        return response


@pytest.mark.asyncio
async def test_api_request(httpx_mock):
    httpx_mock.add_response(
        url='https://some-api.org/post', 
        json={'status': 'created'}, 
        status_code=200
    )
    response = await make_api_request(
        'https://some-api.org/post',
        {'username': 'some_name'}
    )
    assert response.json() == {'status': 'created'}
    assert response.status_code == 200

