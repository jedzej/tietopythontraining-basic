# Problem «Clock face - 1» (Hard)
# Statement
# H hours, M minutes and S seconds are passed since the midnight (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# Determine the angle (in degrees) of the hour hand on the clock face right now.
CLOCK_TIME = 12 * 60 * 60

print('Input hours passed:')
hours = int(input())
print('Input minutes passed:')
minutes = int(input())
print('Input seconds passed:')
seconds = int(input())

total_time = hours * 60 * 60 + minutes * 60 + seconds
print('Angle to 12 hour point = ' + str((total_time / CLOCK_TIME) * 360))
