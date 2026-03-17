names = []
total_score = 0
# Read the names as a list
# Split by comma
# Remove " in front and after each name

def get_name_score(name: str) -> int:
    name = name.lower()
    score = 0
    for char in name:
        score += ord(char) - 96
    return score

with open('0022_names.txt') as f:
    names = f.read().replace('"', '').split(",")
    names.sort()

for i, name in enumerate(names):
    name_score = get_name_score(name) * (i +1)
    total_score += name_score

print("The total name score of all %d names is: %d" % (len(names), total_score))

