def solution(id_pw, db):
    ID, PW = id_pw
    for i, p in db :
        if ID == i and PW == p : return "login"
        elif ID == i and PW != p : return "wrong pw"
    return "fail"