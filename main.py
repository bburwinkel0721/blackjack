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

# Variable for ending the game
enough = False

# Start the game
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
if play == "y":
  play = True
  print(logo)
else:
  play = False

# The main loop for the game
while play:
  # Generate cards for the game
  your_cards = your_new_hand()
  computers_cards = computers_new_hand()
  your_score = current_your_score()
  computers_score = current_computers_score()
  
  # Check for an early blackjack
  if your_score == 21:
    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print("Win with a Blackjack!")
    play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")
  elif computers_score == 21:
    print(f"Your final hand: {your_cards}, final score: {your_score}")
    print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
    print("The house got blackjack. You lost.")
    play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")
  else:
    # Loop until your score goes above 20 or you say you have had enough
    while not enough and your_score < 21:
      # If you get blackjack
      if your_score == 21:
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
        print("Win with a Blackjack!")
        play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")
      # If you are still below 21
      elif your_score < 21:
        print(f"Your cards: {your_cards}, current score: {your_score}")
        print(f"Computer's first card: {computers_cards[0]}")
        deal_new_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if deal_new_card == "y":
          your_cards.append(deal())
          your_score = current_your_score()
          if your_score > 21:
            for ace in range(0,len(your_cards)):
              if your_cards[ace] == 11:
                your_cards[ace]=1
            your_score = current_your_score()
        else:
          enough = True
    # If your hand goes above 21
    if your_score > 21:
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
        print("You bust. You lose!")
        play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")
    # For the computer if you pass and are still below 21
    else:
      while computers_score < 17 and computers_score < your_score:
        computers_cards.append(deal())
        computers_score = current_computers_score()
        if computers_score > 21:
          for ace in range(0,len(computers_cards)):
            if computers_cards[ace] == 11:
              computers_cards[ace]=1
          computers_score = current_computers_score()
      if computers_score <= 21:
        if computers_score > your_score:
          print(f"Your final hand: {your_cards}, final score: {your_score}")
          print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
          print("You lose!")
          play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")
        elif computers_score == your_score:
          print(f"Your final hand: {your_cards}, final score: {your_score}")
          print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
          print("It was a tie.")
          play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")
        else: 
          print(f"Your final hand: {your_cards}, final score: {your_score}")
          print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
          print("You win!")
          play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")
      else:
        print(f"Your final hand: {your_cards}, final score: {your_score}")
        print(f"Computer's final hand: {computers_cards}, final score: {computers_score}")
        print("You win!")
        play = input("Do you want to play a new game of Blackjack? Type 'y' or 'n': ")

      enough = False
  play = still_playing(play)
 