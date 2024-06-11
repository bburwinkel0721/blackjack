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