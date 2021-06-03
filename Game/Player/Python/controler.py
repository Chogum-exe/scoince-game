from pygame import key
class Key(object):
    def wasd():
        left  = pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]
        up    = pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]
        down  = pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]
        right = pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]
        return (right - left), (down - up)
    def key(key, function):
        if pygame.key.get_pressed()[pygame.K_ + key] = 1:
            function()
