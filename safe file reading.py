scores=[]
try:
    with open("scores.txt", encoding="utf-8") as f:
        for line in f:
            line=line.strip()
            try:
                name,score=line.split(",")
                scores.append(int(score))
            except ValueError:
                print("skipped line:",line)
except FileNotFoundError:
    print("File not found")
if scores:
    print("Average score:",sum(scores)/len(scores))