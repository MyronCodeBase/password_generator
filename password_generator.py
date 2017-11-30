"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of 
lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password 
every time the user asks for a new password. Include your run-time code in a main method.

"""
import random


def password_generator(x):
    generator = True
    user_input = input("Generate Password? (Yes, or quit) ").lower()
    while generator:
        if user_input == 'quit':
            print("Thanks for not using password generator!")
            generator = False
            break

        while user_input not in ('yes', 'y'):
            user_input = input("Generate Password (Yes, or quit) ").lower()

        if user_input == 'yes' or user_input == 'y':
            generator_options = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXUYZ", "!@#$%^&*()_+=-", "123456789"]
            password = []
            while len(password) < x:
                for i in generator_options:
                    password.append(random.choice(i))
            join_password = "".join(password)
            print(join_password)
            user_input = input("\nGenerate Password? (Yes, or quit) ").lower()
            if user_input == 'quit':
                print("Thanks for using password generator!")
                generator = False
                break

            if user_input not in ('yes', 'y'):
                user_input = input("Generate Password (Yes, or quit) ")

# Generates a 24 character strong password
password_generator(24)
