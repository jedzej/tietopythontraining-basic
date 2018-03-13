#https://snakify.org/lessons/for_loop_range/problems/lost_card/
#piotrsta

number_of_cards = int(input())
summary_value = 0

for i in range(1, number_of_cards + 1):
    summary_value += i
    
for i in range(number_of_cards - 1):
    summary_value -= int(input())
print(summary_value)
