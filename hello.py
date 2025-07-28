#!/usr/bin/env python3
"""
A simple Python program demonstrating basic concepts
"""

def greet_user(name):
    """Function to greet a user with their name"""
    return f"Hello, {name}! Welcome to Python programming!"

def calculate_area(length, width):
    """Function to calculate the area of a rectangle"""
    return length * width

def main():
    """Main function that runs the program"""
    print("=== Simple Python Program ===")
    
    # Basic greeting
    print("Hello, World!")
    
    # Get user input
    user_name = input("What's your name? ")
    print(greet_user(user_name))
    
    # Simple calculation
    print("\nLet's calculate the area of a rectangle:")
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = calculate_area(length, width)
        print(f"The area is: {area}")
    except ValueError:
        print("Please enter valid numbers!")
    
    # List demonstration
    favorite_colors = ["blue", "green", "red", "purple"]
    print(f"\nMy favorite colors are: {', '.join(favorite_colors)}")
    
    # Loop demonstration
    print("\nCounting from 1 to 5:")
    for i in range(1, 6):
        print(f"Count: {i}")
    
    print("\nThanks for running this simple Python program!")

if __name__ == "__main__":
    main()