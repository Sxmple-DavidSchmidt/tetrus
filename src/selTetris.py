"""Try to observe the screen and play Tetris to perform a new highscore"""
import base64
import keyboard
import matplotlib.pyplot as plt
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from io import BytesIO

from src import game_state_parser


class TetrisControl:
    def __init__(self):
        self.controlStart = None
        self.running = None
        self.driver = None
        self.canvas = None
        self.data = None

    def setup(self):
        # start the tetris site on chrome
        self.driver = webdriver.Chrome()
        self.driver.get("https://tetris.com/play-tetris")
        self.running = True

    def controlGame(self):
        print("Press CTRL to start..")
        keyboard.wait("ctrl")

        self.canvas = self.driver.find_element(By.ID, "gameIFrame")
        self.update_screen()

        # self.rotateTile()
        # self.moveTileLeft()
        # self.dropTile()
        # self.tearDown()

    def update_screen(self):
        if self.canvas is None:
            print("Canvas element is None")
            return

        # TODO find better way to to this..
        image = Image.open(
            BytesIO(
                base64.b64decode(
                    self.canvas.screenshot_as_base64
                )
            )
        )
        wins = game_state_parser.get_sub_windows(image)

        self.data = (
            game_state_parser.parse_primary_window(wins[0], flatten=False),
            game_state_parser.parse_secondary_window(wins[1])
        )
        pass

    def rotateTile(self):
        self.canvas.send_keys(Keys.UP)
        print("rotated Element")

    def moveTileLeft(self):
        self.canvas.send_keys(Keys.LEFT)
        print("moved Left")

    def moveTileRight(self):
        self.canvas.send_keys(Keys.RIGHT)
        print("moved right")

    def dropTile(self):
        self.canvas.send_keys(Keys.DOWN)

    def tearDown(self):
        self.driver.close()

    def giveReward(self):
        pass


if __name__ == "__main__":
    c = TetrisControl()
    c.setup()
    c.controlGame()

    plt.imshow(c.data[0])
    plt.show()
