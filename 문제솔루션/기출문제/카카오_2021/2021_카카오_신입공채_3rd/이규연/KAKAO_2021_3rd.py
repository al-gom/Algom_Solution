from bisect import bisect_left
from itertools import combinations
import re


def solution(info, query):
    answer = []
    dict = {}
    info = [i.split(' ') for i in info]
    for i in info:
        for j in range(5):
            for c in combinations([0, 1, 2, 3], j):
                key = ""
                for idx in range(4):
                    if idx not in c:
                        key += i[idx]
                    else:
                        key += '-'
                if key in dict.keys():
                    dict[key].append(int(i[-1]))
                else:
                    dict[key] = [int(i[-1])]

    for key in dict:
        dict[key].sort()

    query = [i.replace('and ', '').replace(' ', '') for i in query]
    for q in query:
        score = int(re.sub('[^0-9]', '', q))
        target = re.sub('[0-9]', '', q)
        if target in dict.keys():
            answer.append(len(dict[target]) - bisect_left(dict[target], score))
        else:
            answer.append(0)

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"]

print(solution(info, query))
