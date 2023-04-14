"""Try to observe the screen and play Tetris to perform a newe highscore"""

#TODO
# pip install selenium
# setup webdriver to oberserve the game
# setup basic game control to control the game by yourself
# then implement a reinforcement model to give the control up

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import keyboard



# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)



class TetrisControl:

    def setup(self):
        # start the tetris site on chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://tetris.com/play-tetris")
        self.running = True
        self.controlStart = False

    def controlGame(self):
        while self.running:

            # start the progress
            keyboard.wait("ctrl")
            
            # find the game area to focus on it
            elem = self.driver.find_element(By.ID, "gameIFrame")
            
            
            if elem != None:
                elem.screenshot_as_png()
                self.driver.save_screenshot("test.png")
                self.controlStart = True
                print("start control")
            else: 
                print("Element was not found")


            while self.controlStart:
                self.rotateTile(elem)
                self.moveTileLeft(elem)
                self.dropTile(elem)

                
            # element = driver.find_element(By.ID, "passwd-id")
            # element = driver.find_element(By.NAME, "passwd")
            # element = driver.find_element(By.XPATH, "//input[@id='passwd-id']")
            # element = driver.find_element(By.CSS_SELECTOR, "input#passwd-id")

            

        self.tearDown()

    def rotateTile(self, elem):
        elem.send_keys(Keys.UP)
        print("rotate Element")

    def moveTileLeft(self, elem):
        elem.send_keys(Keys.LEFT)
        print("moved Left")

    def moveTileRight(self, elem):
        elem.send_keys(Keys.RIGHT)
        print("moved right")

    def dropTile(self, elem):
        elem.send_keys(Keys.DOWN)

    def tearDown(self):
        self.driver.close()

    def giveReward(self):
        pass

control = TetrisControl()
control.setup()
control.controlGame()

    