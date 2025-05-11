from time import perf_counter
import csv
import os


# Ensure output directory exists
os.makedirs("solutions", exist_ok=True)
dataset_name = "pr2_50"

solution_dir = "solutions/"+dataset_name+"_greedy.csv" # Updated to CSV
dataset_dir = "datasets/"+dataset_name+".csv"  

list_of_items = []

with open(dataset_dir, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        list_of_items.append((int(row[0]), int(row[1])))

start_time = perf_counter()

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

# with open("solutions/pr6_10000_solutions", "a") as f:
#     f.write("\n" + str(decision_list))

# Save decision list to a CSV file
with open(solution_dir, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(decision_list)  # One row with all decisions