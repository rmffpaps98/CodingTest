def solution(rsp):
    return ''.join([str(2) if i == str(5) else str(0) if i == str(2) else str(5) for i in rsp])