import os
import sys
from dotenv import load_dotenv
import pytest
from database.connect import Connection
from app import app

@pytest.fixture(scope="session")
def mongodb():
    load_dotenv()
    assert Connection.init(), "Connection error!"
    Connection.set_testing()

@pytest.fixture(scope="session")
def test_client():
    with app.test_client() as client:
        Connection.set_testing()
        yield client

if __name__ == "__main__":
    # add "-q" to list to have reduced message logs
    if len(sys.argv) == 3 and sys.argv[1] == "-t":
        filename = sys.argv[2]
        if os.path.exists(filename):
            sys.exit(pytest.main(["tests", "-k", filename]))
        else:
            print (f'Test file "{filename}" could not be found!')
    elif len(sys.argv) == 1:
        # run all the tests
        sys.exit(pytest.main(["tests"]))
    else:
        print ("Bad arguments!")
        print ("Leave blank to run all tests. To run specific test, type -t <path_to_test>")