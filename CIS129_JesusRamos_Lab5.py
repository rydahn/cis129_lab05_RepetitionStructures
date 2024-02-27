# Lab 5 The Bottles Return Program
# Jesus Ramos
# 02/26/2024
"""This program calculates the number of bottles returned for the week and calculates the total payout"""

# Initialize variables
total_bottles = 0
counter = 1
today_bottles = 0
total_payout = 0
keep_going = 'y'
nbr_of_days = 7

# Loop to run program again
while keep_going == 'y':
    total_bottles = 0 # Reset number of bottles per week
    for day in range(1, nbr_of_days + 1):
        today_bottles = float(input(f'Enter number of bottles returned for day #{day}: '))
        total_bottles += today_bottles

# Calculate number of bottles and payout
    total_payout = total_bottles * 0.10
    print(f'Total number of bottles returned: {total_bottles}')
    print(f'Total payout: {total_payout:.2f}')
    keep_going = str(input('Do you want another week\'s worth of data? (Enter \'y\' or \'n\')'))
    if keep_going != 'y':
        break # End loop
