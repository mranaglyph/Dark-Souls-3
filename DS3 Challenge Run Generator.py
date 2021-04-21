#Name : DS3 Challenge Run Generator 
#Original Author : mranaglyph (interdim_designs)
#Date : 4/20/2021

#import random module for selecting from the created lists later
import random

text_color = '\033[3;32m' #assigning green, italic text variable with ANSI
default = '\033[m' #assigning default text color and style with ANSI

#creating the multiple lists that determine the possible challenges of the run
char_param = ['SL1', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Perma-Death (1 Life, End Playthrough on Death)', 'Cat Cosplay (9 Lives, Perma-Death)', 'Hail Mary (3 Lives, Perma-Death)', 'No Leveling Vigor', 'No Leveling Endurance', 'Int Build', 'Faith Build', 'Pyro Build', 'No Leveling Vit', 'Soul Level Cap = 10 + Highest Weapon Requirement', 'Soul Level Cap = 20 + Highest Weapon Requirement', 'Soul Level Cap = 30 + Highest Weapon Requirement', 'All Bosses Required (Including DLC, If Possible)']
sl1 = ['Longsword', 'Shortsword', 'Broadsword']
armor_param = ['No Armor Allowed', 'Any Armor Allowed', 'Starting Armor Only', 'Armor with Weight >= 10 Only', 'Armor with Weight <= 3 Only', 'Fashion Souls (Always Wear a Complete Set)', "Mix n' Match Souls (One Piece of Armor per Set)"]
weapon_param = ['Fist Only', 'Starting Weapon Only', "Aquamarine Dagger", "Bandit's Knife", "Brigand Twindaggers", "Corvian Greatknife", "Dagger","Handmaid's Dagger", "Harpe", "Mail Breaker", "Murky Hand Scythe", "Parrying Dagger", "Rotten Ghru Dagger", "Scholar's Candlestick", "Tailbone Short Sword", "Straight Swords", "Anri's Straight Sword", "Astora Straight Sword", "Barbed Straight Sword", "Broadsword", "Broken Straight Sword", "Cleric's Candlestick", "Dark Sword", "Gotthard Twinswords", "Irithyll Straight Sword", "Long Sword", "Lothric's Holy Sword", "Lothric Knight Sword", "Morion Blade", "Ringed Knight Straight Sword", "Shortsword", "Sunlight Straight Sword", "Valorheart", "Any Greatsword", "Bastard Sword", "Black Knight Sword", "Claymore", "Drakeblood Greatsword", "Executioner's Greatsword", "Firelink Greatsword", "Flamberge", "Gael's Greatsword", "Greatsword of Judgment", "Hollowslayer Greatsword", "Moonlight Greatsword", "Onyx Blade", "Storm Ruler", "Twin Princes' Greatsword", "Wolf Knight's Greatsword", "Wolnir's Holy Sword", "Any Ultra Greatsword", "Astora Greatsword", "Black Knight Greatsword", "Cathedral Knight Greatsword", "Farron Greatsword", "Fume Ultra Greatsword", "Greatsword", "Lorian's Greatsword", "Lothric Knight Greatsword", "Profaned Greatsword", "Ringed Knight Paired Greatswords", "Zweihander", "Curved Blades", "Any Curved Sword", "Carthus Curved Sword", "Carthus Shotel", "Crescent Moon Sword", "Dancer's Enchanted Swords", "Falchion", "Follower Sabre", "Painting Guardian's Curved Sword", "Pontiff Knight Curved Sword", "Rotten Ghru Curved Sword", "Scimitar", "Sellsword Twinblades", "Shotel", "Storm Curved Sword", "Warden Twinblades", "Any Curved Greatsword", "Carthus Curved Greatsword", "Exile Greatsword", "Harald Curved Greatsword", "Murakumo", "Old Wolf Curved Sword", "Crow Quills", "Crystal Sage's Rapier", "Estoc", "Irithyll Rapier", "Rapier", "Ricard's Rapier", "Any Katana", "Black Blade", "Bloodlust", "Chaos Blade", "Darkdrift", "Frayed Blade", "Onikiri and Ubadachi", "Uchigatana", "Washing Pole", "Any Axe", "Battle Axe", "Brigand Axe", "Butcher Knife", "Dragonslayer's Axe", "Eleonora", "Hand Axe", "Man Serpent Hatchet", "Millwood Battle Axe", "Thrall Axe", "Winged Knight Twinaxes", "Any Greataxe", "Black Knight Greataxe", "Demon's Greataxe", "Dragonslayer Greataxe", "Earth Seeker", "Greataxe", "Great Machete", "Yhorm's Great Machete", "Any Hammer", "Blacksmith Hammer", "Club", "Drang Hammers", "Heysel Pick", "Mace", "Morning Star", "Reinforced Club", "Warpick", "Great Hammers", "Dragon Tooth", "Gargoyle Flame Hammer", "Great Mace", "Great Wooden Hammer", "Large Club", "Ledo's Great Hammer", "Morne's Great Hammer", "Old King's Great Hammer", "Pickaxe", "Quakestone Hammer", "Smough's Great Hammer", "Spiked Mace", "Vordt's Great Hammer", "Polearms", "Any Spear", "Arstor's Spear", "Dragonslayer Spear", "Dragonslayer Swordspear", "Drang Twinspears", "Follower Javelin", "Four-Pronged Plow", "Gargoyle Flame Spear", "Golden Ritual Spear", "Partizan", "Rotten Ghru Spear", "Saint Bident", "Soldering Iron", "Tailbone Spear", "Winged Spear", "Yorshka's Spear", "Greatlance", "Lothric Knight Long Spear", "Lothric War Banner", "Pike", "Ringed Knight Spear", "Any Halberd", "Black Knight Glaive", "Crescent Axe", "Crucifix of the Mad King", "Glaive", "Gundyr's Halberd", "Halberd", "Immolation Tinder", "Lucerne", "Red Hilted Halberd", "Splitleaf Greatsword", "Winged Knight Halberd", "Any Scythe", "Friede's Great Scythe", "Great Corvian Scythe", "Great Scythe", "Pontiff Knight Great Scythe", "Any Whip", "Notched Whip", "Rose of Ariandel", "Spotted Whip", "Whip", "Any Claw", "Caestus", "Dark Hand", "Demon's Fist", "Claw", "Crow Talons", "Manikin Claws", "Any Weapon"]
weapon_param2 = ['WA Allowed (If Possible)', 'WA Allowed (If Possible)', 'WA Allowed (If Possible)', 'WA Allowed (If Possible)', 'WA Allowed (If Possible)', 'WA Allowed (If Possible)', 'No WA Allowed', 'Only WA Attack Allowed (If Possible)']
staves = ["Archdeacon's Great Staff", "Court Sorcerer's Staff", "Heretic's Staff", "Izalith Staff", "Man-grub's Staff", "Mendicant's Staff", "Murky Longstaff", "Preacher's Right Arm", "Sage's Crystal Staff", "Sorcerer's Staff", "Storyteller's Staff", "Witchtree Branch"]
chimes = ["Caitha's Chime", "Cleric's Sacred Chime", 'Crystal Chime', "Priest's Chime", "Sacred Chime of Filianore", 'Saint-Tree Bellvine', "Yorshka's Chime"]
talismans = ['Canvas Talisman', "Saint's Talisman", 'Sunless Talisman', 'Sunlight Talisman', 'Talisman', 'White Hair Talisman']
pyro = ['Pyromancy Flame', "Pyromancer's Parting Flame"]
misc_param = ['Only Glitches Allowed [No Exploits or Skips]', 'Only Exploits Allowed [No Glitches or Skips]', 'Only Skips Allowed [No Glitches or Exploits]', 'No Glitches/Exploits/Skips Allowed', 'All Glitches/Exploits/Skips Allowed']
equip_param = ['All Equipment Upgrades Allowed', 'No Equipment Upgrades Allowed', 'Weapon Upgradable [Not Shield]', 'Shield Upgradable [Not Weapon]', 'Weapon Upgradable +3 (No Upgrades for Special Weapons)', 'Weapon Upgradable +6 (+3 for Special Weapon)' ]
shield = ['No Shields Allowed', 'Any Shield Allowed', 'No Parrying Shields', 'No "Weapon Skill" [WA] Shield', 'Greatshields Only', 'Parry Shields Only']
addtl = ['Reallocate Stats Allowed (If Possible)', 'Reallocate Stats Not Allowed (Even If Possible)']
consumables = ['Consumables Allowed', 'No Consumables Allowed', 'Only [RNG] Dropped Consumables Allowed', 'Only Purchased Consumables Allowed']
rings = ['Any/All Rings Allowed', 'One Ring Allowed', 'Two Rings Allowed', 'Three Rings Allowed', 'Only Rings with Negative Side/Main Effect(s) Allowed', 'Unupgraded Rings Only']
keys = ['Optional Key Items Must Be Skipped', 'Optional Key Items Must Be Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained']
estus = ['Estus Flask(s) Can Be Fully Upgraded', 'Estus Flask(s) Cannot Be Upgraded', 'Estus Flask(s) Cannot Be Upgraded Past +1', 'Estus Flask(s) Cannot Be Upgraded Past +2', 'Estus Flask(s) Cannot Be Upgraded Past +3', 'Estus Flask(s) Cannot Be Upgraded Past +4', 'Estus Flask(s) Cannot Be Upgraded Past +5', 'Estus Flask(s) Cannot Be Upgraded Past +6', 'Estus Flask(s) Cannot Be Upgraded Past +7', 'Estus Flask(s) Cannot Be Upgraded Past +8', 'Estus Flask(s) Cannot Be Upgraded Past +9']

#creating while loop so user can re-roll for a different challenge if they wish
while True:
    roll = input('\nRoll for a DS3 Challenge? [Y/N] : ')
    
    if (roll == 'y') or (roll == 'Y'):
        
        #randomly chooses the character parameter, but additional restrictions are needed for SL1, Int/Faith/Pyro Builds 
        character_restriction = random.choice(char_param)
        
        if character_restriction == 'SL1':

            #random list choices are decided and saved to variables to be called/printed later
            #this is the same process for all elif
            soul_level_one_restriction = random.choice(sl1)
            weapon_restriction_two = random.choice(weapon_param2)
            shield_restriction = random.choice(shield)
            equip_restriction = random.choice(equip_param)
            armor_restriction = random.choice(armor_param)
            rings_restriction = random.choice(rings)
            estus_restriction = random.choice(estus)
            consumables_restriction = random.choice(consumables)
            key_restriction = random.choice(keys)
            additional_restriction = random.choice(addtl)
            misc_restriction = random.choice(misc_param)
            
            #print output of the list choices for the user to see the challenge run provided
            #this is the same process for all elif
            print('\nCharacter Restriction : ', text_color + character_restriction, default)
            print('\nWeapon to Use : ', text_color + soul_level_one_restriction, default)
            print('\nWeapon Restriction : ', text_color + weapon_restriction_two, default)
            print('\nShield Restriction : ', text_color + shield_restriction, default)
            print('\nEquipment Restriction : ', text_color + equip_restriction, default)
            print('\nArmor Restriction : ', text_color + armor_restriction, default)
            print('\nRings Restriction : ', text_color + rings_restriction, default)
            print('\nEstus Restriction : ', text_color + estus_restriction, default)
            print('\nConsumables Restriction : ', text_color + consumables_restriction, default)
            print('\nKey Item Restriction : ', text_color + key_restriction, default)
            print('\nAdditional Restrictions : ', text_color + additional_restriction, default)
            print('\nMisc Restriction : ', text_color + misc_restriction, default)
            continue
            
        elif character_restriction == 'Int Build':
            staves_restriction = random.choice(staves)
            weapon_restriction_two = random.choice(weapon_param2)
            shield_restriction = random.choice(shield)
            equip_restriction = random.choice(equip_param)
            armor_restriction = random.choice(armor_param)
            rings_restriction = random.choice(rings)
            estus_restriction = random.choice(estus)
            consumables_restriction = random.choice(consumables)
            key_restriction = random.choice(keys)
            additional_restriction = random.choice(addtl)
            misc_restriction = random.choice(misc_param)
            
            print('\nCharacter Restriction : ', text_color + character_restriction, default)
            print('\nWeapon to Use : ', text_color + staves_restriction, default)
            print('\nWeapon Restriction : ', text_color + weapon_restriction_two, default)
            print('\nShield Restriction : ', text_color + shield_restriction, default)
            print('\nEquipment Restriction : ', text_color + equip_restriction, default)
            print('\nArmor Restriction : ', text_color + armor_restriction, default)
            print('\nRings Restriction : ', text_color + rings_restriction, default)
            print('\nEstus Restriction : ', text_color + estus_restriction, default)
            print('\nConsumables Restriction : ', text_color + consumables_restriction, default)
            print('\nKey Item Restriction : ', text_color + key_restriction, default)
            print('\nAdditional Restrictions : ', text_color + additional_restriction, default)
            print('\nMisc Restriction : ', text_color + misc_restriction, default)
            continue
            
        elif character_restriction == 'Faith Build':
            chimes_restriction = random.choice(chimes)
            weapon_restriction_two = random.choice(weapon_param2)
            shield_restriction = random.choice(shield)
            equip_restriction = random.choice(equip_param)
            armor_restriction = random.choice(armor_param)
            rings_restriction = random.choice(rings)
            estus_restriction = random.choice(estus)
            consumables_restriction = random.choice(consumables)
            key_restriction = random.choice(keys)
            additional_restriction = random.choice(addtl)
            misc_restriction = random.choice(misc_param)
            
            print('\nCharacter Restriction : ', text_color + character_restriction, default)
            print('\nWeapon to Use : ', text_color + chimes_restriction, default)
            print('\nWeapon Restriction : ', text_color + weapon_restriction_two, default)
            print('\nShield Restriction : ', text_color + shield_restriction, default)
            print('\nEquipment Restriction : ', text_color + equip_restriction, default)
            print('\nArmor Restriction : ', text_color + armor_restriction, default)
            print('\nRings Restriction : ', text_color + rings_restriction, default)
            print('\nEstus Restriction : ', text_color + estus_restriction, default)
            print('\nConsumables Restriction : ', text_color + consumables_restriction, default)
            print('\nKey Item Restriction : ', text_color + key_restriction, default)
            print('\nAdditional Restrictions : ', text_color + additional_restriction, default)
            print('\nMisc Restriction : ', text_color + misc_restriction, default)
            continue
            
        elif character_restriction == 'Pyro Build':
            pyro_restriction = random.choice(pyro)
            weapon_restriction_two = random.choice(weapon_param2)
            shield_restriction = random.choice(shield)
            equip_restriction = random.choice(equip_param)
            armor_restriction = random.choice(armor_param)
            rings_restriction = random.choice(rings)
            estus_restriction = random.choice(estus)
            consumables_restriction = random.choice(consumables)
            key_restriction = random.choice(keys)
            additional_restriction = random.choice(addtl)
            misc_restriction = random.choice(misc_param)
            
            print('\nCharacter Restriction : ', text_color + character_restriction, default)
            print('\nWeapon to Use : ', text_color + pyro_restriction, default)
            print('\nWeapon Restriction : ', text_color + weapon_restriction_two, default)
            print('\nShield Restriction : ', text_color + shield_restriction, default)
            print('\nEquipment Restriction : ', text_color + equip_restriction, default)
            print('\nArmor Restriction : ', text_color + armor_restriction, default)
            print('\nRings Restriction : ', text_color + rings_restriction, default)
            print('\nEstus Restriction : ', text_color + estus_restriction, default)
            print('\nConsumables Restriction : ', text_color + consumables_restriction, default)
            print('\nKey Item Restriction : ', text_color + key_restriction, default)
            print('\nAdditional Restrictions : ', text_color + additional_restriction, default)
            print('\nMisc Restriction : ', text_color + misc_restriction, default)
            continue
            
        else:
            weapon_restriction = random.choice(weapon_param)
            weapon_restriction_two = random.choice(weapon_param2)
            shield_restriction = random.choice(shield)
            equip_restriction = random.choice(equip_param)
            armor_restriction = random.choice(armor_param)
            rings_restriction = random.choice(rings)
            estus_restriction = random.choice(estus)
            consumables_restriction = random.choice(consumables)
            key_restriction = random.choice(keys)
            additional_restriction = random.choice(addtl)
            misc_restriction = random.choice(misc_param)
            
            print('\nCharacter Restriction : ', text_color + character_restriction, default)
            print('\nWeapon to Use : ', text_color + weapon_restriction, default)
            print('\nWeapon Restriction : ', text_color + weapon_restriction_two, default)
            print('\nShield Restriction : ', text_color + shield_restriction, default)
            print('\nEquipment Restriction : ', text_color + equip_restriction, default)
            print('\nArmor Restriction : ', text_color + armor_restriction, default)
            print('\nRings Restriction : ', text_color + rings_restriction, default)
            print('\nEstus Restriction : ', text_color + estus_restriction, default)
            print('\nConsumables Restriction : ', text_color + consumables_restriction, default)
            print('\nKey Item Restriction : ', text_color + key_restriction, default)
            print('\nAdditional Restrictions : ', text_color + additional_restriction, default)
            print('\nMisc Restriction : ', text_color + misc_restriction, default)
            continue
    
    #giving the user the option to break out of the while loop and end the program
    elif (roll == 'n') or (roll == 'N'):
        break
        exit()
    
    #in case the user inputs something other than 'y' or 'n' sends user back to top of while loop
    else:
        print('\nValue Not Recognized')
    continue