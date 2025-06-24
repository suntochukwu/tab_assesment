from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_find_account():
    #test no user found exception case
    response = client.get("/", params={'account_id': '12345asdfg'})
    assert response.status_code == 404
    #test user found exception case
    response = client.get("/", params={'account_id': '7299be1b-8506-4702-8eb9-c418761f2dcf'})
    assert response.status_code == 200
    # assert response.json() == {"msg": "Hello World"}

    