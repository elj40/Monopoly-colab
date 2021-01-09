import pygame
import random


class Player:
    def __init__(self, count):
        self.count = count
        self.money = 1500
        self.pos = 0
        self.properties = []
        self.trainStations = []
        self.utilities = []
        self.inJail = False
        self.jailFreeCard = False

    def buy_property(self, prop):
        if prop.bought:
            print("This property is already owned")
        elif self.money < prop.base_price:
            print("You don't have enough money")
        else:
            self.properties.append(prop)
            self.money -= prop.base_price
            prop.bought = True
            print('You now own ' + prop.name + ' and have $' + str(self.money) + 'left.')


class Property:
    def __init__(self, i, name, base_price, house_price, hotel_price):
        self.index = i
        self.name = name
        self.base_price = base_price
        self.housePrice = house_price
        self.hotelPrice = hotel_price
        self.houses = 0
        self.colour = 0, 0, 0
        self.bought = False
        self.type = "Property"
        # Add an image or a show function

    def print_info(self):
        print("Index: " + str(self.index))
        print("Name: " + str(self.name))
        print("Price: " + str(self.base_price))
        print("House price: " + str(self.housePrice))
        print("Hotel price: " + str(self.hotelPrice))


screen = 100, 100

success, fails = pygame.init()
pygame.display.set_mode(screen)

print(str(success) + " successes and " + str(fails) + " fails")
p = Player(1)

properties = []
for i in range(20):
    properties.append(Property(i, "NoName", i * 10, i * 10 + 50, i * 20))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            p.pos += 1
            p.pos %= len(properties)
            print("moved")
        elif event.type == pygame.KEYDOWN:
            p.buy_property(properties[p.pos])

    pygame.display.update()
