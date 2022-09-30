####################################################################
#Imports
####################################################################
import random as r
import tkinter as tk

####################################################################
#Root Tkinter Setup
####################################################################
root = tk.Tk()
root.title("Dark Souls 3 : Challenge Run Generator 2")
root.geometry("1024x570")
root.resizable(False, False)

bgColorCanvas = "gray9"
bgColorLabel = "gray12"
bgColorButton = "gray12"
bgColorField = "gray15"

textColor = 'DarkOrange2'

root.configure(bg=bgColorCanvas)

####################################################################
#Labels
####################################################################
restriction1 = tk.Label(root, text="Character and Weapon", bg=bgColorLabel, fg=textColor)
restriction1.grid(column=0, row=0)

restriction2 = tk.Label(root, text="Shield Usage", bg=bgColorLabel, fg=textColor)
restriction2.grid(column=0, row=2)

restriction3 = tk.Label(root, text="Weapon/Shield Upgrade", bg=bgColorLabel, fg=textColor)
restriction3.grid(column=0, row=4)

restriction4 = tk.Label(root, text="Weapon Arts", bg=bgColorLabel, fg=textColor)
restriction4.grid(column=0, row=6)

restriction5 = tk.Label(root, text="Armor Usage", bg=bgColorLabel, fg=textColor)
restriction5.grid(column=0, row=8)

restriction6 = tk.Label(root, text="Ring Usage", bg=bgColorLabel, fg=textColor)
restriction6.grid(column=0, row=10)

restriction7 = tk.Label(root, text="Estus Upgrade", bg=bgColorLabel, fg=textColor)
restriction7.grid(column=0, row=12)

restriction8 = tk.Label(root, text="Consumable Usage", bg=bgColorLabel, fg=textColor)
restriction8.grid(column=0, row=14)

restriction9 = tk.Label(root, text="Keys", bg=bgColorLabel, fg=textColor)
restriction9.grid(column=0, row=16)

restriction10 = tk.Label(root, text="Reallocation", bg=bgColorLabel, fg=textColor)
restriction10.grid(column=0, row=18)

restriction11 = tk.Label(root, text="Misc", bg=bgColorLabel, fg=textColor)
restriction11.grid(column=0, row=20)

restriction12 = tk.Label(root, text="Side Quest", bg=bgColorLabel, fg=textColor)
restriction12.grid(column=0, row=22)

####################################################################
#Text Fields
####################################################################
restriction1Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction1Display.grid(column=1, row=1)

restriction2Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction2Display.grid(column=1, row=3)

restriction3Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction3Display.grid(column=1, row=5)

restriction4Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction4Display.grid(column=1, row=7)

restriction5Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction5Display.grid(column=1, row=9)

restriction6Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction6Display.grid(column=1, row=11)

restriction7Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction7Display.grid(column=1, row=13)

restriction8Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction8Display.grid(column=1, row=15)

restriction9Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction9Display.grid(column=1, row=17)

restriction10Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction10Display.grid(column=1, row=19)

restriction11Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction11Display.grid(column=1, row=21)

restriction12Display = tk.Text(root, height=1, width=10, bg=bgColorField, fg=textColor)
restriction12Display.grid(column=1, row=23)

####################################################################
#Functions
####################################################################
def deleteCharParamChallenge():
    restriction1Display.config(state="normal")
    restriction1Display.delete("1.0", "end")
    restriction1Display.config(state="disabled")

def charParamChallenge():
    deleteCharParamChallenge()

    charParam = ['Soul Level 1', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Normal SL Progression', 'Perma-Death (1 Life, End Playthrough on Death)', 'Cat Cosplay (9 Lives, Perma-Death)', 'Hail Mary (3 Lives, Perma-Death)', 'No Leveling (Vigor)', 'No Leveling (Endurance)', 'Int Build', 'Faith Build', 'Pyro Build', 'No Leveling (Vitality)', 'Soul Level Cap = 10 + (Highest Weapon Requirement of Weapon)', 'Soul Level Cap = 20 + (Highest Weapon Requirement of Weapon)', 'Soul Level Cap = 30 + (Highest Weapon Requirement of Weapon)']
    characterRestriction = r.choice(charParam)
    
    if characterRestriction == "Soul Level 1":
        sl1 = ['Longsword', 'Shortsword', 'Broadsword']
        weapon = r.choice(sl1)
    
    elif characterRestriction == "Int Build":
        staves = ["Archdeacon's Great Staff", "Court Sorcerer's Staff", "Heretic's Staff", "Izalith Staff", "Man-grub's Staff", "Mendicant's Staff", "Murky Longstaff", "Preacher's Right Arm", "Sage's Crystal Staff", "Sorcerer's Staff", "Storyteller's Staff", "Witchtree Branch"]
        weapon = r.choice(staves)
    
    elif characterRestriction == "Faith Build":
        chimes = ["Caitha's Chime", "Cleric's Sacred Chime", 'Crystal Chime', "Priest's Chime", "Sacred Chime of Filianore", 'Saint-Tree Bellvine', "Yorshka's Chime"]
        talismans = ['Canvas Talisman', "Saint's Talisman", 'Sunless Talisman', 'Sunlight Talisman', 'Talisman', 'White Hair Talisman']
        coin = r.randrange(1, 3) #random number 1 included, and 3 not included
        if coin == 1:
            weapon = r.choice(chimes)
        else:
            weapon = r.choice(talismans)

    elif characterRestriction == "Pyro Build":
        pyro = ['Pyromancy Flame', "Pyromancer's Parting Flame"]
        weapon = r.choice(pyro)
    
    else:
        weaponParam = ['Fist Only', 'Starting Weapon Only', "Any Dagger", "Aquamarine Dagger", "Bandit's Knife", "Brigand Twindaggers", "Corvian Greatknife", "Dagger","Handmaid's Dagger", "Harpe", "Mail Breaker", "Murky Hand Scythe", "Parrying Dagger", "Rotten Ghru Dagger", "Scholar's Candlestick", "Tailbone Short Sword", "Any Straight Sword", "Anri's Straight Sword", "Astora Straight Sword", "Barbed Straight Sword", "Broadsword", "Broken Straight Sword", "Cleric's Candlestick", "Dark Sword", "Gotthard Twinswords", "Irithyll Straight Sword", "Long Sword", "Lothric's Holy Sword", "Lothric Knight Sword", "Morion Blade", "Ringed Knight Straight Sword", "Shortsword", "Sunlight Straight Sword", "Valorheart", "Any Greatsword", "Bastard Sword", "Black Knight Sword", "Claymore", "Drakeblood Greatsword", "Executioner's Greatsword", "Firelink Greatsword", "Flamberge", "Gael's Greatsword", "Greatsword of Judgment", "Hollowslayer Greatsword", "Moonlight Greatsword", "Onyx Blade", "Storm Ruler", "Twin Princes' Greatsword", "Wolf Knight's Greatsword", "Wolnir's Holy Sword", "Any Ultra Greatsword", "Astora Greatsword", "Black Knight Greatsword", "Cathedral Knight Greatsword", "Farron Greatsword", "Fume Ultra Greatsword", "Greatsword", "Lorian's Greatsword", "Lothric Knight Greatsword", "Profaned Greatsword", "Ringed Knight Paired Greatswords", "Zweihander", "Any Curved Sword", "Carthus Curved Sword", "Carthus Shotel", "Crescent Moon Sword", "Dancer's Enchanted Swords", "Falchion", "Follower Sabre", "Painting Guardian's Curved Sword", "Pontiff Knight Curved Sword", "Rotten Ghru Curved Sword", "Scimitar", "Sellsword Twinblades", "Shotel", "Storm Curved Sword", "Warden Twinblades", "Any Curved Greatsword", "Carthus Curved Greatsword", "Exile Greatsword", "Harald Curved Greatsword", "Murakumo", "Old Wolf Curved Sword", "Any Thrusting Sword", "Crow Quills", "Crystal Sage's Rapier", "Estoc", "Irithyll Rapier", "Rapier", "Ricard's Rapier", "Any Katana", "Black Blade", "Bloodlust", "Chaos Blade", "Darkdrift", "Frayed Blade", "Onikiri and Ubadachi", "Uchigatana", "Washing Pole", "Any Axe", "Battle Axe", "Brigand Axe", "Butcher Knife", "Dragonslayer's Axe", "Eleonora", "Hand Axe", "Man Serpent Hatchet", "Millwood Battle Axe", "Thrall Axe", "Winged Knight Twinaxes", "Any Greataxe", "Black Knight Greataxe", "Demon's Greataxe", "Dragonslayer Greataxe", "Earth Seeker", "Greataxe", "Great Machete", "Yhorm's Great Machete", "Any Hammer", "Blacksmith Hammer", "Club", "Drang Hammers", "Heysel Pick", "Mace", "Morning Star", "Reinforced Club", "Warpick", "Great Hammers", "Dragon Tooth", "Gargoyle Flame Hammer", "Great Mace", "Great Wooden Hammer", "Large Club", "Ledo's Great Hammer", "Morne's Great Hammer", "Old King's Great Hammer", "Pickaxe", "Quakestone Hammer", "Smough's Great Hammer", "Spiked Mace", "Vordt's Great Hammer", "Any Spear or Pike", "Arstor's Spear", "Dragonslayer Spear", "Dragonslayer Swordspear", "Drang Twinspears", "Follower Javelin", "Four-Pronged Plow", "Gargoyle Flame Spear", "Golden Ritual Spear", "Partizan", "Rotten Ghru Spear", "Saint Bident", "Soldering Iron", "Tailbone Spear", "Winged Spear", "Yorshka's Spear", "Greatlance", "Lothric Knight Long Spear", "Lothric War Banner", "Pike", "Ringed Knight Spear", "Any Halberd", "Black Knight Glaive", "Crescent Axe", "Crucifix of the Mad King", "Glaive", "Gundyr's Halberd", "Halberd", "Immolation Tinder", "Lucerne", "Red Hilted Halberd", "Splitleaf Greatsword", "Winged Knight Halberd", "Any Scythe", "Friede's Great Scythe", "Great Corvian Scythe", "Great Scythe", "Pontiff Knight Great Scythe", "Any Whip", "Notched Whip", "Rose of Ariandel", "Spotted Whip", "Whip", "Witch's Locks", "Any Claw or Fist Weapon", "Caestus", "Dark Hand", "Demon's Fist", "Claw", "Crow Talons", "Manikin Claws", "Any Bow", "Any Greatbow", "Any Crossbow", "Any Weapon"]
        weapon = r.choice(weaponParam)

    text1Display = "{} with {}".format(characterRestriction, weapon)
    text1DisplayLen = len(text1Display)
    restriction1Display.config(width=text1DisplayLen+1)
    restriction1Display.config(state="normal")
    restriction1Display.insert("1.0", text1Display)
    restriction1Display.config(state="disabled")

def deleteShieldChallenge():
    restriction2Display.config(state="normal")
    restriction2Display.delete("1.0", "end")
    restriction2Display.config(state="disabled")

def shieldChallenge():
    deleteShieldChallenge()

    shield = ['No Shields Allowed', 'Any Shield Allowed', 'No Parrying Shields', 'No "Weapon Skill" [WA] Shield', 'Greatshields Only', 'Parry Shields Only']
    shieldRestriction = r.choice(shield)

    text2Display = "{}".format(shieldRestriction)
    text2DisplayLen = len(text2Display)
    restriction2Display.config(width=text2DisplayLen+1)
    restriction2Display.config(state="normal")
    restriction2Display.insert("1.0", text2Display)
    restriction2Display.config(state="disabled")

def deleteUpgradeChallenge():
    restriction3Display.config(state="normal")
    restriction3Display.delete("1.0", "end")
    restriction3Display.config(state="disabled")

def upgradeChallenge():
    deleteUpgradeChallenge()

    upgrades = ['All Equipment Upgrades Allowed', 'No Equipment Upgrades Allowed', 'Weapon Upgradable [Not Shield]', 'Shield Upgradable [Not Weapon]', 'Weapon Upgradable +3 (No Upgrades for Special Weapons)', 'Weapon Upgradable +6 (+3 for Special Weapon)' ]
    upgradeRestriction = r.choice(upgrades)

    text3Display = "{}".format(upgradeRestriction)
    text3DisplayLen = len(text3Display)
    restriction3Display.config(width=text3DisplayLen+1)
    restriction3Display.config(state="normal")
    restriction3Display.insert("1.0", text3Display)
    restriction3Display.config(state="disabled")

def deleteWeaponArtChallenge():
    restriction4Display.config(state="normal")
    restriction4Display.delete("1.0", "end")
    restriction4Display.config(state="disabled")

def weaponArtChallenge():
    deleteWeaponArtChallenge()

    weaponArt = ['WA Allowed', 'WA Allowed', 'WA Allowed', 'WA Allowed', 'WA Allowed', 'WA Allowed', 'No WA Allowed', 'Only WA Attack Allowed (If/When Possible)']
    weaponArtRestriction = r.choice(weaponArt)

    text4Display = "{}".format(weaponArtRestriction)
    text4DisplayLen = len(text4Display)
    restriction4Display.config(width=text4DisplayLen+1)
    restriction4Display.config(state="normal")
    restriction4Display.insert("1.0", text4Display)
    restriction4Display.config(state="disabled")

def deleteArmorChallenge():
    restriction5Display.config(state="normal")
    restriction5Display.delete("1.0", "end")
    restriction5Display.config(state="disabled")

def armorChallenge():
    deleteArmorChallenge()

    armor = ['No Armor Allowed', 'Any Armor Allowed', 'Starting Armor Only', 'Armor with Weight >= 10 Only [Per Piece]', 'Armor with Weight <= 3 Only [Per Piece]', 'Fashion Souls (Always Wear a Complete Set)', "Mix n' Match Souls (One Piece of Armor per Set)"]
    armorRestriction = r.choice(armor)

    text5Display = "{}".format(armorRestriction)
    text5DisplayLen = len(text5Display)
    restriction5Display.config(width=text5DisplayLen+1)
    restriction5Display.config(state="normal")
    restriction5Display.insert("1.0", text5Display)
    restriction5Display.config(state="disabled")

def deleteRingChallenge():
    restriction6Display.config(state="normal")
    restriction6Display.delete("1.0", "end")
    restriction6Display.config(state="disabled")

def ringChallenge():
    deleteRingChallenge()

    rings = ['Any/All Rings Allowed', 'One Ring Allowed', 'Two Rings Allowed', 'Three Rings Allowed', 'Only Rings with Negative Side/Main Effect(s) Allowed', 'Unupgraded Rings Only']
    ringRestriction = r.choice(rings)

    text6Display = "{}".format(ringRestriction)
    text6DisplayLen = len(text6Display)
    restriction6Display.config(width=text6DisplayLen+1)
    restriction6Display.config(state="normal")
    restriction6Display.insert("1.0", text6Display)
    restriction6Display.config(state="disabled")

def deleteEstusChallenge():
    restriction7Display.config(state="normal")
    restriction7Display.delete("1.0", "end")
    restriction7Display.config(state="disabled")

def estusChallenge():
    deleteEstusChallenge()

    estus = ['Estus Flask(s) Can Be Fully Upgraded', 'Estus Flask(s) Cannot Be Upgraded', 'Estus Flask(s) Cannot Be Upgraded Past +1', 'Estus Flask(s) Cannot Be Upgraded Past +2', 'Estus Flask(s) Cannot Be Upgraded Past +3', 'Estus Flask(s) Cannot Be Upgraded Past +4', 'Estus Flask(s) Cannot Be Upgraded Past +5', 'Estus Flask(s) Cannot Be Upgraded Past +6', 'Estus Flask(s) Cannot Be Upgraded Past +7', 'Estus Flask(s) Cannot Be Upgraded Past +8', 'Estus Flask(s) Cannot Be Upgraded Past +9']
    estusRestriction = r.choice(estus)

    text7Display = "{}".format(estusRestriction)
    text7DisplayLen = len(text7Display)
    restriction7Display.config(width=text7DisplayLen+1)
    restriction7Display.config(state="normal")
    restriction7Display.insert("1.0", text7Display)
    restriction7Display.config(state="disabled")

def deleteConsumableChallenge():
    restriction8Display.config(state="normal")
    restriction8Display.delete("1.0", "end")
    restriction8Display.config(state="disabled")

def consumableChallenge():
    deleteConsumableChallenge()

    consumables = ['Consumables Allowed', 'No Consumables Allowed [Upgrade Material Exempt]', 'Only [RNG] Dropped Consumables Allowed [Upgrade Material Exempt]', 'Only Purchased Consumables Allowed [Upgrade Material Exempt]']
    consumableRestriction = r.choice(consumables)

    text8Display = "{}".format(consumableRestriction)
    text8DisplayLen = len(text8Display)
    restriction8Display.config(width=text8DisplayLen+1)
    restriction8Display.config(state="normal")
    restriction8Display.insert("1.0", text8Display)
    restriction8Display.config(state="disabled")

def deleteKeysChallenge():
    restriction9Display.config(state="normal")
    restriction9Display.delete("1.0", "end")
    restriction9Display.config(state="disabled")

def keysChallenge():
    deleteKeysChallenge()

    keys = ['Optional Key Items Must Be Skipped', 'Optional Key Items Must Be Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained', 'Optional Key Items Can Be Skipped or Obtained']
    keysRestriction = r.choice(keys)

    text9Display = "{}".format(keysRestriction)
    text9DisplayLen = len(text9Display)
    restriction9Display.config(width=text9DisplayLen+1)
    restriction9Display.config(state="normal")
    restriction9Display.insert("1.0", text9Display)
    restriction9Display.config(state="disabled")

def deleteReallocationChallenge():
    restriction10Display.config(state="normal")
    restriction10Display.delete("1.0", "end")
    restriction10Display.config(state="disabled")

def reallocationChallenge():
    deleteReallocationChallenge()

    realloc = ['Reallocate Stats Allowed (If Possible)', 'Reallocate Stats Not Allowed (Even If Possible)']
    reallocationRestriction = r.choice(realloc)

    text10Display = "{}".format(reallocationRestriction)
    text10DisplayLen = len(text10Display)
    restriction10Display.config(width=text10DisplayLen+1)
    restriction10Display.config(state="normal")
    restriction10Display.insert("1.0", text10Display)
    restriction10Display.config(state="disabled")

def deleteMiscChallenge():
    restriction11Display.config(state="normal")
    restriction11Display.delete("1.0", "end")
    restriction11Display.config(state="disabled")

def miscChallenge():
    deleteMiscChallenge()

    misc = ['Only Glitches Allowed [No Exploits or Skips]', 'Only Exploits Allowed [No Glitches or Skips]', 'Only Skips Allowed [No Glitches or Exploits]', 'No Glitches/Exploits/Skips Allowed', 'All Glitches/Exploits/Skips Allowed']
    miscRestriction = r.choice(misc)

    text11Display = "{}".format(miscRestriction)
    text11DisplayLen = len(text11Display)
    restriction11Display.config(width=text11DisplayLen+1)
    restriction11Display.config(state="normal")
    restriction11Display.insert("1.0", text11Display)
    restriction11Display.config(state="disabled")

def deleteSideQuest():
    restriction12Display.config(state="normal")
    restriction12Display.delete("1.0", "end")
    restriction12Display.config(state="disabled")

def sideQuest():
    deleteSideQuest()

    sideQuests = ["Kill Sirris", "Kill Anri", "Kill Siegward", "Kill Patches", "Help Siegward Defeat Yhorm", "Get Greirat to Lothric Castle", "Defeat Holy Knight Hodrick with Sirris", "Win the Duel with Hawkwood in the Abyss Watchers' Arena", "Obtain All Black Knight Weapons and Shield", "Defeat Alva, Seeker of the Spurned in the Ringed City", "Defeat Ancient Wyvern without the Drop", "Obtain 8+ Titanite Slabs"]
    sideQuestsRestriction = r.choice(sideQuests)

    text12Display = "{}".format(sideQuestsRestriction)
    text12DisplayLen = len(text12Display)
    restriction12Display.config(width=text12DisplayLen+1)
    restriction12Display.config(state="normal")
    restriction12Display.insert("1.0", text12Display)
    restriction12Display.config(state="disabled")

####################################################################
#Buttons
####################################################################
characterRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=charParamChallenge)
characterRestrictionButton.grid(column=0, row=1, padx=10, sticky="we")

shieldRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=shieldChallenge)
shieldRestrictionButton.grid(column=0, row=3, padx=10, sticky="we")

upgradeRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=upgradeChallenge)
upgradeRestrictionButton.grid(column=0, row=5, padx=10, sticky="we")

weaponArtsRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=weaponArtChallenge)
weaponArtsRestrictionButton.grid(column=0, row=7, padx=10, sticky="we")

armorRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=armorChallenge)
armorRestrictionButton.grid(column=0, row=9, padx=10, sticky="we")

ringRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=ringChallenge)
ringRestrictionButton.grid(column=0, row=11, padx=10, sticky="we")

estusRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=estusChallenge)
estusRestrictionButton.grid(column=0, row=13, padx=10, sticky="we")

consumableRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=consumableChallenge)
consumableRestrictionButton.grid(column=0, row=15, padx=10, sticky="we")

keysRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=keysChallenge)
keysRestrictionButton.grid(column=0, row=17, padx=10, sticky="we")

reallocationRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=reallocationChallenge)
reallocationRestrictionButton.grid(column=0, row=19, padx=10, sticky="we")

miscRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=miscChallenge)
miscRestrictionButton.grid(column=0, row=21, padx=10, sticky="we")

sideQuestRestrictionButton = tk.Button(root, text="Roll", bg=bgColorButton, fg=textColor, command=sideQuest)
sideQuestRestrictionButton.grid(column=0, row=23, padx=10, sticky="we")

####################################################################
#Root Tkinter Finish
####################################################################
root.mainloop()