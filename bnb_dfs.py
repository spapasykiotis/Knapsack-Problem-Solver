from time import perf_counter
import csv
import os


# Ensure output directory exists
os.makedirs("solutions", exist_ok=True)
dataset_name = "pr2_50"

solution_dir = "solutions/"+dataset_name+"_bnb_dfs.csv" # Updated to CSV
dataset_dir = "datasets/"+dataset_name+".csv"

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
    # print("All solutions: ", sol)
    # print("Length solutions: ", len(sol))

    for i in best_solution[1]:
        decision_list[evaluation_list[i][1]] = 1

    print("Items inside the bug: ", decision_list)
    print("Best Value: ", best_solution[0])
    print("Remaining weight:", best_solution[2])
    
    return decision_list

list_of_items = []

with open(dataset_dir, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        list_of_items.append((int(row[0]), int(row[1])))

start_time = perf_counter()

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

stack = [(0, capacity, upper_bound, 0)]
check = []
solutions = []
previous_id = -1
path = []
loops = 0

while len(stack) > 0:
    loops +=1
    # Pop the last item in the queue
    current_node = stack.pop(len(stack) - 1)
    # print("current_node: ", current_node)

    total_value = current_node[0]
    remaining_weight = current_node[1]
    upper_bound = current_node[2]
    id = current_node[3]

    # Reset check
    if id <= previous_id:
        for j in range(len(check)):
            if check[j] >= id - 1:
                check.pop(j)

    # Children creation
    if current_solution <= upper_bound:
        if total_value < upper_bound:
            left_node = (total_value+values[id], remaining_weight-weights[id], upper_bound, id+1)
            new_upper_bound = newEstimation(id, values, weights, check, capacity)
            right_node = (total_value, remaining_weight, new_upper_bound, id+1)
            # print("right_node: ", right_node)
            stack.append(right_node)
            if left_node[1] >= 0:
                stack.append(left_node)
                check.append(id)
                # print("left_node: ", left_node)
        else:
            solutions.append((total_value, check.copy(), remaining_weight))


    # Save previous id
    previous_id = id
    # print("")

decision_list = createDecisionList(solutions)

end_time = perf_counter()
t = end_time - start_time
print(f"Execution time is: {t*1000:.4f} ms")
print("Total calculation loops:", loops)

# Save decision list to a CSV file
with open(solution_dir, "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(decision_list)  # One row with all decisions