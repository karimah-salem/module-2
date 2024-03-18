file = open("teams.txt", "w")

sports_teams = ["liverpool", "chelsea", "barcelona", "arsenal", "psg"]

for team in sports_teams:
    file.write(team + "\n")

file.close()

file = open("teams.txt", "r+")

lines = file.readlines()

print(lines[0].strip())

lines[0] = "this is a new line\n"

print(lines[3].strip())


file.close()

file = open("teams.txt", "w")

file.writelines(lines)

file.close()

file = open("teams.txt", "r")

for line in file:
    print(line.strip())

file.close()
