import pygame
import sys

def initialize_pygame():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Fibonacci Sequence')
    return screen

def generate_fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def main():
    try:
        num_fib = int(input("Enter the number of Fibonacci numbers to display: "))
        if num_fib <= 0:
            raise ValueError("Number must be positive.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit()

    screen = initialize_pygame()
    font = pygame.font.Font(None, 36)
    fib_numbers = generate_fibonacci_sequence(num_fib)

    white = (255, 255, 255)
    black = (0, 0, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(white)
        
        for i, number in enumerate(fib_numbers):
            text = font.render(str(number), True, black)
            screen.blit(text, (50, 30 * i + 20))
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
