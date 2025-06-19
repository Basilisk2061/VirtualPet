import pygame
import pickle
import os 
from pet import virtualpet

#init pygame
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Virtual Pet ")
font = pygame.font.Font("Arial", 24)
clock = pygame.time.Clock()

#pet selection
pet_types = {
    "dog": {"image": "assets/dog.png", "sound": "assets/bark.mp3"},
    "cat": {"image": "assets/cat.png", "sound": "assets/meow.mp3"}
}

def choose_pet():
    print("Choose your pet:")
    for i, pet in enumerate(pet_types):
        print(f"{i + 1}. {pet}")
    choice = int(input("Enter the number of your choice: ")) - 1
    name = input("Enter a name for your pet: ")
    pet_type = list(pet_types.keys())[choice]
    info - pet_types[pet_type]
    return virtualpet(name, pet_type, info["image"], info["sound"])

SAVE_PATH = "data/pet_save.pkl"
if os.path.exists(SAVE_PATH):
    with open(SAVE_PATH, "rb") as f:
        pet = pickle.load(f)

else:
    pet = choose_pet()

#input box
input_box = pygame.Rect(50, HEIGHT - 50, WIDTH - 100, 40)
user_text = ''
active = False

def draw_interface():
    screen.fill((245, 245, 245))
    screen.blit(pet.image, (pet.x, pet.y))
    
    stats = font.render(per.get_status(), True, (0, 0, 0))
    screen.blit(stats, (50, 20))

    pygame.draw.rect(screen, (200, 200, 255), input_box, 2) 
    txt_surface = font.render(user_text, True, (0, 0, 0))
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

    pygame.display.flip()