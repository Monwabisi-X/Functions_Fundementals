from math import pi


"""
Python Functions Workshop Exercises
---------------------------------
This file contains exercises that progress from basic to advanced function concepts.
Each exercise includes detailed documentation and examples of common pitfalls.
"""

# Exercise 1: Basic Function Definition and Documentation
def greet_user():
    """
    Create a function that prints 'Hello, World!'
    
    Common mistakes to avoid:
    - Forgetting parentheses when calling the function
    - Confusing print with return
    - Inconsistent indentation
    """
    # TODO: Implement this function
    print('Hello, World!')
  

# Exercise 2: Function Parameters and Type Hints
def personalized_greeting(name):
    """
    Create a function that takes a name parameter and returns a personalized greeting
    
    Parameters:
        name (str): The name of the person to greet
        
    Returns:
        str: A personalized greeting message
        
    Raises:
        TypeError: If name is not a string
        
    Examples:
        >>> personalized_greeting("Alice")
        'Hello, Alice!'
        >>> personalized_greeting(123)
        Raises TypeError
    """
    # TODO: Implement this function
    if name and isinstance(name, str):
        return f"Hello, {name}!"
    else:
        raise TypeError
  

# Exercise 3: Multiple Parameters and Default Values
def calculate_rectangle_area(length, width = None):
    """
    Calculate the area of a rectangle. If width is not provided, calculate area of a square.
    
    Parameters:
        length (float): The length of the rectangle
        width (float, optional): The width of the rectangle. Defaults to length if None.
        
    Returns:
        float: The area of the rectangle
        
    Raises:
        ValueError: If length or width is negative
        TypeError: If inputs are not numbers
        
    Common mistakes to avoid:
    - Not handling negative inputs
    - Not validating parameter types
    - Using mutable default values
    """
    # TODO: Implement this function
    if length < 0 or width < 0:
        raise ValueError
    if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
        raise TypeError
    else:
        if not width:
            width = length
        return length * width
  

# Exercise 4: Global vs Local Scope
score = 0  # Global variable

def update_score(points):
    """
    Update the global score variable by adding points
    
    Parameters:
        points (int): Points to add to the score
        
    Returns:
        int: The new score after adding points
        
    Common mistakes to avoid:
    - Forgetting 'global' keyword
    - Shadowing global variables **********************
    - Overusing global variables
    """
    # TODO: Implement this function
    global score
    
    if not isinstance(points, (int, float)):
        raise TypeError
    else:
        score += points
    return score
  

# Exercise 5: Multiple Return Values and Tuple Unpacking
def get_circle_properties(radius):
    """
    Calculate area and circumference of a circle
    
    Parameters:
        radius (float): The radius of the circle
        
    Returns:
        tuple: (area(float), circumference(float)) of the circle
        
    Examples:
        >>> area, circumference = get_circle_properties(1)
        >>> print(f"Area: {area:.2f}, Circumference: {circumference:.2f}")
        Area: 3.14, Circumference: 6.28
    """
    # TODO: Implement this function
    if radius < 0:
        raise ValueError
    else:
        area = pi * (radius ** 2)
        circumference = 2 * pi * radius
        return area, circumference
  

# Exercise 6: Input Validation and Error Handling
def calculate_bmi(weight, height):
    """
    Calculate BMI (Body Mass Index) with proper input validation
    
    Parameters:
        weight (float): Weight in kilograms
        height (float): Height in meters
        
    Returns:
        float: BMI value rounded to 1 decimal place
        
    Raises:
        ValueError: If weight or height is negative or zero
        TypeError: If inputs are not numbers
    """
    # TODO: Implement this function
    if height <= 0 or weight <= 0:
        raise ValueError
    if not isinstance(height, (int, float)) or not isinstance(weight, (int, float)):
        raise TypeError
    else:
        return weight / (height ** 2)
  

# Exercise 7: Recursion with Base Case and Error Handling
def factorial(n):
    """
    Calculate the factorial of a number using recursion
    
    Parameters:
        n (int): The number to calculate factorial for
        
    Returns:
        int: The factorial of n
        
    Raises:
        ValueError: If n is negative
        RecursionError: If recursion depth is exceeded
        
    Common mistakes to avoid:
    - Missing base case
    - Not handling negative numbers
    - Not considering stack overflow **********************
    """
    # TODO: Implement this function
    if n < 0:
        raise ValueError
    if not isinstance(n, int):
        raise TypeError
    if n == 0:
        return 1
    return n * factorial(n -1)
  

# Exercise 8: Complex Return Types and Dictionary Handling
def analyze_numbers(numbers):
    """
    Analyze a list of numbers and return various statistics
    
    Parameters:
        numbers (list): List of numbers to analyze
        
    Returns:
        dict: Dictionary containing:
            - 'sum': Sum of numbers
            - 'average': Average of numbers
            - 'maximum': Maximum number
            - 'minimum': Minimum number
            
    Raises:
        ValueError: If the list is empty
        TypeError: If any element is not a number
        
    Example:
        >>> stats = analyze_numbers([1, 2, 3, 4, 5])
        >>> print(f"Average: {stats['average']}")
        Average: 3.0
    """
    # TODO: Implement this function
    if numbers == []:
        raise ValueError
    
    for i in numbers:
        if not isinstance(i, (int, float)):
            raise TypeError
    
    _sum = sum(numbers)
    average = _sum / len(numbers)
    maximum = max(numbers)
    minnimum = min(numbers)
    
    return {"sum":_sum, "average":average, "maximum":maximum, "minimum":minnimum}
  

# Exercise 9: Default Parameters and Type Checking
def create_profile(name, age, occupation="Student"):
    """
    Create a user profile with optional occupation
    
    Parameters:
        name (str): User's name
        age (int): User's age
        occupation (str, optional): User's occupation. Defaults to "Student"
        
    Returns:
        dict: User profile dictionary
        
    Raises:
        TypeError: If name is not str or age is not int
        ValueError: If age is negative
    """
    # TODO: Implement this function
    if not isinstance(name, str) or not isinstance(age, int):
        raise TypeError
    
    if age < 0:
        raise ValueError
    
    return {"name":name, "age":age, "occupation":occupation}
  

# Exercise 10: Complex Logic and Multiple Validation
def validate_password(password: str):
  
    """
    Validate a password based on multiple criteria
    
    Password must:
    - Be at least 8 characters long
    - Contain at least one uppercase letter
    - Contain at least one lowercase letter
    - Contain at least one number
    
    Parameters:
        password (str): Password to validate
        
    Returns:
        bool: True if password meets all criteria, False otherwise
        
    Raises:
        TypeError: If password is not a string
        
    Examples:
        >>> validate_password("Abc12345")
        True
        >>> validate_password("abc123")  # Too short
        False
        >>> validate_password("12345678")  # No letters
        False
        >>> validate_password("abcdefgh")  # No numbers or uppercase
        False
        >>> validate_password(12345)  # Not a string
        Raises TypeError
        
    Common mistakes to avoid:
    - Not handling non-string inputs
    - Using regular expressions without proper error handling
    - Not checking all criteria independently
    - Forgetting to validate input type before processing
    """
    # TODO: Implement this function
    if not isinstance(password, str):
        raise TypeError
    
    if len(password) < 8:
        return False
    
    if password.isalpha() or password.isnumeric():
        return False
    
    if password.isupper() or password.islower():
        return False
    
    else: return True


if __name__ == "__main__":
    
    # Example usage of functions
    print("Testing greet_user():")
    greet_user()
    
    print("\nTesting personalized_greeting():")
    greeting = personalized_greeting("Alice")
    print(greeting)
    
    print("\nTesting calculate_rectangle_area():")
    area = calculate_rectangle_area(5, 3)
    print(f"Rectangle area: {area}")
