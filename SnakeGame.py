import pygame
import random
import os

# ----------------- INIT -----------------
pygame.init()
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("🐍 Snake Game")

CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("comicsansms", 28)

# ----------------- COLORS -----------------
BG = (30, 30, 60)
SNAKE_COLOR = (0, 255, 170)
FOOD_COLOR = (255, 80, 80)
TEXT_COLOR = (255, 255, 255)

# ----------------- SETTINGS -----------------
BLOCK = 20
START_SPEED = 10

# ----------------- SOUNDS -----------------
eat_sound = pygame.mixer.Sound("eat.wav") if os.path.exists("eat.wav") else None
gameover_sound = pygame.mixer.Sound("gameover.wav") if os.path.exists("gameover.wav") else None

# ----------------- FUNCTIONS -----------------
def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(WIN, SNAKE_COLOR, (*block, BLOCK, BLOCK), border_radius=8)

def draw_food(food):
    pygame.draw.circle(
        WIN,
        FOOD_COLOR,
        (food[0] + BLOCK // 2, food[1] + BLOCK // 2),
        BLOCK // 2
    )

def show_text(text, y):
    render = FONT.render(text, True, TEXT_COLOR)
    rect = render.get_rect(center=(WIDTH // 2, y))
    WIN.blit(render, rect)

# ----------------- MENU SCREEN -----------------
def menu():
    while True:
        WIN.fill(BG)
        show_text("🐍 SNAKE GAME", 120)
        show_text("1 - Start Game (Easy)", 220)
        show_text("2 - Start Game (Normal)", 260)
        show_text("3 - Start Game (Hard)", 300)
        show_text("ESC - Exit Game", 360)
        show_text("Arrow Keys to Move | Space = Pause", 440)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game(8)
                elif event.key == pygame.K_2:
                    game(10)
                elif event.key == pygame.K_3:
                    game(14)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

# ----------------- MAIN GAME -----------------
def game(start_speed):
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = BLOCK, 0

    snake = [[x, y]]
    food = [
        random.randrange(0, WIDTH, BLOCK),
        random.randrange(0, HEIGHT, BLOCK)
    ]

    score = 0
    speed = start_speed
    paused = False

    running = True
    while running:
        CLOCK.tick(speed)
        WIN.fill(BG)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -BLOCK
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, BLOCK
                elif event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -BLOCK, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = BLOCK, 0
                elif event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_ESCAPE:  # STOP GAME
                    return

        if paused:
            show_text("⏸ PAUSED", HEIGHT // 2)
            pygame.display.update()
            continue

        x += dx
        y += dy

        # ❌ WALL COLLISION → GAME OVER
        if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
            if gameover_sound:
                gameover_sound.play()
            break

        head = [x, y]

        # Self collision
        if head in snake:
            if gameover_sound:
                gameover_sound.play()
            break

        snake.append(head)

        if head == food:
            score += 1
            speed += 0.3
            if eat_sound:
                eat_sound.play()
            food = [
                random.randrange(0, WIDTH, BLOCK),
                random.randrange(0, HEIGHT, BLOCK)
            ]
        else:
            snake.pop(0)

        draw_food(food)
        draw_snake(snake)
        show_text(f"Score: {score}", 20)

        pygame.display.update()

    game_over(score)

# ----------------- GAME OVER -----------------
def game_over(score):
    WIN.fill(BG)
    show_text("💀 GAME OVER", HEIGHT // 2 - 40)
    show_text(f"Score: {score}", HEIGHT // 2)
    show_text("ENTER = Menu | ESC = Exit", HEIGHT // 2 + 50)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

# ----------------- START -----------------
menu()
pygame.quit()
