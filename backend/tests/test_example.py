from runtests import test_client, mongodb

def test_hello_world():
    s = "Hello world"
    assert s == "Hello world", "Failed assert equal!"

def test_string():
    s = "hello world"
    assert s.islower() == True, "Failed lower!"
    assert s.isupper() == False, "Failed upper!"

# To test flask, import `test_client` fixture from runtests and pass parameter like so
def test_index_route(test_client):
    # test_client has type FlaskClient. You can do `get`, `post`, and pass in request headers and stuff
    # https://flask.palletsprojects.com/en/2.0.x/testing/
    result = test_client.get("/api/")
    assert result.status_code == 200, "Could not get api index route!"
    # it would be wise to clean up cookies after a test.
    # Also you can clear cookies during the middle of a test, like creating account, clear cookie, then test logging in
    test_client.cookie_jar.clear()

# To have access to the db, import `mongodb` fixture from runtests and pass parameter like so
# Will fail if no ATLAS_URL env is specified
# def test_db(mongodb):
#     pass