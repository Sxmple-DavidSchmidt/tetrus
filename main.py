import matplotlib.pyplot as plt
from src.selTetris import TetrisControl

if __name__ == "__main__":
    c = TetrisControl()
    c.setup()
    c.controlGame()

    plt.imshow(c.data[0])
    plt.show()
