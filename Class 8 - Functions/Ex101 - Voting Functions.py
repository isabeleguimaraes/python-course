#Function to determine if the person can vote based on their birth year.
def vote(year):
    from datetime import date
    age = date.today().year - year
    if age < 16:
        return f" Since you're {age} years old, your vote is PROHIBITED."
    elif 16 <= age < 18 or age > 65:
        return f" Since you're {age} years old, your vote is OPTIONAL."
    else:
        return f" Since you're {age} years old, your vote is MANDATORY."


#Main Program
year = int(input('What is your birth year? '))
print(vote(year))

