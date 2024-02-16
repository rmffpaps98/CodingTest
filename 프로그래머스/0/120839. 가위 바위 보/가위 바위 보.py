def solution(rsp):
    return ''.join(["2" if i == "5" else "0" if i == "2" else "5" for i in rsp])