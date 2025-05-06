def file(name='unknown',goals=0):
    """
    -> A function to show the name of a player and how many goals they scored.
    :param name: player's name
    :param goals: how many goals scored
    :return: player's championship file
    """
    return f'The player {name} scored {goals} goals in the championship.'

# Input and Processing
n = str(input("What is the player's name? ")).strip()
g = str(input("How many goals were scored? ")).strip()

# Validation
n = n if n else 'unknown'
g = g if g.isnumeric() else 0
# Output
print(file(n,g))
