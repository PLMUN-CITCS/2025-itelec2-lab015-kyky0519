total_sum = 0  # Initialize the sum variable

while True:
    user_input = input("Enter a number (or 'stop' to finish): ")  # Prompt the user for input

    if user_input.strip().lower() == "stop":  # Check if the sentinel value 'stop' is entered
        break  # Exit the loop

    try:
        number = float(user_input)  # Convert input to a number
        total_sum += number  # Add to total_sum
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'stop'.")  # Handle non-numeric input

print("The total sum is:", total_sum)  # Print the final total sum
