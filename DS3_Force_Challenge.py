# Name : DS3 Force Challenge
# Original Author : mranaglyph (interdim_designs)
# Date : 7/2/2021.

# Extra Special Thanks To : learncodebygaming for creating the "pydirectinput" library, such a massive help!
# learncodebygaming video : https://www.youtube.com/watch?v=LFDGgFRqVIs
# learncodebygaming github : https://github.com/learncodebygaming

import time, random, keyboard
import pydirectinput as pdi

def forceGesture():
    print()
    while True:
        if keyboard.is_pressed('F9'):
            print('Program Ended\n')
            break
        else:
            varianceTimeG = random.randint(1, vTimeG)
            variantChoice = random.randint(1, 7)
            time.sleep(varianceTimeG)
            pdi.keyDown('g')
            print('Gesture Menu Opened\n')
            time.sleep(.10)
            pdi.keyUp('g')
            for n in range(variantChoice):
                pdi.keyDown('left')
                time.sleep(.10)
                pdi.keyUp('left')
                time.sleep(.25)
            pdi.keyDown('e')
            time.sleep(.10)
            pdi.keyUp('e')
            print('Gestured @ {} Seconds\n'.format(varianceTimeG))
            continue

def forceItem():
    print()
    while True:
        if keyboard.is_pressed('F9'):
            print('Program Ended\n')
            break
        else:
            varianceTimeI = random.randint(1, vTimeI)
            time.sleep(varianceTimeI)
            pdi.keyDown('r')
            time.sleep(.10)
            pdi.keyUp('r')
            time.sleep(.25)
            pdi.keyDown('e')
            time.sleep(.10)
            pdi.keyUp('e')
            print('Item Used @ {} Seconds\n'.format(varianceTimeI))
            continue

def forceCamera():
    print()
    while True:
        if keyboard.is_pressed('F9'):
            print('Program Ended\n')
            break
        else:
            varianceTimeC = random.randint(1, vTimeC)
            time.sleep(varianceTimeC)
            pdi.keyDown('q')
            time.sleep(.10)
            pdi.keyUp('q')
            print('Camera Reset @ {} Seconds\n'.format(varianceTimeC))
            continue

def forceAll():
    print()
    while True:
        if keyboard.is_pressed('F9'):
            print('Program Ended\n')
            break
        else:
            shuffle = random.randint(1, 3)
            if shuffle == 1:
                varianceTimeG = random.randint(1, vTimeG)
                variantChoice = random.randint(1, 7)
                time.sleep(varianceTimeG)
                pdi.keyDown('g')
                print('Gesture Menu Opened\n')
                time.sleep(.10)
                pdi.keyUp('g')
                for n in range(variantChoice):
                    pdi.keyDown('left')
                    time.sleep(.25)
                    pdi.keyUp('left')
                pdi.keyDown('e')
                time.sleep(.10)
                pdi.keyUp('e')
                print('Gestured @ {} Seconds\n'.format(varianceTimeG))
                continue
            
            elif shuffle == 2:
                varianceTimeI = random.randint(1, vTimeI)
                time.sleep(varianceTimeI)
                pdi.keyDown('r')
                time.sleep(.10)
                pdi.keyUp('r')
                time.sleep(.25)
                pdi.keyDown('e')
                time.sleep(.10)
                pdi.keyUp('e')
                print('Item Used @ {} Seconds\n'.format(varianceTimeI))
                continue
            
            elif shuffle == 3:
                varianceTimeC = random.randint(1, vTimeC)
                time.sleep(varianceTimeC)
                pdi.keyDown('q')
                time.sleep(.10)
                pdi.keyUp('q')
                print('Camera Reset @ {} Seconds\n'.format(varianceTimeC))
                continue

while True:
    try:
        userChoice = int(input('\nWhich Challenge Would You Like? [Enter Number] \n\nForce Gesture [1]\n\nForce Item [2]\n\nForce Camera [3]\n\nForce All [4]\n\n : '))
    except ValueError:
        print('\nPlease Select a Number')
        continue
    else:
        if userChoice > 4:
            print('\nPlease Select a Valid Number')
        elif userChoice < 1:
            print('\nPlease Select a Valid Number')
        else:
            break

if userChoice == 1:
    print('\nIf You Need to Quit, Hold [F9] Until "Program Ended" Appears in This Window.')
    print('\nMinimum Time Between Actions is 1 Second; Maximum Time Between Actions Will Be? [Enter Seconds]')
    while True:
        try:
            vTimeG = int(input('\n : '))
        except ValueError:
            print('\nPlease Select a Number')
            continue
            
        else: 
            if vTimeG < 2:
                print('\nMaximum Time Cannot be Less Than or Equal to Minimum Time, Sorry')
                continue        
            else:
                print('\nProgram Starting in Ten Seconds')
                time.sleep(10)
                forceGesture()
                break

if userChoice == 2:
    print('\nIf You Need to Quit, Hold [F9] Until "Program Ended" Appears in This Window.')
    print('\nMinimum Time Between Actions is 1 Second; Maximum Time Between Actions Will Be? [Enter Seconds]')
    while True:
        try:
            vTimeI = int(input('\n : '))
        except ValueError:
            print('\nPlease Select a Number')
            continue
            
        else: 
            if vTimeI < 2:
                print('\nMaximum Time Cannot be Less Than or Equal to Minimum Time, Sorry')
                continue        
            else:
                print('\nProgram Starting in Ten Seconds')
                time.sleep(10)
                forceItem()
                break

if userChoice == 3:
    print('\nIf You Need to Quit, Hold [F9] Until "Program Ended" Appears in This Window.')
    print('\nMinimum Time Between Actions is 1 Second; Maximum Time Between Actions Will Be? [Enter Seconds]')
    while True:
        try:
            vTimeC = int(input('\n : '))
        except ValueError:
            print('\nPlease Select a Number')
            continue
            
        else: 
            if vTimeC < 2:
                print('\nMaximum Time Cannot be Less Than or Equal to Minimum Time, Sorry')
                continue        
            else:
                print('\nProgram Starting in Ten Seconds')
                time.sleep(10)
                forceCamera()
                break

if userChoice == 4:
    print('\nIf You Need to Quit, Hold [F9] Until "Program Ended" Appears in This Window.')
    print('\nMinimum Time Between Actions is 1 Second; Maximum Time Between Actions Will Be? [Enter Seconds]')
    while True:
        try:
            vTimeG = int(input('\nGesture Max : '))
            vTimeI = int(input('\nItem Max : '))
            vTimeC = int(input('\nCamera Max : '))
        except ValueError:
            print('\nPlease Select a Number')
            continue            
        else: 
            if vTimeG < 2:
                print('\nMaximum Time Cannot be Less Than or Equal to Minimum Time, Sorry')
                continue
            elif vTimeI < 2:
                print('\nMaximum Time Cannot be Less Than or Equal to Minimum Time, Sorry')
                continue
            elif vTimeC < 2:
                print('\nMaximum Time Cannot be Less Than or Equal to Minimum Time, Sorry')
                continue       
            else:
                print('\nProgram Starting in Ten Seconds')
                time.sleep(10)
                forceAll()
                break

time.sleep(5)