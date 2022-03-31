

capacity = int(input("\nEnter restaurant capacity - "))
fine = int(input("\nEnter the amount of the fine - "))
print("\nBelow in one line enter the cost of each hanger:")
hook_cost = list(map(int, input().split()))

real_capacity = int(input("\nEnter the number of incoming visitors - "))

if capacity == real_capacity:
    hook_cost = hook_cost[:capacity]
    profit = sum(hook_cost)
elif real_capacity > capacity:
    profit = sum(hook_cost)+((capacity - real_capacity)*fine)
elif capacity > real_capacity:
    hook_cost = hook_cost[:real_capacity]
    profit = sum(hook_cost)

print(profit)


