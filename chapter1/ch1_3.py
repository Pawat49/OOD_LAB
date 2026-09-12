

def counting_score(s):
    score = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    for i in s:
        score[i - 1] += 1
    return score

def most_popular(counted_score):
    highest_vote = max(counted_score)
    score_max = []
    for index,value in enumerate(counted_score):
        if value == highest_vote:
            score_max.append(index + 1)
    return score_max

print(f"*** Election ***")
voters = int(input("Enter a number of voter(s) : "))
number = [int(n) for n in input().split()[:voters]]
filter_number = list(filter(lambda x: 1 <= x <= 20, number))
winner_list = most_popular(counting_score(filter_number))
# print(counting_score(filter_number))
# print(winner_list)
if filter_number:
    for i in winner_list:
        print(i,end=" ")
else:
    print(f"*** No Candidate Wins ***")
