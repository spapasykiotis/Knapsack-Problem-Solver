from time import perf_counter
dataset = "datasets\pr2_50.txt"    # Select Dataset

class ItemValue:
    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt

    def __lt__(self, other):
        return self.cost < other.cost


class FractionalKnapSack:
    @staticmethod
    def getMaxValue(wt, val, capacity):
        global current_solution
        iVal = []
        for i in range(len(wt)):
            iVal.append(ItemValue(wt[i], val[i], i))

        # sorting items by value
        iVal.sort(reverse=True)

        totalValue = 0
        for i in iVal:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >= 0:
                capacity -= curWt
                totalValue += curVal
                bv = totalValue
            else:
                fraction = capacity / curWt
                totalValue += curVal * fraction
                capacity = int(capacity - (curWt * fraction))
                break

        if bv > current_solution:
            current_solution = bv

        return int(totalValue)


def newEstimation(i, values, weights, check, cap):
    new_values = []
    new_weights = []
    if i == 0:
        new_values += values[1:]
        new_weights += weights[1:]
    else:
        for index in check:
            if index < i:
                new_values.append(values[index])
                new_weights.append(weights[index])

        if i != len(values) - 1:
            new_values += values[i+1:]
            new_weights += weights[i+1:]

    return FractionalKnapSack.getMaxValue(new_weights, new_values, cap)


def createDecisionList(sol):
    decision_list = [0 for _ in range(len(values))]

    best_solution = max(sol)
    # print(best_solution)

    for i in best_solution[1]:
        decision_list[evaluation_list[i][1]] = 1

    print("Items inside the bug: ", decision_list)
    print("Best Value: ", best_solution[0])
    print("Remaining weight:", best_solution[2])


    # with open("Solutions/pr6_10000_solutions", "a") as f:
    #     f.write("\n" + str(decision_list))


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
values = []
weights = []

evaluation_list = [(list_of_items[i][1]/list_of_items[i][0], i) for i in range(len(list_of_items))]

evaluation_list.sort(reverse=True)

# Sorted
for item in evaluation_list:
    weights.append(list_of_items[item[1]][0])
    values.append(list_of_items[item[1]][1])

# for item in list_of_items:
#     weights.append(item[0])
#     values.append(item[1])

# Main
current_solution = 0
upper_bound = FractionalKnapSack.getMaxValue(weights, values, capacity)
queue = [(upper_bound, capacity, 0, 0, [])]
solutions = []
loops = 0

while len(queue) > 0:
    loops +=1
    # Sort the queue
    queue.sort(reverse=True)

    # Pop the first item in the queue
    current_node = queue.pop(0)
    # print("current_node: ", current_node)

    upper_bound = current_node[0]
    remaining_weight = current_node[1]
    total_value = current_node[2]
    id = current_node[3]
    current_check = current_node[4]

    # Children creation
    if current_solution <= upper_bound:
        if total_value < upper_bound:
            left_node = (upper_bound, remaining_weight-weights[id], total_value+values[id], id+1, current_check.copy())     # prev Bfs: current_check
            new_upper_bound = newEstimation(id, values, weights, current_check, capacity)
            right_node = (new_upper_bound, remaining_weight, total_value, id+1, current_check.copy())   # prev Bfs: current_check
            # print("right_node: ", right_node)
            queue.append(right_node)
            if left_node[1] >= 0:
                queue.append(left_node)
                left_node[4].append(id)
                # print("left_node: ", left_node)
        else:
            solutions.append((total_value, current_check.copy(), remaining_weight))


createDecisionList(solutions)
# print(solutions)

end_time = perf_counter()
t = end_time - start_time
print(f"Execution time is: {t*1000:.4f} ms")
print("Total calculation loops:", loops)

