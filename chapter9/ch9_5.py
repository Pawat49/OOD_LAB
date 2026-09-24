# team = { "name": "Manchester United", "wins": 30, "loss": 3, "draws": 5, "scored": 88, "conceded": 20 }

# Total Points = 3 * wins + 0 * loss + 1 * draws = 3 * 30 + 0 * 3 + 5 * 1 = 95 points
# Goal Difference = scored - conceded = 88 - 20 = 68

inp = input("Enter Input : ").split("/")
team = { "name": "", "wins": 0, "loss": 0, "draws": 0, "scored": 0, "conceded": 0 ,"GD": 0}
team_list = []
# print(inp)

for stat in inp:
    data = stat.split(",")
    team["name"] = data[0]
    team["wins"] = int(data[1])
    team["loss"] = int(data[2])
    team["draws"] = int(data[3])
    team["scored"] = int(data[4])
    team["conceded"] = int(data[5])
    team["points"] = (3 * team["wins"]) + (1 * team["draws"]) + (0 * team["loss"])
    team["GD"] = team["scored"] - team["conceded"]
    # print(team)
    team_list.append(team.copy())
# print(team_list)
print("== results ==")

n = len(team_list)
for last in range(n-1,0,-1):
    big_i = 0
    for j in range(1,last+1):
        if team_list[big_i]["points"] > team_list[j]["points"]:
            big_i = j
        elif team_list[big_i]["points"] == team_list[j]["points"]:
            if team_list[big_i]["GD"] > team_list[j]["GD"]:
                big_i = j
        team_list[last],team_list[big_i] = team_list[big_i],team_list[last]

for team_jaa in team_list:
    print([team_jaa["name"],{'points': team_jaa["points"]},{'gd': team_jaa["GD"]}])