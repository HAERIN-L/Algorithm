def solution(id_pw, db):
    db_dict = dict(db)
    id, pw = id_pw
    
    if id in db_dict:
        if db_dict[id] == pw:
            return "login"
        else:
            return "wrong pw"
    else:
        return "fail"
