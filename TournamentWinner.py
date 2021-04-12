def tournamentWinner(competitions, results):
    d = dict()
    for i in range(len(competitions)):
        if results[i] == 0:
            if competitions[i][1] in d.keys():
                d[competitions[i][1]] += 3
            else:
                d[competitions[i][1]] = 3
        else:
            if competitions[i][0] in d.keys():
                d[competitions[i][0]] += 3
            else:
                d[competitions[i][0]] = 3
        print(d)
    return max(d,key=d.get)


competitions = [["HTML", "C#"],["C#", "Python"],["Python", "HTML"]]
results = [0, 0, 1]
print(tournamentWinner(competitions,results))

competitions = [["HTML", "Java"],["Java", "Python"],["Python", "HTML"],["C#", "Python"],["Java", "C#"],["C#", "HTML"]]
results = [0, 1, 1, 1, 0, 1]
print(tournamentWinner(competitions,results))

