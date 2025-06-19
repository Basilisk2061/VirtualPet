import pygame

class virtualpet:
    def __init__(self, name, pet_type, image_path, sound_path):
        self.name = name
        self.per_type = pet_type
        self.image = pygame.image.load(image_path)
        self.sound = pygame.mixer.Sound(sound_path)
        self.x = 100
        self.y = 200
        self.happiness = 50
        self.energy = 100
        self.skills = {}

    def move(self,direction):
        if direction == "up":
            self.y -= 10
        elif direction == "down":
            self.y += 10
        elif direction == "left":
            self.x -= 10
        elif direction == "right":
            self.x += 10

    def speak(self):
        self.sound.play()

    def train(self, command):
        if command in self.skills:
            self.skills[command] += 1
        else:
            self.skills[command] = 1
        self.happiness += 1
        self.energy -= 5
        return f"{self.name} learned '{command}'!"
    
    
    def get_status(self):
        return {
            "name": self.name,
            "type": self.per_type,
            "happiness": self.happiness,
            "energy": self.energy,
            "skills": self.skills
        }