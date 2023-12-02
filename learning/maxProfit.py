def maximize_profits(cut_cost, unit_price, num_sausages, lengths):
    max_length = max(lengths)
    max_profit = 0

    for L in range(1, max_length + 1):
        total_length = sum(max(0, sausage - L) for sausage in lengths)
        total_cut_cost = total_length * cut_cost
        total_profit = total_length * L * unit_price - total_cut_cost

        max_profit = max(max_profit, total_profit)

    return max_profit

# Input reading and processing
cut_cost = float(input("Enter cut cost: "))
unit_price = float(input("Enter unit price: "))
num_sausages = int(input("Enter number of sausages produced: "))
lengths = [int(input()) for _ in range(num_sausages)]

# Output the result
result = maximize_profits(cut_cost, unit_price, num_sausages, lengths)
print("The maximum amount of money Mr. Sage can make is:", result)
