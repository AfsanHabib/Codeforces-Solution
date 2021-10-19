#Solved

def Games(teams):
    count = 0
 
    for hostTeam in teams:
        for guestTeam in teams:
            if (hostTeam != guestTeam):
                if (hostTeam["host"] == guestTeam["guest"]):
                    count += 1
 
    return count
 
 
def main():
    n = int(input())
    teams = []
 
    for i in range (n):
        teamColors = input().split()
        teamColors = [int(i) for i in teamColors]
        teams.append({"host": teamColors[0],"guest": teamColors[1]})
    print(Games(teams))
 
main()