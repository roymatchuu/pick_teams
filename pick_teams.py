import random as rand
from prettytable import PrettyTable

rand.seed()

def print_teams(groups):
    tab = PrettyTable()
    num_groups = len(groups)
    print(groups)
    team_headers = [f'TEAM {i+1}' for i in range(num_groups)]
    for i in range(num_groups):
        tab.add_column(team_headers[i],groups[i])
    print(tab)


def parse_list_of_people(str):
    list_of_people = [x.strip() for x in str.split(',')]
    return list_of_people

def group(group,people,num_players):
    total_players = len(people)

    for g in group:
        for i in range(num_players):
            person = rand.choice(people) if len(people) > 1 else people[0]
            people.remove(person)
            g.append(person)

            if not people: break

    if total_players % len(group) != 0: group[-1].append('')
    return group

    

def create_teams(list_of_people):
    num_teams = input('Enter the number of teams: ')
    num_players_per_team = (len(list_of_people)//int(num_teams)) if len(list_of_people) % int(num_teams) == 0 else (len(list_of_people)//int(num_teams))+1
    
    groups =[[] for i in range(int(num_teams))]

    print(f'number of players per team: {num_players_per_team}')
    print(f'number of groups: {num_teams}')
    g = group(groups, list_of_people,num_players_per_team)

    return g

def main():
    inp = input('Enter list of people: ')

    people = parse_list_of_people(inp)
    groups = create_teams(people)
    print_teams(groups)

if __name__ == "__main__":
    main()