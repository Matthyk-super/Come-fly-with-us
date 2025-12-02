#Come fly with us
# The attributes of the seats
class Seat:
   def __init__(self, seat_number, seat_type):
       self.seat_number = seat_number
       self.seat_type = seat_type
       self.is_taken = False
       if seat_type == "first":
           self.fee = 2000
       else:
           self.fee = 0

# How it all seats will appear for selecting
   def __str__(self):
       status = "Taken" if self.is_taken else "Available"
       seat_label = "Seat " + str(self.seat_number) + " (" + self.seat_type.capitalize() + " - $" + str(self.fee) + ")"
       return seat_label + ": " + status

# The plane is keeping the list of seats
class Plane:
   def __init__(self):
       self.seats = []
       self.create_seats()

# The different seat types
   def create_seats(self):
# First class: seats 1–5
       num = 1
       while num <= 5:
           self.seats.append(Seat(num, "first"))
           num = num + 1

# Regular seats: 6–18
       while num <= 18:
           self.seats.append(Seat(num, "regular"))
           num = num + 1

# Emergency seats: 19–20
       while num <= 20:
           self.seats.append(Seat(num, "emergency"))
           num = num + 1

# Shows all the seats and if they are taken or available
   def display_seats(self):
       print("\n     Seating chart     ")
       index = 0
       while index < len(self.seats):
           print(self.seats[index])
           index = index + 1
       print("\n")

# Looks for the matching seat number
   def find_seat(self, seat_number):
       index = 0
       while index < len(self.seats):
           if self.seats[index].seat_number == seat_number:
               return self.seats[index]
           index = index + 1
       return None

# Handles every requirement for buying a seat
   def purchase_seat(self, seat_number):
       seat = self.find_seat(seat_number)

# Sees if the seat exists
       if seat is None:
           print("Invalid seat number.")
           return False

# If the seat is taken
       if seat.is_taken:
           print("Sorry. That seat is already taken.")
           return False

# Emergency seat confirmation
       if seat.seat_type == "emergency":
           print("This is an emergency-exit seat.")
           confirm = input("Please agree and accept that in the event of an emergency you will open the emergency door. (yes/no): ")
           if confirm.lower() != "yes":
               print("please select another seat.")
               return False

# First-class confirmation
       if seat.seat_type == "first":
           print("The first-class seat are few and have a $2000 fee that must be paid.")
           confirm = input("Are you sure you want first-class? (yes/no): ")
           if confirm.lower() != "yes":
               print("Purchase canceled. Please select another seat.")
               return False
# Seat is secure
       seat.is_taken = True
       print("Seat " + str(seat_number) + " successfully purchased!")
       return True


# Welcomes the user and ask the user for a seat number, when quit is enter the program ends.
def main():
   plane = Plane()
   print("Welcome to flyfly airlines! What seat or seats would you like?")

   exit_program = False

   while not exit_program:
       plane.display_seats()
       user_input = input("Enter seat number to purchase (1–20), or 'quit' to exit: ")
       if user_input.lower() == "quit":
           exit_program = True
       else:
           if user_input.isdigit():
               seat_num = int(user_input)
               if 1 <= seat_num <= 20:
                   plane.purchase_seat(seat_num)
               else:
                   print("Please enter a number from 1 to 20.")
           else:
               print("Invalid input. Please enter a seat number or 'quit'.")

   print("Great! Thank you for flying with us")

main()