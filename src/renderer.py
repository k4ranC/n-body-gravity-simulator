import pygame

WIDTH = 1200
HEIGHT = 800

BACKGROUND = (0, 0, 0)

COLOURS = {
    "star": (255, 165, 0), # Orange
    "planet": (100, 149, 237), # Blue
    "black_hole": (30, 30, 30), # Dark grey
    "particle": (180, 180, 180) # Light grey
}


class Renderer:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("N-Body Gravity Simulator")

        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 14)

        self.zoom = 0.08
        self.camera_x = 0
        self.camera_y = 0

    def world_to_screen(self, position):
        x = (position[0] - self.camera_x) * self.zoom + WIDTH / 2
        y = (position[1] - self.camera_y) * self.zoom + HEIGHT / 2
        return int(x), int(y)

    def handle_input(self):
        keys = pygame.key.get_pressed()

        move_speed = 80 / self.zoom

        if keys[pygame.K_w] or keys[pygame.K_UP]: # Move camera up
            self.camera_y -= move_speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: # Move camera down
            self.camera_y += move_speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: # Move camera left
            self.camera_x -= move_speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: # Move camera right
            self.camera_x += move_speed

    def handle_event(self, event):
        if event.type == pygame.MOUSEWHEEL: # Zoom in/out with mouse wheel
            if event.y > 0:
                self.zoom *= 1.15
            elif event.y < 0:
                self.zoom /= 1.15

            self.zoom = max(0.001, min(self.zoom, 10))

    def draw_trail(self, body, colour):
        if len(body.trail) < 2:
            return

        screen_points = [self.world_to_screen(point) for point in body.trail]

        pygame.draw.lines( # Draw the trail of the body as a line connecting its previous positions
            self.screen,
            colour,
            False,
            screen_points,
            1
        )

    def draw_label(self, body, screen_position): # Draw the name of the body next to it
        label = self.font.render(body.name, True, (220, 220, 220))
        self.screen.blit(label, (screen_position[0] + 8, screen_position[1] + 8))

    def draw(self, bodies):
        self.screen.fill(BACKGROUND)

        info = self.font.render(
            f"Zoom: {self.zoom:.4f}",
            True,
            (255, 255, 255)
        )

        self.screen.blit(info, (10, 10))

        for body in bodies:
            if not body.is_active:
                continue

            colour = COLOURS.get(body.body_type, (255, 255, 255))

            body.trail.append(body.position.copy())

            if len(body.trail) > 300:
                body.trail.pop(0) # Limit trail length to prevent memory issues

            self.draw_trail(body, colour)

            screen_position = self.world_to_screen(body.position)
            screen_radius = max(3, int(body.radius * 0.000015)) # Scale the radius for better visibility, with a minimum size of 3 pixels

            pygame.draw.circle(
                self.screen,
                colour,
                screen_position,
                screen_radius
            )

            if body.body_type != "particle":
                self.draw_label(body, screen_position) # Only draw labels for non-particle bodies to reduce clutter

        pygame.display.flip()

    def tick(self): # Limit the frame rate to 60 FPS
        self.clock.tick(60)