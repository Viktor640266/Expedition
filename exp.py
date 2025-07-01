import random
import time 

class Expedition():
    def __init__(self, difficulty):
        self.diff = difficulty
        self.random_num = random.randint(0, 2)
        self.way = 1
        self.snow_colors = [15, 8, 15]
        self.nature_colors = [10, 11, 10]
        self.sky_colors = [21, 12, 0]
        self.sea_colors = [21, 12, 21]
        self.hp = 100
        self.hunger = 100
        self.temperature = 100
        self.matches = 10
        self.biom_list = ["mountain", "village", "snow flat", "sea", "forest"]
        self.km = 0
        self.biom = "sea"
        self.animals = ["bear", "wolf", "BIRD"]
        self.actions = [f"The {self.animals[self.random_num]} catched you! Write 'w' fast to escape!\nНа вас напал {self.animals[self.random_num]}! Чтобы спастись, быстро вводите w.", "You found berries!\n If you want to take the berries, write 'take'. Else, skip (press Enter).\nВы нашли ягоды! Если хотите их взять, напишите 'take'.\nЕсли не хотите их брать, пропустите, нажав Enter."]
        self.world = [['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'], 
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m'],
                      ['\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m', '\x1b[38;5;226;48;5;226m = \x1b[0m']]
    def game(self):
        self.biom = self.biom_list[self.random_num]
        inventory = ["meal", "meal", "meal", "water", "water", "water", "boat", "axe", "fishing rod", "showel"]
        food_list = ["berries", "tree bark", "meal", "water"]
        food_list_2 = []
        pole = 0
        d_list = []
        while self.hp > 0:
            random_on_way = random.randint(1, self.way)
            pole += 1
            if self.biom == "snow flat":
                self.way = 20
                for q in range(len(self.world)):
                    for r in range(len(self.world[q])):
                        if q < 10:
                            self.world[q][r] = f'\x1b[38;5;226;48;5;{self.sky_colors[self.random_num]}m . \x1b[0m'
                            self.randomnum()
                        else:
                            self.world[q][r] = f'\x1b[38;5;0;48;5;{self.snow_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum()
                self.km += 1
                self.hunger -= 1
                self.temperature -= 2
            if self.biom == "mountain":
                self.way = 15
                for m in range(len(self.world)):
                    for u in range(len(self.world[m])):
                        if u == m:
                            self.world[m][u] = f'\x1b[38;5;0;48;5;{self.snow_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum()
                        elif u < m:
                            self.world[m][u] = f'\x1b[38;5;0;48;5;{self.snow_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum()
                        else:
                            self.world[m][u] = f'\x1b[38;5;0;48;5;{self.sky_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum()
                self.hunger -= 5
                self.temperature -= 5
                self.km += 0.5
            if self.biom == "village":
                self.way = 1
                for i in range(len(self.world)):
                    for j in range(len(self.world[i])):         
                        if i == 1 and 2 < j < 6:
                            self.world[i][j] = f'\x1b[38;5;0;48;5;{self.snow_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum() 
                        elif i == 2 and 1 < j < 7:
                            self.world[i][j] = f'\x1b[38;5;0;48;5;{self.snow_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum()
                        elif i == 3 and 0 < j < 8:
                            self.world[i][j] = f'\x1b[38;5;0;48;5;{self.snow_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum()   
                        elif i == 4 and 0 <= j < 9:
                            self.world[i][j] = f'\x1b[38;5;0;48;5;{self.snow_colors[self.random_num]}m = \x1b[0m'
                            self.randomnum()   
                        else:
                            self.world[i][j] = f'\x1b[38;5;226;48;5;{self.sky_colors[self.random_num]}m . \x1b[0m'
                            self.randomnum()
                print("This is the village. Here you finally can sleep and eat food in the houses of kind villagers.\nЭто деревня. Здесь вы можете переночевать и поесть в домах добрых жителей.")    
                self.hp += 20
                self.hunger += 30
                self.temperature += 50
            if self.biom == "forest":
                self.way = 10
                for g in range(len(self.world)):
                    for l in range(len(self.world[g])):
                        if g < 5:
                            self.world[g][l] = f'\x1b[38;5;226;48;5;{self.sky_colors[self.random_num]}m ... \x1b[0m'
                        elif 4 < g < 9:
                            self.world[g][l] = f'\x1b[38;5;226;48;5;{self.nature_colors[self.random_num]}m /| \x1b[0m'
                        else:
                            self.world[g][l] = f'\x1b[38;5;226;48;5;{self.snow_colors[self.random_num]}m ... \x1b[0m'
                self.hunger -= 1
                self.temperature -= 5
            if self.biom == "sea":
                self.way = 15
                if "boat" in inventory:
                    for _ in range(len(self.world)):
                        for c in range(len(self.world[_])):
                            self.world[_][c] = f'\x1b[38;5;15;48;5;{self.sea_colors[self.random_num]}m - \x1b[0m'
                            self.randomnum()
                else:
                    print("You have no boat. You stayed here waiting for whales to reach the shore.\nWhat a pity there are no whales in this sea.\nУ вас не осталось лодки. Вы ждёте на берегу какого-нибудь кита чтобы он вас подвёз.\nКак жаль что в этих краях никогда не водились киты.")
                    break
            for row in self.world:
                print("".join(row))
            print("Health/Здоровье: ", self.hp)
            print("Fullness/Сытость: ", self.hunger)
            print("Biom name/Название биома: ", self.biom)
            print("Distance in biom/Расстояние пройденное в биоме: ", self.km, "km/км")
            w = input()
            if w == "i" or w == "I":
                use = input(f"{inventory}\n")
                luck = random.randint(0, 1)
                if self.biom == "sea" and use == "fishing rod fish":
                    if luck == 1:
                        inventory.append("fish")
                    else:
                        print("This time you didn`t catch anything\nВ этот раз вы ничего не поймали")
                if self.biom == "forest" and use == "axe tree":
                    inventory.append("tree bark")
                if self.biom == "snow flat" and use == "showel snow":
                    inventory.append("snow")
                if use == "matches tree bark":
                    if self.matches > 0 and "tree bark" in inventory:
                        self.temperature += 30
                        self.hp += 20
                        inventory.remove("tree bark")
                        fire = input("What do you want to do with fire? To cook fish or to boil the snow?\n If you want to cook fish, write 'fire fish'.\n If you want to boil the snow, write 'fire snow'.\n Else, skip (press Enter).\nЧто вы хотите сделать на костре? Если вы хотите приготовить рыбу, напишите 'fire fish'.\nЕсли вы хотите разогреть снег чтобы получить воду, напишите 'fire snow'.\nЕсли вы ничего не хотите, пропустите (нажав Enter).\n")
                        if fire == "fire snow" and "snow" in inventory:
                            inventory.append("water")
                            inventory.remove("snow")
                        if fire == "fire fish" and "fish" in inventory:
                            inventory.append("meal")
                            inventory.remove("fish")
                    else:
                        print("You have no matches\nСпички закончились\n")
                        continue
                for k in range(len(food_list)):
                    if use == f"eat {food_list[k]}":
                        self.hunger += 30
                        self.hp += 20
                        inventory.remove(food_list[k])
            else:
                self.hunger -= 2
                self.km += 1
            if self.km >= self.way - 1:
                randombiom = random.randint(0, 4)
                self.biom = self.biom_list[randombiom]
                print(f"Biom changed to {self.biom}\nБиом изменён на {self.biom}")
                d_list.append(self.km)
                self.km = 0
            if self.hunger < 20:
                self.hp -= 10
                for b in range(len(inventory)):
                    if inventory[b] in food_list:
                        food_list_2.append(inventory[b])
                if len(food_list_2) == 0:
                    eat = input("You ran out of food. But you have a wood boat. Do you want to eat the boat?\nIf yes, write yes. If no, skip (press Enter).\nУ вас закончилась еда. Вы хотите съесть свою лодку? Если да, напишите 'yes'. Если нет, пропустите (нажав Enter).\n")
                    if eat == "yes" or eat == "Yes":
                        inventory.remove("boat")
                        self.hunger += 30
                        self.hp += 20
            else:
                continue  
            if self.temperature < 50:
                self.hp -= 5
            if self.km % random_on_way == 0:
                randomaction = random.randint(0, 1)
                if randomaction == 0:
                    w_list = []
                    for s in range(10):
                        t = time.perf_counter()
                        y = input(self.actions[randomaction])
                        x = time.perf_counter()
                        if x - t <= 1 and y == "w" or x - t <= 1 and y == "W":
                            w_list.append(1)
                    if len(w_list) < 7:
                        print(len(w_list))
                        print("The animal is won. It`s end of expedition.\nЗверь победил. Экспедиция окончена.")
                        break
                    else:
                        print("You escaped from this animal. Now you can continue your expedition.\nПоздравляю, вы спаслись от зверя! Теперь вы можете продолжить экспедицию.")
                        randomaction = random.randint(0, 1)
                        random_on_way = random.randint(1, self.way)
                        continue
                else:
                    if input(self.actions[randomaction]) != "":
                        inventory.append("berries")
                    else:
                        randomaction = random.randint(0, 1)
                        random_on_way = random.randint(1, self.way)
                        continue
            if self.hp <= 0:
                print("Game over! HP is 0\nИгра окончена - ХП равно нулю")
            if self.diff == "easy" or self.diff == "Easy":
                if pole >= 100:
                    print(f"You won! You reached the pole!\nDistance you walked: {sum(d_list)}\nВы выиграли, достигнув полюса!\nРасстояние которое вы прошли: {sum(d_list)}")
                    break
            elif self.diff == "hard" or self.diff == "Hard":
                if pole >= 1000:
                    print(f"You won! You reached the pole!\nDistance you walked: {sum(d_list)}\nВы выиграли, достигнув полюса!\nРасстояние которое вы прошли: {sum(d_list)}")
                    break
            else:
                if pole >= 500:
                    print(f"You won! You reached the pole!\nDistance you walked: {sum(d_list)}\nВы выиграли, достигнув полюса!\nРасстояние которое вы прошли: {sum(d_list)}")
                    break
        return self.hunger, self.hp, self.km, self.biom
    def randomnum(self):
        self.random_num = random.randint(0, 2)
        return self.random_num

e = Expedition("medium")
e.game()