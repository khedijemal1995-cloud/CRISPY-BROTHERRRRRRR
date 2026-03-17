import random
import time
import sys

# GLOBAL VARIABLES EVERYWHERE
p_hp = 100
p_mp = 50
p_xp = 0
p_lvl = 1
p_name = "CRISPY BROTHER"
p_inv = ["Old Bread", "Rusty Spoon"]
p_loc = "Kitchen"
p_gold = 10
is_alive = True
has_key = False
boss_hp = 500
enemy_name = ""
enemy_hp = 0
turn_count = 0
weather = "Sunny"
hunger = 0
thirst = 0
luck = 5
strength = 10
agility = 10
intelligence = 10
stamina = 100
mana_regen = 5
health_regen = 2
is_poisoned = False
is_stunned = False
is_burning = False
is_frozen = False
is_invisible = False
is_invincible = False
is_flying = False
is_swimming = False
is_climbing = False
is_sleeping = False
is_confused = False
is_cursed = False
is_blessed = False
is_enraged = False
is_tired = False
is_hungry = False
is_thirsty = False
is_dirty = False
is_smelly = False
is_happy = True
is_sad = False
is_angry = False
is_scared = False
is_bored = False
is_excited = False
is_surprised = False
is_disgusted = False
is_ashamed = False
is_guilty = False
is_proud = False
is_lonely = False
is_loved = False
is_hated = False
is_jealous = False
is_greedy = False
is_lazy = False
is_lustful = False
is_gluttonous = False
is_vain = False
is_cruel = False
is_kind = False
is_honest = False
is_brave = False
is_cowardly = False
is_wise = False
is_foolish = False
is_strong = False
is_weak = False
is_fast = False
is_slow = False
is_smart = False
is_dumb = False
is_rich = False
is_poor = False
is_famous = False
is_infamous = False
is_hero = False
is_villain = False
is_legend = False
is_myth = False
is_god = False
is_mortal = False
is_immortal = False
is_undead = False
is_ghost = False
is_demon = False
is_angel = False
is_alien = False
is_robot = False
is_cyborg = False
is_mutant = False
is_vampire = False
is_werewolf = False
is_zombie = False
is_skeleton = False
is_dragon = False
is_phoenix = False
is_unicorn = False
is_mermaid = False
is_centaur = False
is_minotaur = False
is_cyclops = False
is_giant = False
is_dwarf = False
is_elf = False
is_orc = False
is_goblin = False
is_troll = False
is_ogre = False
is_gnome = False
is_halfling = False
is_hobbit = False
is_human = True

print("WELCOME TO THE WORLD OF CRISPY BROTHER!!!")
print("-----------------------------------------")

while is_alive:
    print("\n--- STATUS ---")
    print("Name:", p_name)
    print("HP:", p_hp)
    print("MP:", p_mp)
    print("Location:", p_loc)
    print("Inventory:", p_inv)
    print("Gold:", p_gold)
    print("Hunger:", hunger)
    print("Thirst:", thirst)
    print("Weather:", weather)
    
    if hunger > 50:
        print("You are hungry!")
        is_hungry = True
    if thirst > 50:
        print("You are thirsty!")
        is_thirsty = True
    
    if p_hp <= 0:
        print("YOU DIED!")
        is_alive = False
        break
        
    cmd = input("What do you want to do? (move, eat, drink, search, status, quit): ").lower()
    
    if cmd == "quit":
        print("Goodbye!")
        break
    elif cmd == "move":
        print("Where do you want to go?")
        dest = input("Destinations: Garden, Cellar, Attic, Street: ").lower()
        if dest == "garden":
            p_loc = "Garden"
            print("You are in the garden. It is " + weather)
            if random.randint(1, 10) > 7:
                print("A wild Rat appeared!")
                enemy_name = "Rat"
                enemy_hp = 20
                while enemy_hp > 0 and p_hp > 0:
                    print("Rat HP:", enemy_hp)
                    act = input("Action (attack, run): ").lower()
                    if act == "attack":
                        dmg = random.randint(1, strength)
                        enemy_hp -= dmg
                        print("You hit the Rat for", dmg, "damage!")
                        if enemy_hp > 0:
                            e_dmg = random.randint(1, 5)
                            p_hp -= e_dmg
                            print("The Rat bit you for", e_dmg, "damage!")
                    elif act == "run":
                        if random.randint(1, 10) > 5:
                            print("You escaped!")
                            break
                        else:
                            print("You couldn't escape!")
                            e_dmg = random.randint(1, 5)
                            p_hp -= e_dmg
                            print("The Rat bit you for", e_dmg, "damage!")
                if enemy_hp <= 0:
                    print("You killed the Rat!")
                    p_xp += 10
                    p_gold += 2
        elif dest == "cellar":
            p_loc = "Cellar"
            print("It's dark here.")
            if not has_key:
                print("You found a key!")
                has_key = True
                p_inv.append("Rusty Key")
        elif dest == "attic":
            p_loc = "Attic"
            print("Dusty...")
            if random.randint(1, 10) == 1:
                print("You found a Golden Spoon!")
                p_inv.append("Golden Spoon")
        elif dest == "street":
            p_loc = "Street"
            print("The street is busy.")
            if p_gold >= 5:
                buy = input("Do you want to buy a sandwich for 5 gold? (yes/no): ").lower()
                if buy == "yes":
                    p_gold -= 5
                    p_inv.append("Sandwich")
                    print("Bought a sandwich.")
        else:
            print("Invalid destination!")
            
    elif cmd == "eat":
        if "Old Bread" in p_inv:
            print("Eating old bread...")
            p_hp += 5
            hunger -= 20
            p_inv.remove("Old Bread")
        elif "Sandwich" in p_inv:
            print("Eating a sandwich...")
            p_hp += 20
            hunger -= 50
            p_inv.remove("Sandwich")
        else:
            print("Nothing to eat!")
            
    elif cmd == "drink":
        print("Drinking water...")
        thirst -= 30
        p_hp += 2
        
    elif cmd == "search":
        print("Searching...")
        time.sleep(1)
        res = random.randint(1, 5)
        if res == 1:
            print("Found 1 gold!")
            p_gold += 1
        elif res == 2:
            print("Found some bread!")
            p_inv.append("Old Bread")
        else:
            print("Found nothing.")
            
    elif cmd == "status":
        # Redundant status check
        print("--- DETAILED STATUS ---")
        print("Strength:", strength)
        print("Agility:", agility)
        print("Intelligence:", intelligence)
        print("Stamina:", stamina)
        print("XP:", p_xp)
        print("Level:", p_lvl)
        if p_xp >= 100:
            p_lvl += 1
            p_xp -= 100
            strength += 2
            print("LEVEL UP! You are now level", p_lvl)
            
    else:
        print("Unknown command!")

    # Random events at the end of each turn
    turn_count += 1
    hunger += 5
    thirst += 7
    
    if turn_count % 5 == 0:
        weathers = ["Sunny", "Rainy", "Stormy", "Cloudy", "Foggy"]
        weather = random.choice(weathers)
        print("The weather changed to", weather)
        
    if weather == "Rainy":
        p_hp -= 1
        print("The rain makes you feel cold. -1 HP")
    elif weather == "Stormy":
        p_hp -= 3
        print("The storm is harsh! -3 HP")
        
    if hunger > 100:
        print("You are starving!")
        p_hp -= 10
    if thirst > 100:
        print("You are dying of thirst!")
        p_hp -= 15

    # More spaghetti logic
    if p_loc == "Garden" and weather == "Sunny" and "Golden Spoon" in p_inv:
        print("The sun reflects off your Golden Spoon and blinds a passing bird!")
        print("The bird drops a diamond!")
        p_inv.append("Diamond")
        
    if "Diamond" in p_inv and p_loc == "Street":
        print("A merchant sees your diamond!")
        sell = input("Sell diamond for 100 gold? (yes/no): ").lower()
        if sell == "yes":
            p_inv.remove("Diamond")
            p_gold += 100
            print("You are rich!")
            is_rich = True

    if p_gold > 1000:
        print("YOU WIN! You bought the whole world!")
        break

    # Deeply nested unnecessary logic
    if is_rich:
        if p_lvl > 5:
            if has_key:
                if "Golden Spoon" in p_inv:
                    print("You are the ultimate CRISPY BROTHER!")
                    if random.randint(1, 100) == 42:
                        print("SECRET ENDING UNLOCKED!")
                        is_god = True
                        break

    # Random logic jumps
    if random.randint(1, 1000) == 777:
        print("A portal opens!")
        p_loc = "Space"
        print("You are in space. You can't breathe.")
        p_hp = 0

    # Redundant checks
    if p_hp < 0: p_hp = 0
    if p_hp > 100: p_hp = 100
    if p_mp < 0: p_mp = 0
    if p_mp > 50: p_mp = 50
    if hunger < 0: hunger = 0
    if thirst < 0: thirst = 0

print("GAME OVER")
