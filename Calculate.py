def calculate_statistics(numbers):
    if not numbers:
        return None, None, None

    # Find maximum
    maximum = max(numbers)

    # Find minimum
    minimum = min(numbers)

    # Calculate average
    average = sum(numbers) / len(numbers)

    return maximum, minimum, average

numbers = [52, 55, 90, 10, 14, 72, 33, 66]
max_value, min_value, avg_value = calculate_statistics(numbers)

print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
print(f"Average: {avg_value}")