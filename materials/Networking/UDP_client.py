import socket
import sys

import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
blue = (0, 0, 128)

class AnotherPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super(AnotherPlayer, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def update(self, x, y):
        self.rect.center = (x,y)


class Player(pygame.sprite.Sprite):

    def __init__(self, name):
        super(Player, self).__init__()
        self.name = name
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 0)
        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT


class UPDClient:

    def __init__(self, host="localhost", port=9999):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.host = host
        self.port = port

    def send(self, player: Player):
        name = bytes(player.name, "utf-8")
        n = len(name)
        data = n.to_bytes(1, byteorder="big") + name + player.rect.centerx.to_bytes(2, byteorder="big") + player.rect.centery.to_bytes(2, byteorder="big")
        self.sock.sendto(data, (self.host, self.port))

    def receive(self, buff_size=1024):
        data = self.sock.recv(buff_size)
        n = int.from_bytes(data[:2], byteorder="big")
        number_of_player = data[2]
        result = []
        cursor = 3
        for i in range(number_of_player):
            n = data[cursor]
            cursor += 1
            name = str(data[cursor: cursor + n], encoding="utf-8")
            cursor += n
            x = int.from_bytes(data[cursor:cursor+2], byteorder="big")
            cursor += 2
            y = int.from_bytes(data[cursor:cursor + 2], byteorder = "big")
            cursor += 2
            result.append((name, x, y))
        return result


def main():
    pygame.init()
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    running = True
    client = UPDClient()
    player = Player(sys.argv[1])
    another_players = {}
    font = pygame.font.Font('freesansbold.ttf', 32)
    texts = []
    text = font.render(player.name, True, blue)
    texts.append(text)

    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()
        player.update(pressed_keys)
        screen.fill((255, 255, 255))
        client.send(player)
        for item in client.receive():
            name, x, y = item
            if name == player.name:
                continue
            if name not in another_players.keys():
                new_another = AnotherPlayer()
                another_players[name] = new_another
                text = font.render(name, True, blue)
                texts.append(text)

            a_p = another_players[name]
            a_p.update(x,y)
            screen.blit(a_p.surf, a_p.rect)
        screen.blit(player.surf, player.rect)
        for i, text in enumerate(texts):
            rect = text.get_rect()
            rect.y += 30*(i+1)
            screen.blit(text, rect)
        pygame.display.flip()
    pygame.quit()

if __name__ == '__main__':
    main()