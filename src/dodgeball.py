import pygame
import random

# Model
class Model:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.ball_size = 30
        self.ball_speed = 5
        self.player_size = 50
        self.player_speed = 8
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)
        self.player_x = self.screen_width // 2
        self.player_y = self.screen_height - 50
        self.balls = []
        self.score = 0
        self.background = pygame.image.load("gui.jpg")

    def move_player(self, dx):
        self.player_x += dx
        if self.player_x < 0:
            self.player_x = 0
        elif self.player_x > self.screen_width - self.player_size:
            self.player_x = self.screen_width - self.player_size

    def move_balls(self):
        for i in range(len(self.balls)):
            self.balls[i][1] += self.ball_speed
            if self.balls[i][1] > self.screen_height:
                self.balls[i][0] = random.randint(0, self.screen_width - self.ball_size)
                self.balls[i][1] = random.randint(-self.screen_height, 0)
                self.score += 1

    def check_collision(self):
        for ball in self.balls:
            if (self.player_x < ball[0] + self.ball_size and
                self.player_x + self.player_size > ball[0] and
                self.player_y < ball[1] + self.ball_size and
                self.player_y + self.player_size > ball[1]):
                    return True
        return False

    def increase_difficulty(self):
        self.ball_speed += 0.05

# View
class View:
    def __init__(self, model):
        self.model = model
        pygame.init()

        self.screen = pygame.display.set_mode((self.model.screen_width,
        self.model.screen_height))
        pygame.display.set_caption("Dodge Ball")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 36)

    def draw_player(self):
        pygame.draw.rect(self.screen, self.model.blue,
        (self.model.player_x, self.model.player_y, self.model.player_size,
        self.model.player_size))

    def draw_ball(self, x, y):
        pygame.draw.circle(self.screen, self.model.red, (x, y), self.model.ball_size // 2)

    def draw_score(self):
        score_text = self.font.render("Score: {self.model.score}", True, self.model.white)
        self.screen.blit(score_text, (10, 10))

    def draw_background(self):
        self.screen.blit(self.model.background, (0, 0))

    def draw(self):
        self.draw_background()
        self.draw_player()
        for ball in self.model.balls:
            self.draw_ball(ball[0], ball[1])
            self.draw_score()
        pygame.display.flip()

    # Controller
    class Controller:
        def __init__(self, model):
            self.model = model

        def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.model.move_player(-self.model.player_speed)
                    elif event.key == pygame.K_RIGHT:
                        self.model.move_player(self.model.player_speed)
            return True

# Main
def main():
    model = Model()
    view = View(model)
    controller = View.Controller(model)

    running = True
    while running:
        running = controller.handle_events()
        model.move_balls()
        if model.check_collision():
            running = False
        model.increase_difficulty()
        view.draw()
        view.clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()