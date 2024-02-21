def solution(myString, pat):
    myString = myString.replace(pat, pat+' ').split()
    return ''.join([i for i in myString if pat in i])