import csv
from random import seed, randrange
from datetime import datetime
from time import perf_counter
import os


# Ensure output directory exists
os.makedirs("solutions", exist_ok=True)
dataset_name = "pr2_50"

solution_dir = "solutions/"+dataset_name+"_random.csv" # Updated to CSV
dataset_dir = "datasets/"+dataset_name+".csv"  

list_of_items = []

with open(dataset_dir, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        list_of_items.append((int(row[0]), int(row[1])))

start_time = perf_counter()
seed(int(datetime.now().timestamp()))

info = list_of_items.pop(0)
capacity = info[0]
total_items = info[1]
decision_list = [0 for _ in range(total_items)]
indexes = [i for i in range(len(list_of_items))]
knapsack = []
minimum_item = min(list_of_items)
value = 0

while True:
    random_index = randrange(len(indexes))
    index_for_item = indexes[random_index]
    indexes.pop(random_index)
    random_item = list_of_items[index_for_item]

    if random_item[0] <= capacity:
        knapsack.append(random_item)
        capacity -= random_item[0]
        value += random_item[1]
        decision_list[index_for_item] = 1
        print(f"item: {random_item}, Capacity: {capacity}")

    if capacity < minimum_item[0] or len(indexes) == 0:
        print("\nNo other item can fit.")
        break

print(f"Total value: {value}")
end_time = perf_counter()
t = end_time - start_time
print(f"Execution time is: {t*1000:.4f} ms")


# Save decision list to a CSV file
with open(solution_dir, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(decision_list)  # One row with all decisions