from nose.tools import *
from bin.app import app
from bin.post_form import app as pf
from tests.tools import assert_response

def test_index():
    # check that we get 404 on URL /
    resp = app.request("/")
    assert_response(resp, status="404")

def test_index1():
    # test out first GET request to /hello 
    resp = app.request("/hello")
    assert_response(resp)

def test_index2():
    # make sure the default values work for the form
    resp = pf.request("/hello", method="POST")
    assert_response(resp, contains="NoBody")

def test_index3():
    # test that we get tehe expected values
    data = {'name':'vsukt', 'greet':'Hello'}
    resp = pf.request("/hello", method="POST", data=data)
    assert_response(resp, contains="vsukt")