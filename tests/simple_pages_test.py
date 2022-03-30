"""This test the homepage"""


def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" style="font-size:25px" href="/page1">Github</a>' in response.data
    assert b'<a class="nav-link" style="font-size:25px" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" style="font-size:25px" href="/page3">Python & flask</a>' in response.data
    assert b'<a class="nav-link" style="font-size:25px" href="/page4">CICD</a>' in response.data
    assert b'<a class="nav-link" style="font-size:25px" href="/page5">Pylint</a>' in response.data
    assert b'<a class="nav-link" style="font-size:25px" href="/page6">AAA</a>' in response.data
    assert b'<a class="nav-link" style="font-size:25px" href="/page7">OOPS</a>' in response.data
    assert b'<a class="nav-link" style="font-size:25px" href="/page8">SOLID</a>' in response.data


def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hey this is Tarun Sai Pavan Datla" in response.data



def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"A branch represents an" in response.data


def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker Container" in response.data


def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"testing framework that lets" in response.data


def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"different features of the same app" in response.data


def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"A class is like a blueprint while" in response.data


def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"is a pattern for arranging" in response.data


def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"encapsulation is the way to ensure" in response.data


def test_request_page8(client):
    """This makes the index page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"module must not depend on" in response.data


def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page9")
    assert response.status_code == 404
