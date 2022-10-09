from load_candidates import *
from flask import Flask

app = Flask(__name__)


@app.route("/")
def get_all():
    result = ''
    candidates = load_candidates()
    for i in candidates:
        result += i["name"] + "<br>"
        result += i["position"] + "<br>"
        result += i["skills"] + "<br>"
        result += "<br>"
    return f'<p> {result} </p>'


@app.route("/profile/<int:pk>")
def get_by_pk(pk):
    result = ''
    data = get_candidate_by_pk(pk)
    result += data["name"] + "<br>"
    result += data["position"] + "<br>"
    result += data["skills"] + "<br>"

    return f'''
    <img src='({data["picture"]})'>
    <p> {result} </p>
    '''


@app.route("/skill/<skill>")
def get_candidate_skill(skill):
    result = ''
    candidates = get_student_by_skill(skill)
    for i in candidates:
        result += i["name"] + "<br>"
        result += i["position"] + "<br>"
        result += i["skills"] + "<br>"
        result += "<br>"
    return f'<p> {result} </p>'


app.run(debug=True)
