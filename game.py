#inicialização e configuração da tela:
import  pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WIDTH = 600
HEIGTH = 600

pygame.init()
game_font = pygame.font.SysFont('Ubuntu', 40)

#Posições e dimensões 
delay = 30
paddle_speed = 20
paddle_width = 10
paddle_height = 100
p1_x_pos = 10
p1_y_pos = HEIGTH / 2 - paddle_height / 2
p2_x_pos = WIDTH - paddle_width - 10
p2_y_pos = HEIGTH / 2 - paddle_height / 2
p1_score = 0
p2_score = 0
p1_up = False
p1_down = False
p2_up = False
p2_down = False
ball_x_pos = WIDTH / 2
ball_y_pos = HEIGTH / 2
ball_width = 8
ball_x_vel = -10
ball_y_vel = 0

screen = pygame.display.set_mode((HEIGTH, WIDTH))

#Desenho dos elementos na tela
def draw_Objects():
    pygame.draw.rect(screen, WHITE, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))

    pygame.draw.rect(screen, WHITE, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))

    pygame.draw.circle(screen, GREEN, (ball_x_pos, ball_y_pos), ball_width)

    #Linha divisoria
    for i in range(0, HEIGTH, 20):
        pygame.draw.rect(screen, WHITE, (WIDTH // 2 - 1, i, 2, 10))

    #cores do placar
    if p1_score > p2_score:
        p1_color = GREEN
        p2_color = RED
    elif p1_score < p2_score:
        p1_color = RED
        p2_color = GREEN
    else:
        p1_color = YELLOW
        p2_color = YELLOW

    p1_score_display = game_font.render(str(p1_score), False, p1_color)
    
    p2_score_display = game_font.render(str(p2_score), False, p2_color)

    screen.blit(p1_score_display, (WIDTH / 2 - p1_score_display.get_width() - 10, 30))
    
    screen.blit(p2_score_display, (WIDTH / 2 + 10, 30))

#Movimentação dos jogadores
def apply_player_movement():
    global p1_y_pos
    global p2_y_pos

    if p1_up:
        p1_y_pos = max(p1_y_pos - paddle_speed, 0)
    elif p1_down:
        p1_y_pos = min(p1_y_pos + paddle_speed, HEIGTH)

    if p2_up:
        p2_y_pos = max(p2_y_pos - paddle_speed, 0)
    elif p2_down:
        p2_y_pos = min(p2_y_pos + paddle_speed, HEIGTH)

#Movimentação da Bola
def aplly_ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_vel
    global ball_y_vel
    global p1_score
    global p2_score

    if(ball_x_pos + ball_x_vel < p1_x_pos + paddle_width) and (p1_y_pos < ball_y_pos + ball_y_vel + ball_width < p1_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p1_y_pos + paddle_height / 2 - ball_y_pos) / 15

        ball_y_vel = -ball_y_vel

    elif ball_x_pos + ball_x_vel < 0:
        p2_score += 1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGTH / 2
        ball_x_vel = 10
        ball_y_vel = 0

    if (ball_x_pos + ball_x_vel > p2_x_pos - paddle_width) and (p2_y_pos < ball_y_pos + ball_y_vel + ball_width < p2_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel

    elif ball_x_pos + ball_x_vel > HEIGTH:
        p1_score += 1
        ball_x_pos = WIDTH / 2
        ball_y_pos = HEIGTH / 2
        ball_x_vel = -10
        ball_y_vel = 0

    if ball_y_pos + ball_y_vel > HEIGTH or ball_y_pos + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel

    ball_x_pos += ball_x_vel
    ball_y_pos += ball_y_vel

pygame.display.set_caption('PYTHON PONG')
screen.fill(BLACK)
pygame.display.flip()
running = True

#Loop principal do jogo
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                p1_up = True
            if event.key == pygame.K_s:
                p1_down = True            
            if event.key == pygame.K_UP:
                p2_up = True  
            if event.key == pygame.K_DOWN:
                p2_down = True  
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1_up = False
            if event.key == pygame.K_s:
                p1_down = False            
            if event.key == pygame.K_UP:
                p2_up = False  
            if event.key == pygame.K_DOWN:
                p2_down = False 

    screen.fill(BLACK)
    apply_player_movement()
    aplly_ball_movement()
    draw_Objects()

    pygame.display.flip()
    pygame.time.wait(delay)
