import math

def compute():
    totalways = 1
    for a in range(0,3):
        for b in range(0,(2-a)*2 + 1):
            for c in range(0,math.ceil((2-a-b*0.5)*10)+1):
                for d in range(0,math.ceil((2-a-b*0.5-c*0.2)*20)+1):
                    for e in range(0,math.ceil((2-a-b*0.5-c*0.2-d*0.1)*40)+1):
                        for f in range(0,math.ceil((2-a-b*0.5-c*0.2-d*0.1-e*0.05)*100)+1):
                            for g in range(0,math.ceil((2-a-b*0.5-c*0.2-d*0.1-e*0.05-f*0.02)*200)+1):
                                if a*100 + b*50 + c*20 + d*10 + e*5 + f*2 + g*1 == 200:
                                    totalways += 1
    return totalways

print(compute())