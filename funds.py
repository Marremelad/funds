import csv
from os import system
from time import sleep

def main():
    budget = 0
    
    while True:
    
        choice = choices(budget)
        
        if choice == "1":
            budget = change_budget(budget)
        elif choice == "2":
            display()
        elif choice == "3":
            budget = purchase(budget)
        elif choice == "4":
            system("cls")
            print("Thank you for using, budgethantering!")
            break   

def choices(budget):
  while True:
    system("cls")
    print(f"Budget: {budget}kr\n\n    MENU    \n\n1.Budget\n\n2.Purchases\n\n3.Add purchase\n\n4.Exit")
    print("\nSelect an option by typing its associated number and pressing enter. Example '1' for 'Budget'.")
    choices = ["1", "2", "3", "4"]
  
    choice = input().lower()
    
    if choice in choices:
      break   
      
  return choice

def change_budget(budget):
  while True:
    system("cls")
    print(f"Current budget: {budget}")
    
    answer = input("Would you like to add or remove money from your budget?\nPress '+' to add or '-' to remove.\n\nPress 'enter' to return to the menu.\n")
 
    if answer == "+":
      while True:
        system("cls")
        try:  
          budget += int(input("Amount to add?\n"))
          return budget
        except ValueError:
          system("cls")
          print("Amount has to be in numerical.")
          sleep(2)
    elif answer == "-":
      system("cls")
      while True:
        try:
          budget -= int(input("Amount to remove?\n"))
          return budget
        except ValueError:
          system("cls")
          print("Amount has to be numerical")
          sleep(2)
    elif answer == "":
      return budget
    else:
      system("cls")
      
def purchase(budget):
    
      while True:
          system("cls")
          try:
              purchase = input("Purchase: ")
              while True:
                  try:
                      price = int(input("Price: "))
                      break
                  except ValueError:
                      print("price must be an integer")    
              budget -= price
              if budget < 0:
                  choice = input("Too expensive, Would you still like to buy?\n")
                  if choice == "yes":
                      add_to_file(purchase, price)
                      return budget
                  else:
                      budget += price
                      break
              else:
                 add_to_file(purchase, price)              
          except EOFError:
              break
      return budget

def add_to_file(purchase, price):
  with open("purchases.csv", "a", newline = "" ) as file:
    writer = csv.DictWriter(file, fieldnames=["purchase", "price"])
    writer.writerow({"purchase": purchase, "price": price})
  return
   
def display():  
    while True:
        total = 0
        system("cls")
        with open("purchases.csv") as file:
            writer = csv.DictReader(file, fieldnames=["purchase", "price"])
            for row in writer:
                total += int(row["price"])
                print(f"{row['purchase']}, {row['price']}kr")
            print(f"Total: {total}kr")
        back = input("Press 'enter' to return to the menu.")
        if not back:
           break
main()