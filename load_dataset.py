from pathlib import Path
#if in python someone wants to work with file and system he needs this

#creating a variable to store our data or represent
#as python is oops language

dataset_path=Path("data/cat-facts.txt")

with dataset_path.open("r",encoding="utf-8") as file:
    dataset=file.readlines()

print(f"Loaded {len(dataset)} entries")
print("First 3 entries:")

for fact in dataset[:3]:
    print(fact.strip())
