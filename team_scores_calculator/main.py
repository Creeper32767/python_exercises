import json
from os.path import join, abspath, dirname
from team_scores_calc import Team

with open(join(abspath(dirname(__file__)), "settings.json"), encoding="utf-8") as f:
    settings = json.load(f)
    add_points = settings["add_points"]
    team_number = settings["team_default"]

# get data
li_scores_persons = list()
for team in range(1, team_number+1):
    while True:
        try:
            scores = input(f"[TEAM {team}] 请输入成员分数: ")
            # if it can be turned to 'float' type
            tup_scores = tuple(map(float, scores.split()))
            # check the length to ensure it won't raise ZeroDivisionError
            if len(tup_scores) == 0:
                raise ValueError
            li_scores_persons.append(tup_scores)
            break
        except ValueError:
            print("[error] 输入中包含非数字字符或为空，请再输入一次。")


teams_obj = Team(li_scores_persons, add_points)
teams_obj.rank()
rank_str = teams_obj.output()
print("\n[result]\n"+rank_str)

input("Finished. Press 'Enter' to exit.")
