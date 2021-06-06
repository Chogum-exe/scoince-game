class KeyHandler:
    def __init__(self, pygame):
        self.pygame = pygame
    
    def wasd(self):
        keys = self.pygame.key.get_pressed()

        up  = keys[self.pygame.K_w] or keys[self.pygame.K_UP]
        left    = keys[self.pygame.K_a] or keys[self.pygame.K_LEFT]
        down  = keys[self.pygame.K_s] or keys[self.pygame.K_DOWN]
        right = keys[self.pygame.K_d] or keys[self.pygame.K_RIGHT]

        return (right - left), (down - up)
        
    def key(self, key, function):
        keys = self.pygame.key.get_pressed()
        if keys[self.pygame.K_ + key] == 1:
            function()