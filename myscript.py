# BAN 3110 - Module 2 Homework
# AI Use Statement: I used Gemini to help troubleshoot my local environment setup, 
# understand sys.argv for command-line arguments, and clarify string methods. 
# I learned how to pass arguments from the terminal and the difference between 
# input() and command-line parameters.

import math
import random
import sys

# --- Question 1: Gaussian Random Numbers ---
def generate_gaussian():
    # Generate two uniform random numbers between 0 and 1
    u = random.random()
    v = random.random()

    # Apply the Box-Muller formula: Z = sin(2*pi*v) * sqrt(-2*ln(u))
    z = math.sin(2 * math.pi * v) * math.sqrt(-2 * math.log(u))
    return u, v, z

u_val, v_val, z_val = generate_gaussian()
print(f"Generated u: {u_val:.4f}")
print(f"Generated v: {v_val:.4f}")
print("-" * 25)
print(f"Calculated Gaussian Z value: {z_val:.6f}")


# --- Question 2: Sort Two Integers ---
# Takes two integers from the command line and prints them in ascending order.
a = int(sys.argv[1])
b = int(sys.argv[2])

if a < b:
    print(f"Q2 Ascending: {a} {b}")
else:
    print(f"Q2 Ascending: {b} {a}")


# --- Question 3: Strictly Ascending or Descending ---
# Takes three double values and checks if they are strictly ordered.
x = float(sys.argv[3])
y = float(sys.argv[4])
z = float(sys.argv[5])

is_ordered = (x < y < z) or (x > y > z)
print(f"Q3 Ordered: {is_ordered}")


# --- Question 4: Richter Scale ---
# Reads a magnitude from the user and displays a descriptor.
mag = float(input("Enter earthquake magnitude: "))

if mag < 2.0:
    desc = "Micro"
elif mag < 3.0:
    desc = "Very minor"
elif mag < 4.0:
    desc = "Minor"
elif mag < 5.0:
    desc = "Light"
elif mag < 6.0:
    desc = "Moderate"
elif mag < 7.0:
    desc = "Strong"
elif mag < 8.0:
    desc = "Major"
elif mag < 10.0:
    desc = "Great"
else:
    desc = "Meteoric"

print(f"A magnitude {mag} earthquake is considered to be a {desc} earthquake.")


# --- Question 5: Written Answer ---
# What is printed: range(1, 22, 3)
# Explanation: In Python 3, range() returns a range object. 
# To see the numbers, you would need to use list(range(1, 22, 3)).


# --- Question 6: String Manipulation ---
# print(s.upper()) prints: I ATE IT.
# print(s.count('t')) prints: 2
# print(w) prints: ['I', 'ate', 'it.']


# --- Discussion Questions ---
# 1. My code acts as a CLIENT because it is the requester of services/data.
# 2. An API is like a 'Digital Waiter' that carries requests and data between systems.
# 3. DNS Lookup is like a phonebook that translates a web name into an IP address.
