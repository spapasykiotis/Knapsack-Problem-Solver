from time import perf_counter
dataset = "datasets\pr3_200.txt"    # Select Dataset

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
    
    # with open("Solutions/pr6_10000_solutions", "a") as f:
    #     f.write("\n" + str(decision_list))


main()
