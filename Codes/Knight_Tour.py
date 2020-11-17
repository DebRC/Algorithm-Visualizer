import pygame
from heapq import *
import random
import time
from threading import *
import Codes.Start_Threading

class Knight():
    def __init__(self, size, speed):
        self.n = size
        self.cb = [[0 for x in range(size)] for y in range(size)]
        self.ans = []
        self.speed = speed
        self.WaitForEndProcess=0
        self.operations=0
        self.running=True
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption("Knight's Tour")
        pygame.display.set_icon(pygame.image.load("Images/knight.png"))
        self.SIDE = 600
        self.block = self.SIDE // self.n
        self.win = pygame.display.set_mode((self.SIDE, self.SIDE+130))
        self.K_SIDE = (self.block * 3) // 4
        self.knight_img = pygame.image.load('Images/knight1.png')
        self.knight_img = pygame.transform.scale(self.knight_img, (self.K_SIDE, self.K_SIDE))
        self.WHITE = (255, 255, 255)
        self.BLACK = (145, 96, 22)
        self.ROUTE = (214, 61, 34)
        self.x = self.block // 2
        self.y = self.block // 2
        self.x1 = (self.block - self.K_SIDE) // 2
        self.line_w = -int(-70 // self.n)
        self.grid()
        self.start = time.time()
        self.play_time = 0
        StartSolving = Thread(target=self.solve)
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
            if self.WaitForEndProcess == 1:
                self.win.blit(pygame.font.SysFont('comicsans', 50).render("Knight's Tour Shown", True, (59, 60, 84)), (145, 680))
                self.WaitForEndProcess += 1


    def grid(self):
        for i in range(self.n):
            for j in range(self.n):
                if not self.running:
                    break
                if ((i + j) % 2 == 0):
                    color = self.WHITE
                else:
                    color = self.BLACK
                pygame.draw.rect(self.win, color, (i * self.block, j * self.block, self.block, self.block))
                if ([i, j] in self.ans):
                    pygame.draw.rect(self.win, (66, 245, 161),
                                     (self.x1 + i * self.block, self.x1 + j * self.block, self.K_SIDE, self.K_SIDE))
        pygame.draw.rect(self.win, (240, 239, 209), (0, 600, 600, 730))


    def show(self):
        self.grid()
        xx, yy = self.ans[0]
        for i in range(1, len(self.ans)):
            if not self.running:
                break
            tx, ty = self.ans[i]
            pygame.draw.line(self.win, self.ROUTE, (self.x + xx * self.block, self.x + yy * self.block),
                             (self.x + tx * self.block, self.x + ty * self.block), self.line_w)
            xx, yy = self.ans[i]
        self.win.blit(self.knight_img, (self.x1 + xx * self.block, self.x1 + yy * self.block))
        self.win.blit(
            pygame.font.SysFont('calibri', 25).render(
                "Time - " + str(self.play_time // 60) + ":" + str(self.play_time % 60), True, (59, 60, 84)),
            (465, 627))


    def solve(self):
        kx = random.randint(0, self.n - 1)
        ky = random.randint(0, self.n - 1)
        dx = [-2, -1, 1, 2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        for k in range(self.n ** 2):
            if not self.running:
                break
            self.operations+=1
            self.cb[ky][kx] = k + 1
            self.ans.append([kx, ky])
            self.play_time = round(time.time() - self.start)
            self.show()
            if not self.running:
                break
            time.sleep(1/self.speed)
            pq = []
            for i in range(8):
                self.operations+=1
                if not self.running:
                    break
                nx = kx + dx[i]
                ny = ky + dy[i]
                if 0 <= nx < self.n and 0 <= ny < self.n:
                    if self.cb[ny][nx] == 0:
                        ctr = 0
                        for j in range(8):
                            self.operations+=1
                            if not self.running:
                                break
                            ex = nx + dx[j]
                            ey = ny + dy[j]
                            if 0 <= ex < self.n and 0 <= ey < self.n:
                                if self.cb[ey][ex] == 0: ctr += 1
                        heappush(pq, (ctr, i))
            if len(pq) > 0:
                (p, m) = heappop(pq)
                kx += dx[m]
                ky += dy[m]
            else:
                break
            pygame.display.update()
        self.WaitForEndProcess=1
        return True
