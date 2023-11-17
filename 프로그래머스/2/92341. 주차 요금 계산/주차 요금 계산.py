import math

def solution(fees, records):
    answer = []
    dict_rec = {}
    dict_time = {}
    bhour, bfee, fmin, pfee = map(int, fees)
    
    for record in records:
        time, num, ent = record.split()
        hour, mn = map(int, time.split(':'))
        minutes = (hour * 60) + mn
        
        if num not in dict_rec and ent == "IN":
            dict_rec[num] = minutes
        elif num in dict_rec and ent == "OUT" :
            if num not in dict_time :
                dict_time[num] = 0
            dict_time[num] += minutes - dict_rec[num]
            del dict_rec[num]
            
    if dict_rec :        
        for num in dict_rec :
            if num not in dict_time :
                dict_time[num] = 0
            dict_time[num] += 1439 - dict_rec[num]
            
    dict_time = sorted(dict_time.items())
    for _, value in dict_time :
        if value > bhour :
            fee = bfee + (math.ceil((value - bhour) / fmin) * pfee)
        else :
            fee = bfee
            
        answer.append(fee)
        
    return answer