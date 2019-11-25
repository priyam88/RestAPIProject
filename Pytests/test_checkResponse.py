import requests
import jsonpath

url = "https://jsonplaceholder.typicode.com/posts"


def test_response_code():
    response = requests.get(url)
    assert response.status_code == 200


def test_response_body():
    # To find userID: 7
    response = requests.get(url)
    json_response = response.json()
    userids = jsonpath.jsonpath(json_response, "$[0:].userId")
    assert userids.__contains__(7)
    # To find title of that userID
    print("\n")
    for item in json_response:              # Check for dict loop
        if item["userId"] == 7:
            print("userId: " + str(item["userId"]) +
                  "\ntitle: " + item["title"])
