import pygame

class Ship():
	"""This is Class for ship managment"""
	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		#initial posoition of the ship
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
		
		# moving the ship
		self.moving_right = False
		self.moving_left = False

	def update(self):
		# 'x' atribute is update, not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#updating rect attribute based on self.x
		self.rect.x = self.x
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)
