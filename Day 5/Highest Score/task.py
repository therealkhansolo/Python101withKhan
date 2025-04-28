student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]


# Function to find the maximum value
def find_max(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty

    max_value = numbers[0]  # Assume the first element is the max
    for num in numbers[1:]:  # Start from the second element
        if num > max_value:  # If we find a larger number
            max_value = num  # Update the max value
    return max_value


# Function to find the minimum value
def find_min(numbers):
    if len(numbers) == 0:
        return None  # Return None if the list is empty

    min_value = numbers[0]  # Assume the first element is the min
    for num in numbers[1:]:  # Start from the second element
        if num < min_value:  # If we find a smaller number
            min_value = num  # Update the min value
    return min_value


# Example usage:
numbers = [3, 5, 7, 2, 8, 1]
print(f"Maximum: {find_max(numbers)}")  # Output: Maximum: 8
print(f"Minimum: {find_min(numbers)}")  # Output: Minimum: 1

# List of student scores
student_scores = [8, 65, 89, 86, 55, 91, 64, 89]

# Initialize the highest score with the first element in the list
highest_score = student_scores[0]

# Loop through the list starting from the second element
for score in student_scores[1:]:
    # If the current score is greater than the current highest score
    if score > highest_score:
        # Update the highest score
        highest_score = score

# Print the highest score
print(highest_score)

