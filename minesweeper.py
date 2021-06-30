import pygame
import random

pygame.init()

# cols er vanrett
cols = 16
# rows er loddrett
rows = 16
number_of_bombs = 40
w = 16
h = 16
border_x = 4
border_y = 50
bomb_square = [10, 10, 60, border_y - 20]
text_size = 20

game_width = w * cols
game_height = h * rows
display_width = game_width + border_x * 2
display_height = game_width + border_y
font = pygame.font.SysFont("comicsansms", 26)
smiley_size = 26
smiley_place = (display_width/2 - 13, border_y/2 - 13)
time_square = [display_width - 90, 10, 80 , border_y - 20]

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Minesweeper")

clock = pygame.time.Clock()

square = pygame.image.load("square.png")
flag = pygame.image.load("flag.png")
square_opened = pygame.image.load("square_opened.png")
bomb = pygame.image.load("bomb.png")
question = pygame.image.load("question.png")
smiley = pygame.image.load("smiley.png")
smiley_mad = pygame.image.load("sur_smiley.png")
smiley_rar = pygame.image.load("simley_rar.png")
bombe_blown = pygame.image.load("bomb_sprengt.png")
cool_smiley = pygame.image.load("cool_smiley.png")


one = pygame.image.load("one.png")
two = pygame.image.load("two.png")
three = pygame.image.load("tree.png")
four = pygame.image.load("four.png")
five = pygame.image.load("five.png")
six = pygame.image.load("six.png")
seven = pygame.image.load("seven.png")
eight = pygame.image.load("eight.png")

grey = (99, 99, 99)
black = (0, 0, 0)

grid = None
game_plan = True


class Cell:

	def __init__(self, x, y, x_size, y_size, bomb=False):
		self.bomb = bomb
		self.revealed = False
		self.x = x + border_x
		self.y = y + border_y - border_x
		self.x_size = x_size
		self.y_size = y_size
		self.number = False
		self.flag = False
		self.question = False
		self.temp = False
		self.blown = False
	def draw(self):
		if self.bomb and self.revealed:
			gameDisplay.blit(bomb, (self.x, self.y))
		elif not self.revealed and not self.question and not self.flag:
			gameDisplay.blit(square, (self.x, self.y))
		elif self.revealed:
			gameDisplay.blit(square_opened, (self.x, self.y))
		elif self.question:
			gameDisplay.blit(question, (self.x, self.y))
		elif self.flag:
			gameDisplay.blit(flag, (self.x, self.y))
		if self.temp and not self.flag and not self.question:
			gameDisplay.blit(square_opened, (self.x, self.y))
		if self.number and not self.flag and not self.question:
			if self.bomb_number == 1:
				gameDisplay.blit(one, (self.x, self.y))
			elif self.bomb_number == 2:
				gameDisplay.blit(two, (self.x, self.y))
			elif self.bomb_number == 3:
				gameDisplay.blit(three, (self.x, self.y))
			elif self.bomb_number == 4:
				gameDisplay.blit(four, (self.x, self.y))
			elif self.bomb_number == 5:
				gameDisplay.blit(five, (self.x, self.y))
			elif self.bomb_number == 6:
				gameDisplay.blit(six, (self.x, self.y))
			elif self.bomb_number == 7:
				gameDisplay.blit(seven, (self.x, self.y))
			elif self.bomb_number == 8:
				gameDisplay.blit(eight, (self.x, self.y))
		if self.blown:
			gameDisplay.blit(bombe_blown, (self.x, self.y))



	def click(self,i, j, check=False):
		global grid
		if not grid[i][j].flag and not grid[i][j].question and not check:
			self.revealed = True
		if self.revealed and self.bomb:
			game_over()
			self.blown = True
		self.bomb_number = 0
		self.flag_number = 0
		self.check = check
		if not self.bomb:
			if j-1 >= 0 and j-1 < rows:
				if grid[i][j-1].bomb:
					self.bomb_number += 1
				if grid[i][j-1].flag:
					self.flag_number += 1
			if j + 1 >= 0 and j + 1 < rows:
				if grid[i][j+1].bomb:
					self.bomb_number += 1
				if grid[i][j+1].flag:
					self.flag_number += 1
			if i - 1 >= 0 and i - 1 < cols:
				if grid[i-1][j].bomb:
					self.bomb_number += 1
				if grid[i-1][j].flag:
					self.flag_number += 1
			if i + 1 >= 0 and i + 1 < cols:
				if grid[i+1][j].bomb:
					self.bomb_number += 1
				if grid[i+1][j].flag:
					self.flag_number += 1
			if i - 1 >= 0 and i - 1 < cols and j + 1 >= 0 and j + 1 < rows:
				if grid[i-1][j+1].bomb:
					self.bomb_number += 1
				if grid[i-1][j+1].flag:
					self.flag_number += 1
			if i - 1 >= 0 and i - 1 < cols and j - 1 >= 0 and j - 1 < rows:
				if grid[i-1][j-1].bomb:
					self.bomb_number += 1
				if grid[i-1][j-1].flag:
					self.flag_number += 1
			if i + 1 >= 0 and i + 1 < cols and j + 1 >= 0 and j + 1 < rows:
				if grid[i+1][j+1].bomb:
					self.bomb_number += 1
				if grid[i+1][j+1].flag:
					self.flag_number += 1
			if i + 1 >= 0 and i + 1 < cols and j - 1 >= 0 and j - 1 < rows:
				if grid[i+1][j-1].bomb:
					self.bomb_number += 1
				if grid[i+1][j-1].flag:
					self.flag_number += 1
		if self.check and self.flag_number == self.bomb_number and self.flag_number > 0 and self.number:
			if j - 1 >= 0 and j - 1 < rows:
				if not grid[i][j - 1].revealed and not grid[i][j - 1].flag and not grid[i][j - 1].question:
					grid[i][j - 1].click(i,j-1)
			if j + 1 >= 0 and j + 1 < rows:
				if not grid[i][j + 1].revealed and not grid[i][j + 1].flag and not grid[i][j + 1].question:
					grid[i][j + 1].click(i,j+1)
			if i - 1 >= 0 and i - 1 < cols:
				if not grid[i - 1][j].revealed and not grid[i - 1][j].flag and not grid[i - 1][j].question:
					grid[i - 1][j].click(i-1,j)
			if i + 1 >= 0 and i + 1 < cols:
				if not grid[i + 1][j].revealed and not grid[i + 1][j].flag and not grid[i + 1][j].question:
					grid[i + 1][j].click(i+1,j)
			if i - 1 >= 0 and i - 1 < cols and j + 1 >= 0 and j + 1 < rows:
					if not grid[i - 1][j + 1].revealed and not grid[i - 1][j + 1].flag and not grid[i - 1][j + 1].question:
						grid[i - 1][j + 1].click(i-1, j+1)
			if i - 1 >= 0 and i - 1 < cols and j - 1 >= 0 and j - 1 < rows:
				if not grid[i - 1][j - 1].revealed and not grid[i - 1][j - 1].flag and not grid[i - 1][j - 1].question:
					grid[i - 1][j - 1].click(i-1,j-1)
			if i + 1 >= 0 and i + 1 < cols and j + 1 >= 0 and j + 1 < rows:
				if not grid[i + 1][j + 1].revealed and not grid[i + 1][j + 1].flag and not grid[i + 1][j + 1].question:
					grid[i + 1][j + 1].click(i+1,j+1)
			if i + 1 >= 0 and i + 1 < cols and j - 1 >= 0 and j - 1 < rows:
				if not grid[i + 1][j - 1].revealed and not grid[i + 1][j - 1].flag and not grid[i + 1][j - 1].question:
					grid[i + 1][j - 1].click(i+1,j-1)
		if self.bomb_number == 0 and not self.bomb :
			if j - 1 >= 0 and j - 1 < rows:
				if not grid[i][j - 1].revealed and not grid[i][j - 1].flag and not grid[i][j - 1].question:
					grid[i][j - 1].click(i,j-1)
			if j + 1 >= 0 and j + 1 < rows:
				if not grid[i][j + 1].revealed and not grid[i][j + 1].flag and not grid[i][j + 1].question:
					grid[i][j + 1].click(i,j+1)
			if i - 1 >= 0 and i - 1 < cols:
				if not grid[i - 1][j].revealed and not grid[i - 1][j].flag and not grid[i - 1][j].question:
					grid[i - 1][j].click(i-1,j)
			if i + 1 >= 0 and i + 1 < cols:
				if not grid[i + 1][j].revealed and not grid[i + 1][j].flag and not grid[i + 1][j].question:
					grid[i + 1][j].click(i+1,j)
			if i - 1 >= 0 and i - 1 < cols and j + 1 >= 0 and j + 1 < rows:
					if not grid[i - 1][j + 1].revealed and not grid[i - 1][j + 1].flag and not grid[i - 1][j + 1].question:
						grid[i - 1][j + 1].click(i-1,j+1)
			if i - 1 >= 0 and i - 1 < cols and j - 1 >= 0 and j - 1 < rows:
				if not grid[i - 1][j - 1].revealed and not grid[i - 1][j - 1].flag and not grid[i - 1][j - 1].question:
					grid[i - 1][j - 1].click(i-1,j-1)
			if i + 1 >= 0 and i + 1 < cols and j + 1 >= 0 and j + 1 < rows:
				if not grid[i + 1][j + 1].revealed and not grid[i + 1][j + 1].flag and not grid[i + 1][j + 1].question:
					grid[i + 1][j + 1].click(i+1,j+1)
			if i + 1 >= 0 and i + 1 < cols and j - 1 >= 0 and j - 1 < rows:
				if not grid[i + 1][j - 1].revealed and not grid[i + 1][j - 1].flag and not grid[i + 1][j - 1].question:
					grid[i + 1][j - 1].click(i+1,j-1)
		elif not self.bomb:
			self.number = True

def make_array(cols, rows):
	arr = []
	for i in range(cols):
		temp = []
		for j in range(rows):
			temp.append(j)
		arr.append(temp)
	return arr
def flag_count():
	pygame.draw.rect(gameDisplay, black, [0, 0, display_width, display_height])
	pygame.draw.rect(gameDisplay, grey, bomb_square)
	gameDisplay.blit(smiley, smiley_place)
	flag_number = number_of_bombs
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j].flag:
				flag_number -= 1

	gameDisplay.blit(font.render(str(flag_number), True, black),
					 (bomb_square[0] + bomb_square[2]/2 - text_size/2 - 5, bomb_square[1] + bomb_square[3]/2 - text_size/2 - 6))
def setup():
	pygame.draw.rect(gameDisplay, black, [0, 0, display_width, display_height])
	global grid
	bombs = generate(number_of_bombs)
	grid = make_array(cols, rows)

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if bombs[i][j] == "bomb":
				grid[i][j] = Cell(i * w, j * h, w, h, True)
			else:
				grid[i][j] = Cell(i*w, j*h , w, h)

	pygame.display.update()
def game_over():
	global game_plan
	gameDisplay.blit(smiley_mad, smiley_place)
	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if grid[i][j].bomb:
				grid[i][j].revealed = True
	game_plan = False

def mouse_check(pos, state, click=None):
	pos_x = pos[0]
	pos_y = pos[1]
	if state == "normal":
		for i in range(len(grid)):
			for j in range(len(grid[i])):
				if pos_x > grid[i][j].x and pos_x < grid[i][j].x + grid[i][j].x_size:
					if pos_y > grid[i][j].y and pos_y < grid[i][j].y + grid[i][j].y_size:
						if not grid[i][j].flag and not grid[i][j].question and game_plan:
							grid[i][j].click(i, j)
		if pos_x > smiley_place[0] and pos_x < smiley_place[0] + smiley_size:
			if pos_y > smiley_place[1] and pos_y < smiley_place[1] + smiley_size:
				loop()
	if game_plan:
		gameDisplay.blit(smiley, smiley_place)
	if game_plan:
		if state == "flag":
			for i in range(len(grid)):
				for j in range(len(grid[i])):
					if pos_x > grid[i][j].x and pos_x < grid[i][j].x + grid[i][j].x_size:
						if pos_y > grid[i][j].y and pos_y < grid[i][j].y + grid[i][j].y_size:
							if not grid[i][j].revealed:
								if not grid[i][j].flag and not grid[i][j].question:
									grid[i][j].flag = True
									grid[i][j].question = False
								elif grid[i][j].flag:
									grid[i][j].question = True
									grid[i][j].flag = False
								elif grid[i][j].question:
									grid[i][j].question = False
									grid[i][j].flag = False
		elif state == "hold":
			for i in range(len(grid)):
				for j in range(len(grid[i])):
					if (pos_x > grid[i][j].x and pos_x < grid[i][j].x + grid[i][j].x_size and
							pos_y > grid[i][j].y and pos_y < grid[i][j].y + grid[i][j].y_size):
							grid[i][j].temp = True
					else:
						grid[i][j].temp = False
		elif state == "dobbelhold":
			temporary = []
			for i in range(len(grid)):
				for j in range(len(grid[i])):
					if (pos_x > grid[i][j].x and pos_x < grid[i][j].x + grid[i][j].x_size and
							pos_y > grid[i][j].y and pos_y < grid[i][j].y + grid[i][j].y_size):
						grid[i][j].temp = True
						temporary.append([i,j])
						if j - 1 >= 0 and j - 1 < rows:
							grid[i][j - 1].temp = True
							temporary.append([i,j-1])
						if j + 1 >= 0 and j + 1 < rows:
							grid[i][j + 1].temp = True
							temporary.append([i,j+1])
						if i - 1 >= 0 and i - 1 < rows:
							grid[i - 1][j].temp = True
							temporary.append([i-1,j])
						if i + 1 >= 0 and i + 1 < rows:
							grid[i + 1][j].temp = True
							temporary.append([i+1,j])
						if i + 1 >= 0 and i + 1 < rows and j + 1 >= 0 and j + 1 < rows:
							grid[i + 1][j + 1].temp = True
							temporary.append([i+1,j+1])
						if i - 1 >= 0 and i - 1 < rows and j + 1 >= 0 and j + 1 < rows:
							grid[i - 1][j + 1].temp = True
							temporary.append([i-1,j+1])
						if i + 1 >= 0 and i + 1 < rows and j - 1 >= 0 and j - 1 < rows:
							grid[i + 1][j - 1].temp = True
							temporary.append([i+1,j-1])
						if i - 1 >= 0 and i - 1 < rows and j - 1 >= 0 and j - 1 < rows:
							grid[i - 1][j - 1].temp = True
							temporary.append([i-1,j-1])
					else:
						if not([i,j] in temporary):
							grid[i][j].temp = False
		else:
			for i in range(len(grid)):
				for j in range(len(grid[i])):
					grid[i][j].temp = False
					if pos_x > grid[i][j].x and pos_x < grid[i][j].x + grid[i][j].x_size:
						if pos_y > grid[i][j].y and pos_y < grid[i][j].y + grid[i][j].y_size:
							if grid[i][j].number:
								grid[i][j].click(i, j, True)
			gameDisplay.blit(smiley, smiley_place)
		if state == "hold" or state == "dobbelhold":
			gameDisplay.blit(smiley_rar, smiley_place)
def draw_normal():
	for i in range(len(grid)):
		for j in range(len(grid[i])):
				grid[i][j].draw()
	pygame.display.update()

def generate(number):
	bombs = make_array(cols, rows)
	for i in range(number):
		boi = True
		while boi:
			n = random.randrange(len(bombs))
			j = random.randrange(len(bombs[0]))
			if bombs[n][j] != "bomb":
				bombs[n][j] = "bomb"
				boi = False
	return bombs
def score(seconds):
	pygame.draw.rect(gameDisplay, grey, time_square)
	gameDisplay.blit(font.render(str(seconds), True, black), (time_square[0] + 3, time_square[1] - 4))
def win(score):
	global game_plan
	win = True

	for i in range(len(grid)):
		for j in range(len(grid[i])):
			if not grid[i][j].revealed and not grid[i][j].bomb:
				win = False

	if win:
		gameDisplay.blit(cool_smiley, smiley_place)
		pygame.display.update()
		game_plan = False
		try:
			f = open("scores.txt", "r")
			boi = f.readline()
			jepp = boi.split(" ")
			prev = int(jepp[0])
			f.close()
		except:
			prev = 10000
		if score < prev:
			print("congrats you made a new highscore, whats your name")
			name = input("> ")
			f = open("scores.txt", "w")
			nope = str(score) + " " + name
			f.write(nope)
			f.close()

def loop():
	global game_plan
	game_plan = True
	game = True
	setup()
	flag_count()
	seconds = 0
	score(seconds)
	draw_normal()
	clicked = False
	clicked2 = True
	clicked3 = False
	fps = 30
	timer = 0

	while game:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()
		if click[0] == 1 and click[2] == 0:
			mouse_check(mouse, "hold", click)
			clicked = True
			draw_normal()
		elif click[0] == 0 and clicked:
			mouse_check(mouse, "normal")
			draw_normal()
			win(seconds)
			clicked = False
		elif click[2] == 1 and click[0] == 0 and clicked2:
			clicked2 = False
			if game_plan:
				mouse_check(mouse, "flag")
				gameDisplay.fill(black)
				flag_count()
				score(seconds)
				draw_normal()

		elif click[2] == 0 and not clicked2:
			clicked2 = True
		elif click[0] == 1 and click[2] == 1:
			clicked3 = True
			mouse_check(mouse, "dobbelhold")
			draw_normal()
		elif click[0] == 0 and click[2] == 0 and clicked3:
			mouse_check(mouse, "dobbel")
			clicked3 = False
			draw_normal()
		timer += 1
		if timer == fps and game_plan:
			seconds += 1
			timer = 0
			gameDisplay.fill(black)
			flag_count()
			score(seconds)


			draw_normal()
		clock.tick(fps)
loop()






