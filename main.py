# Import the libraries
import pyautogui
import time
import pytesseract
from PIL import ImageGrab
from PIL import Image


def clickTextOnScreen(text,screenWidth, screenHeight):
    # Define a region of interest on the screen (top, left, width, height)
    region = (0, 0, screenWidth, screenHeight)

    # Take a screenshot of that region
    screenshot = ImageGrab.grab(bbox=region)

    # Convert the screenshot to text using pytesseract
    textData = pytesseract.image_to_data(screenshot)
    print(textData)

    # Find the coordinates of the text on the image using pytesseract
    for i in range(len(textData.splitlines())):
        line = textData.splitlines()[i]
        if i == 0:
            continue # Skip the first line which is a header
        data = line.split()
        if len(data) == 12: # Check if there are 12 fields in the data
            word = data[11] # The last field is the word
            if word == text: # Check if the word matches the text we want to click
                x = int(data[6]) # The seventh field is the left coordinate of the word
                y = int(data[7]) # The eighth field is the top coordinate of the word

                # Move the mouse cursor to those coordinates and click using pyautogui
                pyautogui.moveTo(x + region[0], y + region[1]) # Add the region offset to get absolute coordinates on screen
                pyautogui.click()

def clickImageOnScreen(imageFile, screenWidth, screenHeight):
    # Define a region of interest on the screen (top, left, width, height)
    region = (0, 0, screenWidth, screenHeight)

    # Take a screenshot of that region
    screenshot = ImageGrab.grab(bbox=region)

    # Find the location of the image on the screenshot using pyautogui
    location = pyautogui.locate(imageFile, screenshot,confidence=0.9)

    # If the image is found on the screen
    if location is not None:
        # Get the center coordinates of the image
        x, y = pyautogui.center(location)

        # Move the mouse cursor to those coordinates and click using pyautogui
        pyautogui.moveTo(x + region[0], y + region[1]) # Add the region offset to get absolute coordinates on screen
        pyautogui.click()
    
    # If the image is not found on the screen
    else:
        print("Image not found on screen.")

def is_image_on_screen(imageFile, screenWidth, screenHeight):
    # Define a region of interest on the screen (top, left, width, height)
    region = (0, 0, screenWidth, screenHeight)

    # Take a screenshot of that region
    screenshot = ImageGrab.grab(bbox=region)

    # Find the location of the image on the screenshot using pyautogui
    location = pyautogui.locate(imageFile, screenshot,confidence=0.9)
    if location != None:
        return True
    else:
        return False

def save_screenshot(top, left, width, height,file_name):
    # Define a region of interest on the screen (top, left, width, height)
    region = (top, left, width, height)

    # Take a screenshot of that region
    screenshot = ImageGrab.grab(bbox=region)

    # Save the screenshot to a file
    screenshot.save(file_name)

def endTurn():
    # Get the size of the screen
    screenWidth, screenHeight = pyautogui.size()

    # Calculate the coordinates based on percentage of display
    x = screenWidth * 0.80 # 90% from left
    y = screenHeight * 0.45 # 20% from top

    # Move the mouse cursor to (x, y) and click
    pyautogui.moveTo(x, y)
    pyautogui.click()

def merc_tp_barrens_hq(screenWidth, screenHeight):
    # Wait for 5 seconds before starting
    time.sleep(1)

    #Open Merc game mode
    pyautogui.moveTo(screenWidth * 0.504, screenHeight *  0.452)
    pyautogui.click()
    time.sleep(6)
    
    #Open Travel Point    
    pyautogui.moveTo(screenWidth * 0.508, screenHeight *  0.235)
    pyautogui.click()
    time.sleep(3)

    #Select The Barrens mission    
    clickImageOnScreen("images/TheBarrens.png",screenWidth, screenHeight)
    time.sleep(2)

    #Select The heroic button
    if is_image_on_screen("images/HeroicMission.png",screenWidth, screenHeight):
        clickImageOnScreen("images/HeroicMission.png",screenWidth, screenHeight)
        time.sleep(1)
    else:
        pyautogui.click()
        time.sleep(1)        
        clickImageOnScreen("images/HeroicMission.png",screenWidth, screenHeight)
        time.sleep(1)
    
    #Select the choose button
    print("clicking Travel Point choose")
    clickImageOnScreen("images/TP_Choose.png",screenWidth, screenHeight)
    time.sleep(4)

    #Select the mission
    clickImageOnScreen("images/fq.png",screenWidth, screenHeight)
    time.sleep(1)

    #Select the choose button    
    clickImageOnScreen("images/Choose.png",screenWidth, screenHeight)
    time.sleep(4)

    #Select the bot hero group    
    clickImageOnScreen("images/bot_hero_group.png",screenWidth, screenHeight)
    time.sleep(1)

    #Select the choose button    
    clickImageOnScreen("images/Choose.png",screenWidth, screenHeight)
    time.sleep(1)

    #Select the Lock in button    
    clickImageOnScreen("images/LockIn.png",screenWidth, screenHeight)
    time.sleep(5)

    #Select the Play in button
    time.sleep(1)
    clickImageOnScreen("images/Play.png",screenWidth, screenHeight)
    time.sleep(20)

    while True:
        #Select Heros    
        endTurn()
        time.sleep(2)

        #Play rounds
        time.sleep(2)
        print("Playing rounds")
        while is_image_on_screen("images/PickTreas.png",screenWidth, screenHeight) == False:
            time.sleep(1)
            while is_image_on_screen("images/FightYellow.png",screenWidth, screenHeight) :
                time.sleep(1)
                #Select first Ability
                pyautogui.moveTo(screenWidth * 0.3984, screenHeight *  0.4444)
                pyautogui.click()
                time.sleep(2)
                gab = 0
                while (not is_image_on_screen("images/AbillitiesBoarderWarrior.png",screenWidth, screenHeight)) and ( not is_image_on_screen("images/AbillitiesBoarderFighter.png",screenWidth, screenHeight) and ( not is_image_on_screen("images/AbillitiesBoarderCaster.png",screenWidth, screenHeight)) and ( not is_image_on_screen("images/AbillitiesBoarderNetrual.png",screenWidth, screenHeight)) and is_image_on_screen("images/FightYellow.png",screenWidth, screenHeight)) :
                    #trying to hit enemy
                    pyautogui.moveTo((screenWidth * 0.2507) + gab, screenHeight * 0.2715)
                    pyautogui.click()
                    time.sleep(0.5)
                    gab += 100
            
            endTurn()
            time.sleep(2)
        
        #Click take to take treasure
        time.sleep(1)
        print("choosing treasure")
        pyautogui.moveTo((screenWidth * 0.5) + gab, screenHeight * 0.5)
        pyautogui.click()
        time.sleep(3)
        print("clicking take")
        clickImageOnScreen("images/TakeTreasure.png",screenWidth, screenHeight)
        time.sleep(2)

        #Chose next battle
        gab=0
        while (not is_image_on_screen("images/Play.png",screenWidth, screenHeight)):
            pyautogui.moveTo((screenWidth * 0.2) + gab, screenHeight * 0.5)
            pyautogui.click()
            time.sleep(0.5)
            gab +=100
        
        #Select the Play in button
        time.sleep(1)
        clickImageOnScreen("images/Play.png",screenWidth, screenHeight)
        time.sleep(20)

    #endTurn()
    
def getMousePercentage(screenWidth, screenHeight):
    # Get the current mouse coordinates
    mouseX, mouseY = pyautogui.position()

    # Calculate the percentage of display for x and y
    xPercent = mouseX / screenWidth
    yPercent = mouseY / screenHeight

    # Return a tuple of (xPercent, yPercent)
    return (xPercent, yPercent)


# Define the main function
def main():
    # Wait for 5 seconds before starting
    time.sleep(5)

    # Get the size of the screen
    screenWidth, screenHeight = pyautogui.size()

    merc_tp_barrens_hq(screenWidth, screenHeight)
    input()

    # Get mouse location in percentage
    xPercent, yPercent = getMousePercentage(screenWidth, screenHeight)
    print(xPercent, yPercent)
    top, left, width, height = (xPercent * screenWidth ) , (yPercent * screenHeight)  ,(xPercent * screenWidth)  + 100, (yPercent * screenHeight) + 50
    #save_screenshot(top, left, width, height ,"images/TakeTreasure.png")

    clickImageOnScreen("images/TakeTreasure.png",screenWidth, screenHeight)



# Run the main function
if __name__ == "__main__":
    main()
