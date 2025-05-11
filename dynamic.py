from time import perf_counter
import csv
import os


# Ensure output directory exists
os.makedirs("solutions", exist_ok=True)
dataset_name = "pr2_50"

solution_dir = "solutions/"+dataset_name+"_dynamic.csv" # Updated to CSV
dataset_dir = "datasets/"+dataset_name+".csv"  

def knapsack(k, weights, values, n, solution):
    array = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(k + 1):
            if i == 0 or w == 0:
                array[i][w] = 0
            elif weights[i - 1] <= w:
                array[i][w] = max(values[i - 1] + array[i - 1][w - weights[i - 1]], array[i - 1][w])
            else:
                array[i][w] = array[i - 1][w]

    #  Solution
    i = n
    j = k
    while i != 0:
        if array[i][j] == array[i - 1][j]:
            i -= 1
        else:
            solution[i - 1] = 1
            j -= weights[i - 1]
            i -= 1

    # print(array)
    return array[n][k]


def main():

    list_of_items = []

    with open(dataset_dir, newline='', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            list_of_items.append((int(row[0]), int(row[1])))

    start_time = perf_counter()

    info = list_of_items.pop(0)
    capacity = info[0]
    total_items = info[1]
    decision_list = [0 for _ in range(total_items)]
    list_of_values = []
    list_of_weights = []

    for item in list_of_items:
        list_of_weights.append(item[0])
        list_of_values.append(item[1])

    bug = knapsack(capacity, list_of_weights, list_of_values, total_items, decision_list)

    for index in range(len(decision_list)):
        if decision_list[index] == 1:
            print(f"item: {list_of_items[index]}")

    print(f"\nTotal value: {bug}")
    end_time = perf_counter()
    t = end_time - start_time
    print(f"Execution time is: {t*1000:.4f} ms")
    
    # Save decision list to a CSV file
    with open(solution_dir, "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerow(decision_list)  # One row with all decisions


main()
