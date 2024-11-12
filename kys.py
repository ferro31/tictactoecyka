import random
penz, szorzok = 100, [[0, "szopo"], [2, "double kill"], [3, "triple kill"], [10, "holy shit"]]
if input("A kezdéshez kérlek írd be hogy kezdés!") == "kezdes": print(f"A kezdőérték {penz}$")
while input("Írja be hogy pörgetés ha pörgetni szeretne") == "porgetes":
        c = random.choice(szorzok)
        penz *= c[0]
        print(f"{c[1]}\nJelenlegi érték = {penz}$")