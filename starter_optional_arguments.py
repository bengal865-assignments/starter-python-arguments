# Add your name here
# Current date
# Optional Arguments 

# Optional argument example
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'riley', 'lee')
print(musician)

# A function can have one or more optional arguments so that the user can
# choose to provide extra information only if they want to

# In the example above, the middle name is optional, so we (1) set the default
# value of the middle name PARAMETER to an empty string and (2) wrote the 
# optional middle name PARAMETER to the end of the parameter list

# Remember: Optional PARAMETERS always go at the end of the parameter list!

# Write a function that uses a person's age as the optional PARAMETER; set the default 
# value of the optional age parameter to 17

# Use an IF/ELSE statement in your function to generate different output strings
# depending on whether the user provides an age for the person

# For example:
# Christina is 16 and a junior at Kalkaska High School.
# Christina is a junior at Kalkaska High School.

# Your three arguments in your function call should be first name, age, and school.  Your parameter
# list will contain three parameters; use age as your optional PARAMETER.

# For help with optional arguments, see pages 138 - 139 in your Python Crash Course book.