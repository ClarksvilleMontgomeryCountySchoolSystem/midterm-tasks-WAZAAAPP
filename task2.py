# Given variables
allowance = 20
dishes, room, trash, lawn, laundry, vacuum = 4, 6, 3, 10, 5, 7
candy, soda, game, movie, toy, snack = 5, 3, 18, 12, 8, 4

"""
CHORE MENU - Earn Money:        PURCHASE MENU - Spend Money:
dishes = $4                      candy = $5
room = $6                        soda = $3
trash = $3                       game = $18
lawn = $10                       movie = $12
laundry = $5                     toy = $8
vacuum = $7                      snack = $4
"""

#Do Not use Ctrl+A to select code. Only copy the code below this line.
#------------------------------------------------------------------------------------------------
# Week 1: Chores and first purchase
allowance += dishes   # Did Dishes (+$4)
allowance += lawn     # Mowed lawn (+$10)
allowance -= candy    # Bought candy (-$5)

# Week 2: Bonus week and purchase
allowance += 5        # Bonus (+$5)
allowance += vacuum   # Vacuumed (+$7)
allowance -= toy      # Bought toy (-$8)

# Week 3: Savings
allowance -= 5        # Saving deposit (-$5)

# Print final allowance
print(f"Final allowance: ${allowance}")
