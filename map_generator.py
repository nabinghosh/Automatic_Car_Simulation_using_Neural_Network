import pygame
from PIL import Image

# Initialize pygame
pygame.init()

# Define canvas size
WIDTH, HEIGHT = 1920, 1080

# Create a pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Map Generator")

# Define brush properties
brush_color = (0, 0, 0)  # Black color
brush_size = 40

# Fill the screen with white color
screen.fill((255, 255, 255))

# Draw starting point grid
light_green = (144, 238, 144)  # Light green color
dark_green = (0, 100, 0)       # Dark green color
grid_width = brush_size // 6
grid_height = brush_size // 4

# Car starting position
car_start_x, car_start_y = 830, 920
CAR_SIZE_X, CAR_SIZE_Y = 60, 60

# Adjust the grid position to be centered around the car's starting position
start_x = car_start_x + CAR_SIZE_X // 2 - (3 * grid_width) // 2
start_y = car_start_y + CAR_SIZE_Y // 2 - (8 * grid_height) // 2

for row in range(8):
    for col in range(3):
        color = light_green if (row + col) % 2 == 0 else dark_green
        pygame.draw.rect(screen, color, (start_x + col * grid_width, start_y + row * grid_height, grid_width, grid_height))

# Define button properties
button_color = (0, 255, 0)  # Green color
button_rect_save = pygame.Rect(WIDTH - 240, HEIGHT - 60, 100, 40)
button_rect_clear = pygame.Rect(WIDTH - 120, HEIGHT - 60, 100, 40)
font = pygame.font.Font(None, 36)
button_text_save = font.render("Save", True, (0, 0, 0))
button_text_clear = font.render("Clear", True, (0, 0, 0))

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if button_rect_save.collidepoint(event.pos):
                    # Draw starting point grid before saving
                    for row in range(8):
                        for col in range(3):
                            color = light_green if (row + col) % 2 == 0 else dark_green
                            pygame.draw.rect(screen, color, (start_x + col * grid_width, start_y + row * grid_height, grid_width, grid_height))

                    # Save the drawing to a file
                    pygame.image.save(screen, "map.png")

                    # Convert the saved image to a format compatible with PIL
                    image = Image.open("map.png")
                    image = image.convert("RGB")
                    image.save("map.png")

                    print("map.png has been generated.")
                    
                    # Close the window
                    running = False
                elif button_rect_clear.collidepoint(event.pos):
                    # Clear the canvas
                    screen.fill((255, 255, 255))
                    # Redraw the starting point grid
                    for row in range(8):
                        for col in range(3):
                            color = light_green if (row + col) % 2 == 0 else dark_green
                            pygame.draw.rect(screen, color, (start_x + col * grid_width, start_y + row * grid_height, grid_width, grid_height))
                else:
                    mouse_x, mouse_y = event.pos
                    pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), brush_size)
            elif event.button == 4:  # Mouse wheel up
                brush_size += 1
                # Update grid size to match new brush size
                grid_width = brush_size // 6
                grid_height = brush_size // 4
            elif event.button == 5:  # Mouse wheel down
                brush_size = max(1, brush_size - 1)
                # Update grid size to match new brush size
                grid_width = brush_size // 6
                grid_height = brush_size // 4
        elif event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                mouse_x, mouse_y = event.pos
                pygame.draw.circle(screen, brush_color, (mouse_x, mouse_y), brush_size)

    # Draw buttons
    pygame.draw.rect(screen, button_color, button_rect_save)
    pygame.draw.rect(screen, button_color, button_rect_clear)
    screen.blit(button_text_save, (button_rect_save.x + 10, button_rect_save.y + 5))
    screen.blit(button_text_clear, (button_rect_clear.x + 10, button_rect_clear.y + 5))

    pygame.display.flip()

pygame.quit()