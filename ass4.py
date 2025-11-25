import csv
import math

# -------------------------------
# FUNCTION: Load CSV (removes BOM)
# -------------------------------
def load_csv(filename):
    print(f"Loading Lipstick file: {filename}")
    
    with open(filename, "r", encoding="utf-8-sig") as f:   # FIX for BOM (\ufeff)
        reader = csv.reader(f)
        data = list(reader)

    header = data[0]
    rows = data[1:]

    return header, rows


# ------------------------------
# FUNCTION: Entropy calculation
# ------------------------------
def entropy(values):
    total = len(values)
    value_counts = {}

    for v in values:
        value_counts[v] = value_counts.get(v, 0) + 1

    ent = 0
    for count in value_counts.values():
        p = count / total
        ent -= p * math.log(p, 2)

    return ent


# ----------------------------------------------
# FUNCTION: Information Gain for an attribute
# ----------------------------------------------
def information_gain(dataset, attr_index, target_index):
    total_rows = len(dataset)
    target_values = [row[target_index] for row in dataset]

    base_entropy = entropy(target_values)

    partitions = {}
    for row in dataset:
        key = row[attr_index]           # value of attribute
        partitions.setdefault(key, []).append(row)

    weighted_entropy = 0
    for subset in partitions.values():
        subset_prob = len(subset) / total_rows
        subset_entropy = entropy([row[target_index] for row in subset])
        weighted_entropy += subset_prob * subset_entropy

    return base_entropy - weighted_entropy


# ------------------------
# MAIN PROGRAM
# ------------------------
if __name__ == "__main__":
    
    filename = r"F:\TY SUBMISSION\DSML\DSML practical all assignment\Lipstick.csv"
    header, rows = load_csv(filename)

    # Remove BOM exactly from first column
    header = [h.replace("\ufeff", "") for h in header]

    target_attribute = "Buys"
    target_index = header.index(target_attribute)

    print("\nAttributes considered for root:")
    print(header[:-1])  # Exclude target variable

    # Entropy of target
    base_ent = entropy([row[target_index] for row in rows])
    print(f"\nEntropy({target_attribute}) = {base_ent:.4f}\n")

    # Compute information gain for each attribute
    gains = {}
    for attr in header:
        if attr == target_attribute:
            continue

        attr_index = header.index(attr)
        gain = information_gain(rows, attr_index, target_index)

        print(f"Information Gain for {attr}: {gain:.4f}")
        gains[attr] = gain

    print("\n------------------------------------------")
    root = max(gains, key=gains.get)
    print(f"ROOT NODE of the Decision Tree = {root}")
    print("------------------------------------------")
