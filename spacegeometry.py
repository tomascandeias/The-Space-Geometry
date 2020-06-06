import pygame
import math
import random

pygame.init()

screenWidth = 800
screenHeight = 600

win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("The Space Geometry")

# img
bg = pygame.image.load("background.png")
ss_up = pygame.image.load("spaceship_up.png")
ss_right = pygame.image.load("spaceship_right.png")
ss_down = pygame.image.load("spaceship_down.png")
ss_left = pygame.image.load("spaceship_left.png")
heart_icon = pygame.image.load("heart_icon.png")

clock = pygame.time.Clock()
hearts = 3
y_places = [0, 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560, 600, 600]


class SpaceShip(object):
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.hitbox = (self.x, self.y, self.width + 8, self.height)
		self.vel = 6
		self.up = False
		self.right = True
		self.down = False
		self.left = False
	
	def draw(self, win):
		if self.up:
			win.blit(ss_up, (self.x, self.y))
			self.hitbox = (self.x, self.y, self.width + 8, self.height - 10)
		if self.right:
			win.blit(ss_right, (self.x, self.y))
			self.hitbox = (self.x, self.y, self.width, self.height)
		if self.down:
			win.blit(ss_down, (self.x, self.y))
			self.hitbox = (self.x, self.y, self.width + 8, self.height - 10)
		if self.left:
			win.blit(ss_left, (self.x, self.y))
			self.hitbox = (self.x, self.y, self.width, self.height)
	
	# pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
	
	def hit(self):
		self.x = 50
		self.y = screenHeight / 2
		self.up = False
		self.right = True
		self.down = False
		self.left = False
		
		# fontHit = pygame.font.SysFont("bronsimard", 50, True)
		# if hearts > 0:  # lost a heart message
		# 	textHit = fontHit.render("You lost a life", 1, (255, 255, 255))
		# 	win.blit(textHit, ((screenWidth / 2) - (textHit.get_width() / 2), (screenHeight / 2) - 50))
		
		pygame.display.update()


class GeoFigure(object):
	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.x = screenWidth - self.width
		self.y = y_places[random.randint(0, len(y_places) - 1)]
		self.hitbox = (self.x, self.y, self.width, self.height)
		self.vel = 2 * random.randint(1, 4)  # 2, 4, 6, 8
	
	def draw(self, win):
		pygame.draw.rect(win, (255, 255, 255), (self.x, self.y, self.width, self.height))
		
		self.hitbox = (self.x, self.y, self.width, self.height)
	
	# pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
	
	def increaseVel(self, newVel):
		self.vel = newVel


def getTime():
	time = pygame.time.get_ticks() / 1000
	minutes = math.floor(time / 60)
	seconds = time - (minutes * 60)
	return minutes, seconds


def getTimeSum(m2, s2, m1, s1):
	t = (s2 + (m2 * 60)) + (s1 + (m1 * 60))
	minutes = math.floor(t / 60)
	seconds = t - (minutes * 60)
	return minutes, seconds


def getTimeSubtraction(m2, s2, m1, s1):
	t = (s2 + (m2 * 60)) - (s1 + (m1 * 60))
	minutes = math.floor(t / 60)
	seconds = t - (minutes * 60)
	return minutes, seconds


def getDisplayTime():
	M, S = getTime()
	
	if len(times) == 1:
		M, S = getTime()
		M, S = getTimeSubtraction(M, S, times.get(1)[0], times.get(1)[1])
	if len(times) == 2:
		M, S = getTime()
		tSum = getTimeSum(times.get(2)[0], times.get(2)[1], times.get(1)[0], times.get(1)[1])
		# print("m=" + str(M) + " s=" + str(S) + "\tmTimes=" + str(times.get(2)[0]) + " sTimes=" + str(times.get(2)[1]))
		M, S = getTimeSubtraction(M, S, tSum[0], tSum[1])
	
	return M, S


def redrawGameWindow():
	win.blit(bg, (0, 0))
	
	if hearts > 0:
		# Lives left
		text = font.render(str(hearts), 1, (178, 34, 34))  # firebrick
		win.blit(text, (screenWidth - 50, 20))
		win.blit(heart_icon, (screenWidth - 35, 15))
		
		# Time in mm:ss display
		minutes, seconds = getDisplayTime()
		textTime = font.render("{:02.0f}:{:02.0f}".format(minutes, seconds), 1, (178, 34, 34))  # firebrick
		win.blit(textTime, (screenWidth - (screenWidth / 2) - (textTime.get_width() / 2), 20))
		
		ss.draw(win)
		for fg in figures:
			fg.draw(win)
		
		pygame.display.update()
	else:
		text1 = font.render("1º {:02.0f}:{:02.0f}".format(times.get(1)[0], times.get(1)[1]), 1,
							(152, 251, 152))  # palegreen
		text2 = font.render("2º {:02.0f}:{:02.0f}".format(times.get(2)[0], times.get(2)[1]), 1, (152, 251, 152))
		text3 = font.render("3º {:02.0f}:{:02.0f}".format(times.get(3)[0], times.get(3)[1]), 1, (152, 251, 152))
		
		win.blit(text1, ((screenWidth / 2) - (text1.get_width() / 2), (screenHeight / 2) - 100))
		win.blit(text2, ((screenWidth / 2) - (text2.get_width() / 2), (screenHeight / 2) - 50))
		win.blit(text3, ((screenWidth / 2) - (text3.get_width() / 2), (screenHeight / 2)))
		
		pygame.display.update()
		pygame.time.delay(5000)


font = pygame.font.SysFont("bronsimard", 32, True)  # hearts font
ss = SpaceShip(50, (screenHeight / 2), 50, 60)
figures = [GeoFigure(32, 32), GeoFigure(32, 32), GeoFigure(32, 32), GeoFigure(32, 32)]  # starts with 4 figures
times = dict()

# counter
pygame.time.set_timer(pygame.USEREVENT, 1000)
counter = 3
count = 0  # how many times the counter resets

run = True
while run and hearts > 0:
	clock.tick(30)
	
	for event in pygame.event.get():
		if event.type == pygame.USEREVENT:
			counter -= 1
		if event.type == pygame.QUIT:
			run = False
	
	# reset counter and count++
	if counter == 0:
		counter = 3
		count += 1
		
		if count % 5 == 0 and len(figures) <= 30:
			figures.append(GeoFigure(32, 32))
		
		if count % 10 == 0 and count <= 40:  # time played is [00:30, 1:00, 1:30, 2:00]
			for fg in figures:
				fg.increaseVel(2 * random.randint(2, 4))  # 4, 6, 8
		
		if count % 10 == 0 and count > 40:  # time played is [2:30, 3:00, 3:30, ...]
			for fg in figures:
				fg.increaseVel(2 * random.randint(3, 5))  # 6, 8, 10
	
	# Moving figures and check spaceship hit
	print(len(figures))
	for fg in figures:
		if screenWidth > fg.x > -fg.width:
			fg.x -= fg.vel
		else:
			fg.x = screenWidth - 32
			fg.y = y_places[random.randint(0, len(y_places) - 1)]
		
		if ss.hitbox[1] < fg.hitbox[1] + fg.hitbox[3] and ss.hitbox[1] + ss.hitbox[3] > fg.hitbox[1] and ss.hitbox[0] + \
				ss.hitbox[2] > fg.hitbox[0] and ss.hitbox[0] < fg.hitbox[0] + fg.hitbox[2]:
			figures.clear()
			figures = [GeoFigure(32, 32), GeoFigure(32, 32)]
			hearts -= 1
			counter = 5
			count = 0
			ss.hit()
	
	# time table by hearts
	if len(times) == 0 and hearts == 2:
		times[-(hearts - 3)] = getTime()
	if len(times) == 1 and hearts == 1:
		m, s = getTime()
		times[-(hearts - 3)] = getTimeSubtraction(m, s, times.get(1)[0], times.get(1)[1])
	if len(times) == 2 and hearts == 0:
		m, s = getTime()
		mSum, sSum = getTimeSum(times.get(2)[0], times.get(2)[1], times.get(1)[0], times.get(1)[1])
		times[-(hearts - 3)] = getTimeSubtraction(m, s, mSum, sSum)
	
	# Inputs
	keys = pygame.key.get_pressed()
	if keys[pygame.K_UP] and ss.y > ss.vel:
		ss.up = True
		ss.right = False
		ss.down = False
		ss.left = False
		ss.y -= ss.vel
	
	if keys[pygame.K_RIGHT] and ss.x < 200 - ss.vel:
		ss.up = False
		ss.right = True
		ss.down = False
		ss.left = False
		ss.x += ss.vel
	
	if keys[pygame.K_DOWN] and ss.y < screenHeight - ss.height - ss.vel:
		ss.up = False
		ss.right = False
		ss.down = True
		ss.left = False
		ss.y += ss.vel
	
	if keys[pygame.K_LEFT] and ss.x > ss.vel:
		ss.up = False
		ss.right = False
		ss.down = False
		ss.left = True
		ss.x -= ss.vel
	
	redrawGameWindow()

pygame.quit()
