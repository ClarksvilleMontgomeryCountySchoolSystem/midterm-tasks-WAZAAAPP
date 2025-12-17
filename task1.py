# Given variables
party_pizza_mini = 14
large = 8
medium = 6
people = 6  # friends

# ------------------------------------------------------------------------------------------------
# Calculate slices
total_slices = party_pizza_mini + large + medium
print("Total slices:", total_slices)

# Update people to include yourself
people += 1

# Calculate share and leftover
share = total_slices // people
leftover = total_slices % people

# Print share results
print("Slices per person:", share)
print("Leftover slices:", leftover)

# Eric and Brandon are coming too
people += 2

# Recalculate share and leftover
share = total_slices // people
leftover = total_slices % people

# Print updated results
print("Updated slices per person:", share)
print("Updated leftover slices:", leftover)

# Mom upgrades the mini to a party pizza (same as 2 minis)
total_slices = (party_pizza_mini * 2) + large + medium

# Recalculate share and leftover
share = total_slices // people
leftover = total_slices % people

# Print final results
print("Final slices per person:", share)
print("Final leftover slices:", leftover)
print("...for Mr. Hollow Leg")
