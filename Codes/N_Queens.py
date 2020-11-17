import pygame
import time
from threading import *
import Codes.Start_Threading


class N_queen:
    def __init__(self, size, speed):
        pygame.init()
        pygame.font.init()
        # Caption of window
        pygame.display.set_caption("N-Queens")
        # Icon of the window
        pygame.display.set_icon(pygame.image.load("Images/nqueens.png"))
        # Diagonals List
        self.diagonal1 = {}
        self.diagonal2 = {}
        # Column list
        self.col = {}
        self.a = []
        self.solved = 0
        self.WaitForEndProcess = True
        # size of the chessboard
        self.n = size
        # size of the window
        self.SIDE = 600
        # size of entire window
        self.win = pygame.display.set_mode((self.SIDE, self.SIDE + 130))
        # size of each cube
        self.block = self.SIDE // self.n
        # speed of execution
        self.speed = speed
        # size of queen
        self.queen_size = (3 * self.block) // 4
        # image the on queen
        self.queen = pygame.image.load('Images/nqueens1.png')
        # changing image size to desired queen size
        self.queen = pygame.transform.scale(self.queen, (self.queen_size, self.queen_size))
        # colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (145, 96, 22)
        self.ATTACK_COL = (255, 51, 0)
        # queen image starting pos for each block
        self.x = (self.block - self.queen_size) // 2
        self.y = (self.block - self.queen_size) // 2
        # starting the visualization
        self.running = True
        self.play_time = 0
        # drawing the chess board
        self.grid()
        self.start = time.time()
        # start threading
        StartSolving = Thread(target=self.solve, args=(0,))
        StartSolving.start()
        while self.running:
            pygame.display.update()
            click = pygame.mouse.get_pos()
            x = click[0]
            y = click[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 15 <= x <= 230 and 615 <= y <= 665:
                        self.running = False
                        pygame.quit()
                        Process = Codes.Start_Threading.START()
                        Process.start()
                        quit()
            # Buttons for back to main menu
            if 15 <= x <= 230 and 615 <= y <= 665:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                pygame.draw.rect(self.win, (194, 167, 45), [15, 615, 215, 50])
                self.win.blit(pygame.font.SysFont('calibri', 25).render('Back to main menu', True, (56, 66, 87)),
                              (25, 627))
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                pygame.draw.rect(self.win, (232, 191, 9), [15, 615, 215, 50])
                self.win.blit(pygame.font.SysFont('calibri', 25).render('Back to main menu', True, (59, 60, 84)),
                              (25, 627))
            # if solved show at the below of the screen
            if self.solved == 1:
                self.win.blit(
                    pygame.font.SysFont('comicsans', 50).render(str(size) + ' Queens Solved!', True, (59, 60, 84)),
                    (145, 680))
                self.solved += 1

    # function for drawing the grid
    def grid(self):
        for i in range(self.n):
            for j in range(self.n):
                if not self.running:
                    break
                if (i + j) % 2 == 0:
                    color = self.WHITE
                else:
                    color = self.BLACK
                pygame.draw.rect(self.win, color, (i * self.block, j * self.block, self.block, self.block))
        pygame.draw.rect(self.win, (240, 239, 209), (0, 600, 600, 730))

    # function for refreshing the screen with new positions
    def show(self):
        self.grid()
        for i in range(len(self.a)):
            if not self.running:
                break
            self.win.blit(self.queen, (self.x + (self.a[i] - 1) * self.block, self.y + i * self.block))
            self.win.blit(
                pygame.font.SysFont('calibri', 25).render("Time - " + str(self.play_time//60) + ":" + str(self.play_time % 60), True, (59, 60, 84)),
                (465, 627))

    # main solve
    def solve(self, i):
        if i == self.n:
            self.solved = 1
            return 1
        r = i + 1
        for c in range(1, self.n + 1):
            if not self.running:
                break
            click = pygame.mouse.get_pos()
            x = click[0]
            y = click[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 15 <= x <= 230 and 615 <= y <= 665:
                        self.running = False
                        pygame.quit()
                        Process = Codes.Start_Threading.START()
                        Process.start()
                        quit()
            self.a.append(c)
            self.play_time = round(time.time() - self.start)
            self.show()
            if not self.running:
                break
            time.sleep(1 / self.speed)
            if (c in self.col) or (r + c in self.diagonal1) or (r - c in self.diagonal2):
                if c in self.col:
                    pygame.draw.rect(self.win, self.ATTACK_COL, (
                        self.block // 2 + (c - 1) * self.block, self.block // 2, 5, self.SIDE - self.block))
                if r + c in self.diagonal1:
                    temp = r + c
                    yy1 = temp - 1
                    xx1 = 1
                    if temp > self.n:
                        yy1 = self.n
                        xx1 = temp - self.n
                    xx1 = self.block // 2 + self.block * (xx1 - 1)
                    yy1 = self.block // 2 + self.block * (yy1 - 1)
                    pygame.draw.line(self.win, self.ATTACK_COL, (xx1, yy1), (yy1, xx1), 7)

                if r - c in self.diagonal2:
                    temp = r - c
                    yy1 = temp
                    xx1 = 0
                    if (temp < 0):
                        yy1, xx1 = xx1, -yy1
                    pygame.draw.line(self.win, self.ATTACK_COL,
                                     (self.block // 2 + xx1 * self.block, self.block // 2 + yy1 * self.block), (
                                         self.block // 2 + (self.n - yy1 - 1) * self.block,
                                         self.block // 2 + (self.n - xx1 - 1) * self.block), 7)
                if not self.running:
                    break
                time.sleep(1 / self.speed)
                self.a.pop()
                continue
            if not self.running:
                break
            self.col[c] = r
            self.diagonal1[r + c] = r
            self.diagonal2[r - c] = r
            if self.solve(i + 1):
                self.WaitForEndProcess = False
                return 1
            self.a.pop()
            del self.diagonal1[r + c]
            del self.col[c]
            del self.diagonal2[r - c]
            pygame.display.update()
        self.WaitForEndProcess = False
        return 0
