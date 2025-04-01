"""
Python Coding Style Guide

This guide follows PEP 8 conventions with examples of good and bad practices.
"""

# Variable Naming
# Bad Example
tempVar = 100  # Wrong: Variable names should not use camelCase

# Good Example
temp_var = 100  # Correct: Use snake_case


# Indentation
# Bad Example
def incorrect_indent():
  a = 5
       b = 10  # Wrong: Inconsistent indentation
  return a + b

# Good Example
def correct_indent():
    a = 5
    b = 10  # Correct: Each level is indented with 4 spaces
    return a + b


# Spacing
# Bad Example
y=15*3  # Wrong: Missing spaces around operators

# Good Example
y = 15 * 3  # Correct: Spaces around operators improve readability


# Line Length
# Bad Example
long_text = "This line exceeds the recommended 79-character limit, reducing readability."  # Wrong

# Good Example
long_text = (
    "This line is properly split to enhance readability."
)  # Correct


# Function Definitions
# Bad Example
def bad_func(a,b):
    return(a+b)  # Wrong: Missing spaces after commas, incorrect parentheses usage

# Good Example
def good_func(a, b):
    return a + b  # Correct: Proper spacing and naming


# Import Statements
# Bad Example
import sys, os  # Wrong: Multiple imports on one line

# Good Example
import sys
import os  # Correct: One import per line


# Comments and Documentation
# Bad Example
def undocumented_function():
    pass  # Wrong: Function lacks documentation

# Good Example
def documented_function():
    """This function does nothing but includes proper documentation."""
    pass  # Correct
