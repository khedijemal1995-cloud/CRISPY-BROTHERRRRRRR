import random
import time
import sys

# --- THE SPAGHETTI STRATEGY ENGINE v3 (ULTIMATE CHAOS) ---
# Global variables for everything, no classes, just a massive web of logic.

kingdom_name = "CRISPY EMPIRE"
gold = 1500
population = 750
soldiers = 80
food = 3000
happiness = 85
stability = 90
prestige = 20
year = 1200
is_game_over = False

# Relations with neighbors
neighbor_a_relation = 50 # The Kingdom of Soggy Bread
neighbor_b_relation = 40 # The Republic of Toasted Cheese
neighbor_c_relation = 20 # The Empire of Burnt Crust

# Building levels
farm_lvl = 1
barracks_lvl = 1
market_lvl = 1
castle_lvl = 1
temple_lvl = 0
library_lvl = 0
spy_network_lvl = 0
wall_lvl = 1

# Random flags for consequences
has_plague = False
is_at_war = False
tax_rate = 15
conscription_active = False
festival_active = False
is_cursed = False
is_blessed = False
rebellion_chance = 0
science_points = 0
faith_points = 0
corruption = 5
culture = 10
defense_bonus = 0

# History log
history = []

def show_status():
    print("\n" + "═"*60)
    print(f"👑 {kingdom_name} - YEAR {year} 👑")
    print(f"💰 Gold: {gold} | 🍞 Food: {food} | 👥 Pop: {population}")
    print(f"⚔️ Soldiers: {soldiers} | 😊 Happiness: {happiness}%")
    print(f"⚖️ Stability: {stability}% | ⭐ Prestige: {prestige}")
    print(f"🔬 Science: {science_points} | 🙏 Faith: {faith_points} | 🎭 Culture: {culture}")
    print(f"📉 Corruption: {corruption}% | 🛡️ Walls: Lvl {wall_lvl}")
    print("═"*60)

def slow_print(text, speed=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

def add_history(event):
    history.append(f"Year {year}: {event}")
    if len(history) > 5:
        history.pop(0)

slow_print("WELCOME TO CRISPY BROTHER: THE ULTIMATE STRATEGY CHRONICLES", 0.02)
slow_print("Your legacy is written in the blood of your people and the gold in your vaults.", 0.02)

while not is_game_over:
    show_status()
    
    if history:
        print("\nRECENT HISTORY:")
        for h in history:
            print(f" - {h}")
    
    print("\nWhat is your command, Sire?")
    print("1. Infrastructure (Farms, Barracks, Market, Castle, Temple, Library, Walls, Spy Network)")
    print("2. Diplomacy (Gifts, Insults, Trade, Espionage, Alliances)")
    print("3. Military (Recruit, Invade, Defend, Conscription, Training)")
    print("4. Policy (Taxes, Festivals, Religion, Science, Corruption Crackdown, Cultural Gala)")
    print("5. Wait (Next Year)")
    print("6. Abdicate (Quit)")
    
    choice = input("> ")
    
    if choice == "1":
        print("What shall we build?")
        print("f: Farm (200g), b: Barracks (300g), m: Market (250g), c: Castle (500g), t: Temple (400g), l: Library (450g), w: Walls (350g), s: Spy Network (400g)")
        b_choice = input("> ").lower()
        if b_choice == "f" and gold >= 200:
            gold -= 200; farm_lvl += 1; print("Farms upgraded!")
        elif b_choice == "b" and gold >= 300:
            gold -= 300; barracks_lvl += 1; print("Barracks upgraded!")
        elif b_choice == "m" and gold >= 250:
            gold -= 250; market_lvl += 1; print("Market upgraded!")
        elif b_choice == "c" and gold >= 500:
            gold -= 500; castle_lvl += 1; stability += 10; print("Castle reinforced!")
        elif b_choice == "t" and gold >= 400:
            gold -= 400; temple_lvl += 1; faith_points += 15; print("Temple built!")
        elif b_choice == "l" and gold >= 450:
            gold -= 450; library_lvl += 1; science_points += 15; print("Library built!")
        elif b_choice == "w" and gold >= 350:
            gold -= 350; wall_lvl += 1; defense_bonus += 10; print("Walls heightened!")
        elif b_choice == "s" and gold >= 400:
            gold -= 400; spy_network_lvl += 1; print("Spy network expanded!")
        else:
            print("Not enough gold or invalid choice!")

    elif choice == "2":
        print("Which neighbor?")
        n_choice = input("a: Soggy Bread, b: Toasted Cheese, c: Burnt Crust: ").lower()
        print("Action: g: Gift (100g), i: Insult, t: Trade, e: Espionage (150g), l: Alliance (500g)")
        act = input("> ").lower()
        
        target_rel = 0
        if n_choice == "a": target_rel = neighbor_a_relation
        elif n_choice == "b": target_rel = neighbor_b_relation
        elif n_choice == "c": target_rel = neighbor_c_relation
        
        if act == "g" and gold >= 100:
            gold -= 100; target_rel += 25; print("They liked the gift.")
        elif act == "i":
            target_rel -= 50; prestige += 15; print("You insulted them! Your prestige grows, but they are furious.")
        elif act == "t":
            if target_rel > 40:
                gold += 250 + (market_lvl * 60); food -= 200; print("Trade successful!")
            else:
                print("They refuse to trade.")
        elif act == "e" and gold >= 150:
            gold -= 150
            success_chance = 0.4 + (spy_network_lvl * 0.1)
            if random.random() < success_chance:
                loot = random.randint(400, 800); gold += loot; target_rel -= 30; print(f"Spy successful! Stole {loot} gold.")
            else:
                print("Spy caught! They are angry."); target_rel -= 60; prestige -= 20
        elif act == "l" and gold >= 500:
            if target_rel > 70:
                gold -= 500; target_rel = 100; stability += 20; print("ALLIANCE FORMED!")
            else:
                print("They don't trust you enough for an alliance.")
        
        if n_choice == "a": neighbor_a_relation = target_rel
        elif n_choice == "b": neighbor_b_relation = target_rel
        elif n_choice == "c": neighbor_c_relation = target_rel

    elif choice == "3":
        print("Military actions:")
        print("r: Recruit (20g/soldier), v: Invade, c: Conscription (Free but unhappy), t: Training (200g)")
        m_act = input("> ").lower()
        if m_act == "r":
            num = int(input("How many? "))
            if gold >= num * 20:
                gold -= num * 20; soldiers += num; population -= num; print(f"Recruited {num} soldiers.")
            else:
                print("Not enough gold!")
        elif m_act == "c":
            num = int(input("How many to force into service? "))
            soldiers += num; population -= num; happiness -= num // 2; stability -= num // 3; print(f"Forced {num} people into the army.")
        elif m_act == "t" and gold >= 200:
            gold -= 200; science_points += 5; defense_bonus += 5; print("Soldiers trained!")
        elif m_act == "v":
            target = input("Target (a, b, c): ").lower()
            print("WAR!")
            is_at_war = True
            win_chance = (soldiers / 200) * (stability / 100) * (1 + (science_points / 150))
            if win_chance > 0.55:
                loot = random.randint(1000, 3000); gold += loot; prestige += 40; happiness += 15; add_history(f"Conquered lands of {target}")
                print(f"VICTORY! You looted {loot} gold.")
            else:
                loss = soldiers // 2; soldiers -= loss; stability -= 40; happiness -= 30; print(f"DEFEAT! You lost {loss} soldiers.")
            is_at_war = False

    elif choice == "4":
        print("Policy actions:")
        print("t: Set Taxes, f: Festival (500g), r: Religious Ritual (300g), s: Science Grant (400g), c: Corruption Crackdown (200g), g: Cultural Gala (400g)")
        e_act = input("> ").lower()
        if e_act == "t":
            tax_rate = int(input("New tax rate (0-70%): "))
            if tax_rate > 25:
                happiness -= (tax_rate - 25) * 4; stability -= (tax_rate - 25) * 2; print("The people are furious about the taxes.")
        elif e_act == "f" and gold >= 500:
            gold -= 500; happiness += 30; stability += 10; print("A grand festival is held.")
        elif e_act == "r" and gold >= 300:
            gold -= 300; faith_points += 30; is_blessed = (random.random() > 0.6); print("Ritual performed.")
        elif e_act == "s" and gold >= 400:
            gold -= 400; science_points += 40; print("Scientific breakthrough!")
        elif e_act == "c" and gold >= 200:
            gold -= 200; corruption -= 10; stability += 10; print("Corruption reduced.")
        elif e_act == "g" and gold >= 400:
            gold -= 400; culture += 25; prestige += 10; print("Cultural gala was a success.")

    elif choice == "5":
        # --- YEARLY CALCULATIONS (THE SPAGHETTI CORE v3) ---
        year += 1
        
        # Production & Consumption
        food_produced = (farm_lvl * 700) + (science_points * 8)
        food_consumed = population + (soldiers * 4)
        if is_blessed: food_produced *= 1.3
        food += (food_produced - food_consumed)
        
        gold_income = (population * (tax_rate / 100)) + (market_lvl * 200) + (prestige * 5) + (culture * 2)
        gold_income -= (gold_income * (corruption / 100)) # Corruption eats gold
        gold += int(gold_income)
        
        # Population growth
        if food > 0:
            growth = int(population * 0.07)
            population += growth; happiness += 3
        else:
            starvation = int(population * 0.2); population -= starvation; happiness -= 30; stability -= 20; print("!!! MASS FAMINE !!!")
            add_history("Famine killed thousands.")
            
        # Rebellion logic
        rebellion_chance = (100 - happiness) + (100 - stability) + (tax_rate * 3) + corruption
        if rebellion_chance > 150:
            print("!!! CIVIL WAR !!!")
            if soldiers > 100:
                print("The army held the capital, but the country is in ruins.")
                population -= 200; soldiers -= 40; stability -= 40; gold -= 1000; add_history("Civil war suppressed.")
            else:
                print("The rebels have stormed the palace! You are dragged to the guillotine.")
                is_game_over = True; break
        
        # Random Events
        event = random.randint(1, 15)
        if event == 1:
            print("!!! THE GREAT PLAGUE !!!"); population -= int(population * 0.4); stability -= 30; happiness -= 30; add_history("The Great Plague struck.")
        elif event == 2:
            print("!!! GOLD RUSH !!!"); gold += 3000; add_history("Gold rush in the mountains.")
        elif event == 3:
            print("!!! FOREIGN INVASION !!!")
            enemy_power = random.randint(100, 400)
            total_defense = soldiers + (wall_lvl * 20) + defense_bonus
            if total_defense > enemy_power:
                print("Your walls and soldiers held the line!"); soldiers -= 20; add_history("Repelled foreign invasion.")
            else:
                print("The enemy breached the walls!"); gold -= 1500; population -= 200; stability -= 30; wall_lvl -= 1; add_history("City sacked by invaders.")
        elif event == 4:
            if faith_points > 100:
                print("!!! DIVINE INTERVENTION !!!"); happiness = 100; stability = 100; gold += 1000; add_history("Divine miracle occurred.")
        elif event == 5:
            print("!!! CORRUPTION SCANDAL !!!"); corruption += 20; stability -= 20; add_history("Corruption scandal exposed.")
        elif event == 6:
            if science_points > 100:
                print("!!! INDUSTRIAL REVOLUTION !!!"); farm_lvl += 2; market_lvl += 2; gold += 2000; add_history("Industrial revolution began.")
        
        # Corruption growth
        corruption += 2
        
        # Check lose conditions
        if population <= 0:
            print("Your kingdom is a wasteland. GAME OVER."); is_game_over = True
        elif stability <= 0:
            print("Total anarchy has consumed the empire. GAME OVER."); is_game_over = True
        elif gold < -5000:
            print("The international bankers have repossessed your crown. GAME OVER."); is_game_over = True
        
        is_blessed = False

    elif choice == "6":
        print("You have left the throne. Your name will be a footnote in history."); is_game_over = True
    
    # Spaghetti logic: Unconnected state management
    if happiness > 100: happiness = 100
    if happiness < 0: happiness = 0
    if stability > 100: stability = 100
    if stability < 0: stability = 0
    if corruption < 0: corruption = 0
    
    if prestige > 500:
        print("YOU ARE THE EMPEROR OF THE WORLD!")
    
    time.sleep(1.5)

print("\n" + "💀"*30)
print("FINAL SCORE:", (gold + population + soldiers + prestige + science_points + faith_points + culture))
print("💀"*30)
