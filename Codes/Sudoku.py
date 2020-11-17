import pygame
import time
import Codes.Start_Threading
import random
from threading import *


class Grid:
    def __init__(self, board, rows, cols, width, height, win):
        self.rows = rows
        self.board = board
        self.cols = cols
        self.width = width
        self.height = height
        self.win = win
        self.cubes = [[Cube(self.board[i][j], i, j, self.width, self.height) for j in range(self.cols)] for i in
                      range(self.rows)]
        self.model = None
        self.start_time = time.time()
        self.play_time = 0
        self.update_model()
        pygame.display.update()


    def update_model(self):
        self.model = [[self.cubes[i][j].value for j in range(self.cols)] for i in range(self.rows)]

    def format_time(self):
        sec = self.play_time % 60
        minute = self.play_time // 60
        self.play_time = str(minute) + ":" + str(sec)

    def draw(self):
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0 and i != 0:
                thick = 4
            else:
                thick = 1
            pygame.draw.line(self.win, (0, 0, 0), (0, i * gap), (self.width, i * gap), thick)
            pygame.draw.line(self.win, (0, 0, 0), (i * gap, 0), (i * gap, self.height), thick)
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw(self.win)
        pygame.display.update()

    def solve_gui(self, speed):
        self.update_model()
        find = find_empty(self.model)
        if not find:
            return True
        else:
            row, col = find
        for i in range(1, 10):
            click = pygame.mouse.get_pos()
            x = click[0]
            y = click[1]
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 10 <= x <= 230 and 550 <= y <= 595:
                        pygame.quit()
                        Process = Codes.Start_Threading.START()
                        Process.start()
                        quit()
            if 10 <= x <= 230 and 550 <= y <= 595:
                pygame.mouse.set_cursor(*pygame.cursors.tri_left)
                pygame.draw.rect(self.win, (194, 167, 45), [10, 550, 220, 45])
                self.win.blit(pygame.font.SysFont('calibri', 25).render('Back to main menu', True, (56, 66, 87)), (23, 560))
            else:
                pygame.mouse.set_cursor(*pygame.cursors.arrow)
                pygame.draw.rect(self.win, (232, 191, 9), [10, 550, 220, 45])
                self.win.blit(pygame.font.SysFont('calibri', 25).render('Back to main menu', True, (59, 60, 84)), (23, 560))
            self.play_time = round(time.time() - self.start_time)
            self.format_time()
            pygame.draw.rect(self.win, (240, 239, 209), [350, 560, 190, 50])
            self.win.blit(
                pygame.font.SysFont('calibri', 25).render("Time - " + str(self.play_time), True, (59, 60, 84)),
                (400, 560))
            pygame.display.update()
            if valid(self.model, i, (row, col)):
                self.model[row][col] = i
                self.cubes[row][col].set(i)
                self.cubes[row][col].draw_change(self.win, True)
                self.update_model()
                pygame.display.update()
                pygame.time.delay(1000 - (speed * 10))
                if self.solve_gui(speed):
                    return True
                self.model[row][col] = 0
                self.cubes[row][col].set(0)
                self.update_model()
                self.cubes[row][col].draw_change(self.win, False)
                pygame.display.update()
                pygame.time.delay(1000 - (speed * 10))
            pygame.display.update()
        return False


class Cube:
    rows = 9
    cols = 9

    def __init__(self, value, row, col, width, height):
        self.value = value
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height

    def draw(self, win):
        fnt = pygame.font.SysFont("comicsans", 40)
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        if self.temp != 0 and self.value == 0:
            text = fnt.render(str(self.temp), True, (128, 128, 128))
            win.blit(text, (x + 5, y + 5))
        elif not (self.value == 0):
            text = fnt.render(str(self.value), True, (0, 0, 0))
            win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))

    def draw_change(self, win, g=True):
        fnt = pygame.font.SysFont("comicsans", 40)
        gap = self.width / 9
        x = self.col * gap
        y = self.row * gap
        pygame.draw.rect(win, (240, 239, 209), (x, y, gap, gap), 0)
        text = fnt.render(str(self.value), True, (0, 0, 0))
        win.blit(text, (x + (gap / 2 - text.get_width() / 2), y + (gap / 2 - text.get_height() / 2)))
        if g:
            pygame.draw.rect(win, (0, 255, 0), (x, y, gap, gap), 3)
        else:
            pygame.draw.rect(win, (255, 0, 0), (x, y, gap, gap), 3)

    def set(self, val):
        self.value = val


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return i, j
    return None


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def redraw_window(win, board):
    win.fill((240, 239, 209))
    board.draw()


def sudoku(speed):
    pygame.init()
    pygame.font.init()
    win = pygame.display.set_mode((540, 670))
    pygame.display.set_caption("Sudoku Solver Visualizer")
    pygame.display.set_icon(pygame.image.load("Images/sudoku.png"))
    random_board = random.choice([
        [[7, 8, 0, 4, 0, 0, 1, 2, 0],
         [6, 0, 0, 0, 7, 5, 0, 0, 9],
         [0, 0, 0, 6, 0, 1, 0, 7, 8],
         [0, 0, 7, 0, 4, 0, 2, 6, 0],
         [0, 0, 1, 0, 5, 0, 9, 3, 0],
         [9, 0, 4, 0, 6, 0, 0, 0, 5],
         [0, 7, 0, 3, 0, 0, 0, 1, 2],
         [1, 2, 0, 0, 0, 7, 4, 0, 0],
         [0, 4, 9, 2, 0, 6, 0, 0, 7]],

        [[3, 0, 6, 5, 0, 8, 4, 0, 0],
         [5, 2, 0, 0, 0, 0, 0, 0, 0],
         [0, 8, 7, 0, 0, 0, 0, 3, 1],
         [0, 0, 3, 0, 1, 0, 0, 8, 0],
         [9, 0, 0, 8, 6, 3, 0, 0, 5],
         [0, 5, 0, 0, 9, 0, 6, 0, 0],
         [1, 3, 0, 0, 0, 0, 2, 5, 0],
         [0, 0, 0, 0, 0, 0, 0, 7, 4],
         [0, 0, 5, 2, 0, 6, 3, 0, 0]],

        [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]
    ])
    print("choose randomly")
    board = Grid(random_board, 9, 9, 540, 540, win)
    run = True
    solving = 0
    while run:
        click = pygame.mouse.get_pos()
        x = click[0]
        y = click[1]
        if solving <= 1:
            redraw_window(win, board)
        if solving == 1:
            win.blit(pygame.font.SysFont('comicsans', 50).render('Sudoku Solved!', True, (59, 60, 84)), (130, 615))
        board.solve_gui(speed)
        solving += 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 10 <= x <= 230 and 550 <= y <= 595:
                    pygame.quit()
                    Process = Codes.Start_Threading.START()
                    Process.start()
                    quit()
        if 10 <= x <= 230 and 550 <= y <= 595:
            pygame.mouse.set_cursor(*pygame.cursors.tri_left)
            pygame.draw.rect(win, (194, 167, 45), [10, 550, 220, 45])
            win.blit(pygame.font.SysFont('calibri', 25).render('Back to main menu', True, (56, 66, 87)), (23, 560))
        else:
            pygame.mouse.set_cursor(*pygame.cursors.arrow)
            pygame.draw.rect(win, (232, 191, 9), [10, 550, 220, 45])
            win.blit(pygame.font.SysFont('calibri', 25).render('Back to main menu', True, (59, 60, 84)), (23, 560))
        pygame.draw.rect(win, (240, 239, 209), [350, 560, 190, 50])
        win.blit(
            pygame.font.SysFont('calibri', 25).render("Time - " + str(board.play_time), True, (59, 60, 84)),
            (400, 560))
        pygame.display.update()
    pygame.quit()
