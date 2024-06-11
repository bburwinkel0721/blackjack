# Load imports
from art import logo
from replit import clear
import random

# Create the deal function
def deal():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

# Create the new hand function
def your_new_hand():
  your_cards = []
  your_cards.append(deal())
  your_cards.append(deal())
  return your_cards

# Create a function for the computers hand
def computers_new_hand():
  computers_cards = []
  computers_cards.append(deal())
  computers_cards.append(deal())
  return computers_cards

# Create a function for tracking your current score
def current_your_score():
  your_score = 0
  for card in range(len(your_cards)):
    your_score += your_cards[card]
  return your_score

# Create a function for tracking the computer's score
def current_computers_score():
  computers_score = 0
  for card in range(len(computers_cards)):
    computers_score += computers_cards[card]
  return computers_score

# Create a function to check if we are still playing
def still_playing(answer):
  if answer == "y":
    play = True
    clear()
    print(logo)
  else:
    play = False
    clear()
  return play