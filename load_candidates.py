import json


def load_candidates():
    with open("candidates.json", encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_candidate_by_pk(pk):
    student = load_candidates()
    for i in student:
        if i["pk"] == pk:
            return


def get_student_by_skill(skill):
    data = load_candidates()
    skills = []
    for i in data:
        if skill in i["skills"].lower().split(", "):
            skills.append(i)
    return skills
