

#There is no Block scope
game_level = 3
enemies = ["Skeleton","Zombie","Alien"]
if game_level <5:
    new_enemy = enemies[0]
print(new_enemy)


# Trong def thì lỗi
def create_enemies():
    game_level = 3
    enemies = ["Skeleton","Zombie","Alien"]
    if game_level <5:
        new_enemy1 = enemies[0]

print(new_enemy1)