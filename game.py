from random import randint

WIDTH = 1000
HEIGHT = 600
TITLE = "Totoro Run"
PLAYER_SPEED = 4

game_state = "playing"
lives_count = 3
totoro_speed = 4
score = 0

duck = Actor("shuba")
duck.pos = 100, 100

totoro = Actor("totoro")
totoro.pos = (WIDTH + 27.5, 100)

lives = Actor("3_lives", (900, 35))

coin = Actor("coin")

def draw():
    global score, game_state

    screen.fill("light blue")

    if game_state == "life_lost":
        screen.draw.text("Oops!", midtop=(WIDTH / 2, 50), fontsize=60)

    if game_state == "game_over":
        screen.draw.text("Game over!", midtop=(WIDTH / 2, HEIGHT / 2), fontsize=60)

    duck.draw()
    coin.draw()
    totoro.draw()
    lives.draw()


    show_score(score)

def on_mouse_down(pos):
    screen.fill("light blue")

def place_coin():
    coin.x = randint(15, 985)
    coin.y = randint(15, 585)

def show_score(score):
    result = str(score)

    if score == 1:
        result = result + " point"
    else:
        result = result + " points"

    screen.draw.text(result, topleft=(10, 10), fontsize = 60)

def handle_navigation():
    if game_state != "playing":
        return

    if keyboard.rshift or keyboard.lshift:
        speed = PLAYER_SPEED * 2
    else:
        speed = PLAYER_SPEED

    if keyboard.left or keyboard.a:
        duck.x = duck.x - speed

    if keyboard.right or keyboard.d:
        duck.x = duck.x + speed

    if keyboard.up or keyboard.w:
        duck.y = duck.y - speed

    if keyboard.down or keyboard.s:
        duck.y = duck.y + speed

    if duck.x > WIDTH + 31:
        duck.x = -31

    if duck.x < -31:
        duck.x = WIDTH + 31

    if duck.y > HEIGHT + 41.5:
        duck.y = -41.5

    if duck.y < -41.5:
        duck.y = HEIGHT + 41.5

def move_totoro():
    global totoro_speed, game_state

    if game_state != "playing":
        return

    totoro.x = totoro.x - totoro_speed
    if totoro.x < -27.5:
        totoro.y = randint(0, 600)
        totoro.x = WIDTH + 27.5
        totoro_speed = randint(10, 15)

def life_lost():
    global game_state
    lives.image = str(lives_count) + "_lives"

    if lives_count > 0:
        game_state = "life_lost"
        clock.schedule(start_over, 0.3)
    else:
        game_state = "game_over"

def update():
    global score
    global lives_count
    global playing

    move_totoro()

    handle_navigation()

    if duck.colliderect(totoro) and game_state == "playing":
        lives_count = lives_count - 1
        life_lost()


    if duck.colliderect(coin):
        score = score + 1
        show_score(score)
        place_coin()

def start_over():
    global game_state
    totoro.x = WIDTH + 27.5
    game_state = "playing"

place_coin()
