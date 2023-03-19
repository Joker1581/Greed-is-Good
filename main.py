def score(dice):
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

if __name__ == "__main__":
    print(score([5, 1, 3, 4, 1]))