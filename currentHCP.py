import json
from utils import scores_to_use, plotHcp
with open('differentials.json', 'r') as file:
    data = json.load(file)


if len(data) < 3:
    print("Not enough scores to calculate HCP")
    exit()


print(f"Calculating HCP based on {len(data)} rounds")
print()
# Sort data by date in descending order (newest first)
sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    
# Limit to most recent 20 scores if more than 20 exist
limited_data = sorted_data[:20]
    
scoresToUse, adjustment = scores_to_use(len(limited_data))

print(f"Using lowest {scoresToUse} rounds from most recent {len(sorted_data)} rounds.")
if adjustment != 0:
    print(f"Adjusting by {adjustment} due to insufficient round scores.")
print()

sorted_diffs = sorted(limited_data, key=lambda x: x['differential'])

used_diffs = sorted_diffs[:scoresToUse]

hcp = (sum(d["differential"] for d in used_diffs) / len(used_diffs)) + adjustment

print()
print()
print("--------------------------")
print(f"Current HCP: {hcp}")
print("--------------------------")

plotHcp(data)
