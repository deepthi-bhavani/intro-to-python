with open("text.txt",encoding="utf-8") as file:
    text = file.read()
    text = text.lower()

for p in ".,!?":
    text = text.replace(p, "")
words = text.split()
counts = {}

for word in words:
    if word not in counts:
        counts[word] = 0
        counts[word] += 1

with open("report.txt", "w", encoding="utf-8") as file:
    file.write(f"Words: {len(words)}\n")
    file.write(f"Unique: {len(counts)}\n")
    for word in sorted(counts):
        file.write(f"{word} {counts[word]}\n")
print("Report saved to report.txt")