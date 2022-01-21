# local scope

enemies =1

def increase_enemies():
    enemies=2
    print(f"enemies inside function : {enemies}")

increase_enemies()
# 아래에서는 계속 1이 출력 
print(f"enemies outside function : {enemies}")



# Local Scope

def drink_potion():
    potion_strength=2
    print(potion_strength)

drink_potion()
# 아래에서는 에러 발생 
print(potion_strength)



# Global Scope 
player_health=10 

def drink_potion():
    potion_strength=2
    # 아래의 player_health 는 작동함 
    print(player_health)

drink_potion() #10 인쇄함
print(player_health) #10 인쇄함 