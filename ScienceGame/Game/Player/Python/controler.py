from pygame import key
class Key(object):
    def wasd():
        keys = pygame.key.get_pressed()

        left  = keys[pygame.K_w] or keys[pygame.K_UP]
        up    = keys[pygame.K_a] or keys[pygame.K_LEFT]
        down  = keys[pygame.K_s] or keys[pygame.K_DOWN]
        right = keys[pygame.K_d] or keys[pygame.K_RIGHT]
        return (right - left), (down - up)
        
    def key(key, function):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ + key] == 1:
            function()
