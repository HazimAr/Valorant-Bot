users = [
    "Sakuraツ#juice",
    "SyfeFPS#8099",
    "SoulPsych0#uwu",
    "tunaflip#uwu",
    "Misaki#levi",
    "TayTayy#4828",
    "swage#0424",
    "milkyway#MILF",
]
users_rank = [350, 250, 750, 350, 950, 150, 0]

total_mmr = 0
for i in users_rank:
    if type(i) == int:
        total_mmr += i

bracket = []

users_and_rank = {
    "Sakuraツ#juice": 350,
    "SyfeFPS#8099": 250,
    "tunaflip#uwu": 750,
    "Misaki#levi": 350,
    "TayTayy#4828": 950,
    "swage#0424": 150,
    "milkyway#MILF": 0,
}
average_user_mmr = total_mmr / len(users)

for i in range(len(users_and_rank.keys()) // 2):
    users_original = list(users_and_rank.keys())
    users = list(users_and_rank.keys())
    player_one_key = users[i]
    print(player_one_key)
    users.remove(player_one_key)

    temp_key = users[i + 1]

    for j in range(len(users) // 2):
        if (average_user_mmr - users_and_rank[users_original[j]]) < (
            average_user_mmr - users_and_rank[users_original[temp_key]]
        ):
            temp_key = j
            users.remove(temp_key)

    bracket.append(
        [
            [player_one_key, users_and_rank[player_one_key]],
            [temp_key, users_and_rank[temp_key]],
        ]
    )

print(bracket)

# users_and_rank[users_original[j]]
# users_and_rank[users_original[temp_key]]
