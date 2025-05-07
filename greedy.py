from time import perf_counter
dataset = "datasets\pr3_200.txt"    # Select Dataset

start_time = perf_counter()

with open(dataset) as f:
    items = f.readlines()

list_of_items = []

for line in items:
    x = line.rstrip().split("\t")
    list_of_items.append((int(x[0]), int(x[1])))

info = list_of_items.pop(0)
capacity = info[0]
total_items = info[1]

evaluation_list = [(list_of_items[i][1] / list_of_items[i][0], i) for i in range(len(list_of_items))]

# Check for best sorting algorithm
evaluation_list.sort(reverse=True)

decision_list = [0 for _ in range(total_items)]
knapsack = []
value = 0
minimum_item = min(list_of_items)

for item in evaluation_list:
    if list_of_items[item[1]][0] <= capacity:
        knapsack.append(list_of_items[item[1]])
        capacity -= list_of_items[item[1]][0]
        value += list_of_items[item[1]][1]
        decision_list[item[1]] = 1
        print(f"item: {list_of_items[item[1]]}, Capacity: {capacity}")

    if capacity < minimum_item[0]:
        print("\nNo other item can fit.")
        break

print("\n")
print(f"Total value: {value}")
end_time = perf_counter()
t = end_time - start_time
print(f"Execution time is: {t*1000:.4f} ms")

# with open("Solutions/pr6_10000_solutions", "a") as f:
#     f.write("\n" + str(decision_list))
