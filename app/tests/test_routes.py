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
    # reason = 'reputation'
    absences = 92
    studyTime = 1
    activities = False
    # freeTime = 3
    Dalc = 5
    G1 = 3
    G2 = 1
    G3 = 2

    # url = f'''/student?reason={reason}&absences={absences}&studyTime={studyTime}&activities={activities}&freeTime={freeTime}&Dalc={Dalc}&G1={G1}&G2={G2}&G3={G3}'''
    url = f'''/student?absences={absences}&studytime={studyTime}&activities={activities}&Dalc={Dalc}&G1={G1}&G2={G2}&G3={G3}'''
    # url = f'''/student?Dalc={Dalc}&G1={G1}&G2={G2}'''

    response = client.get(url)

    assert response.status_code == 200

    assert response.get_data() == False


    # good student
    
    # reason = 'reputation'
    absences = 0
    studyTime = 4
    activities = True
    # freeTime = 3
    Dalc = 1
    G1 = 16
    G2 = 18
    G3 = 20

    # url = f'''/student?reason={reason}&absences={absences}&studyTime={studyTime}&activities={activities}&freeTime={freeTime}&Dalc={Dalc}&G1={G1}&G2={G2}&G3={G3}'''
    url = f'''/student?absences={absences}&studytime={studyTime}&activities={activities}&Dalc={Dalc}&G1={G1}&G2={G2}&G3={G3}'''
    # url = f'''/student?Dalc={Dalc}&G1={G1}&G2={G2}'''

    response = client.get(url)

    assert response.status_code == 200

    assert response.get_data() == True

    # himothy from the bay (super smart but never studies)
    
    # reason = 'reputation'
    absences = 23
    studyTime = 1
    activities = True
    # freeTime = 5
    Dalc = 5
    G1 = 20
    G2 = 20
    G3 = 20

    # url = f'''/student?reason={reason}&absences={absences}&studyTime={studyTime}&activities={activities}&freeTime={freeTime}&Dalc={Dalc}&G1={G1}&G2={G2}&G3={G3}'''
    url = f'''/student?absences={absences}&studytime={studyTime}&activities={activities}&Dalc={Dalc}&G1={G1}&G2={G2}&G3={G3}'''
    # url = f'''/student?Dalc={Dalc}&G1={G1}&G2={G2}'''

    response = client.get(url)

    assert response.status_code == 200

    assert response.get_data() == True




