# Lab 5 The Bottles Return Program
# Jesus Ramos
# 02/26/2024
"""This program calculates the number of bottles returned for the week and calculates the total payout"""

# Initialize variables
totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'
nbr_of_days = 7

# Loop to run program again
while keepGoing == 'y':
    totalBottles = 0 # Reset number of bottles per week
    for day in range(1, nbr_of_days + 1):
        todayBottles = float(input(f'Enter number of bottles returned for day #{day}: '))
        totalBottles += todayBottles

# Calculate number of bottles and payout
    totalPayout = totalBottles * 0.10
    print(f'Total number of bottles returned: {totalBottles}')
    print(f'Total payout: {totalPayout:.2f}')
    keepGoing = str(input('Do you want another week\'s worth of data? (Enter \'y\' or \'n\')'))
    if keepGoing != 'y':
        break # End loop