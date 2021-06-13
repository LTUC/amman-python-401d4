import random

# Generate 1 num between 1 to 6
def rand_nums_generator():
    """
    Generate one number between 1 to 6
    """
    return random.randint(1,6)


if __name__ == "__main__":
    print(rand_nums_generator())
    # Generate 5 rand nums and put them in a list
    
    nums = []
    for i in range(5):
        nums.append(rand_nums_generator())
    print(nums)

    # Alternatively
    # List comprehension
    nums = [rand_nums_generator() for i in range(5)]
    print(nums)