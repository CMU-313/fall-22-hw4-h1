from binhex import REASONABLY_LARGE
from flask import Flask

from app.handlers.routes import configure_routes


def test_base_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()
    url = '/'

    response = client.get(url)

    assert response.status_code == 200
    assert response.get_data() == b'try the student route it is great!'


def test_student_route():
    app = Flask(__name__)
    configure_routes(app)
    client = app.test_client()

    # bad student

    Dalc = 5
    G1 = 3
    G2 = 1
    studytime = 1

    # keep parameters in this exact order (order in which they were fitted)
    url = f'''/student?Dalc={Dalc}&G1={G1}&G2={G2}&studytime={studytime}'''

    response = client.get(url)

    assert response.status_code == 200

    assert int(response.get_data()) == 0


    # good student
    
    Dalc = 1
    G1 = 20
    G2 = 20
    studytime = 3

    url = f'''/student?Dalc={Dalc}&G1={G1}&G2={G2}&studytime={studytime}'''

    response = client.get(url)

    assert response.status_code == 200

    assert int(response.get_data()) == 1

    # himothy from the bay (super smart but never studies)
    
    Dalc = 5
    G1 = 20
    G2 = 20
    studytime = 1

    url = f'''/student?Dalc={Dalc}&G1={G1}&G2={G2}&studytime={studytime}'''

    response = client.get(url)

    assert response.status_code == 200

    assert int(response.get_data()) == 1




