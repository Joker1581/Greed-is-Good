def score1(dice):
    # your code here
    dict = {}
    score = 0
    for key in dice:
        dict[key] = dict.get(key, 0) + 1
    for key in dict:
        if key == 1:
            if dict[key] > 2:
                score += 1000
                if dict[key] > 3:
                    score += 100*(dict[key] - 3)
            else:
                score += 100*dict[key]
        elif key == 5:
            if dict[key] > 2:
                score += 500
                if dict[key] > 3:
                    score += 50*(dict[key] - 3)
            else:
                score += 50*dict[key]
        elif key == 2 and dict[key] > 2:
            score += 200
        elif key == 3 and dict[key] > 2:
            score += 300
        elif key == 4 and dict[key] > 2:
            score += 400
        elif key == 6 and dict[key] > 2:
            score += 600
    return score

def score(dice): 
    sum = 0
    counter = [0,0,0,0,0,0]
    points = [1000, 200, 300, 400, 500, 600]
    extra = [100,0,0,0,50,0]
    for die in dice: 
        counter[die-1] += 1

    for (i, count) in enumerate(counter):
        sum += (points[i] if count >= 3 else 0) + extra[i] * (count%3)

    return sum 

if __name__ == "__main__":
    res = list()
    dicelist = input("请输入5个1-6的数字,格式为1,2,3,4,5: ")
    for i in dicelist.split(","):
        res.append(int(i))
    print(score(res))