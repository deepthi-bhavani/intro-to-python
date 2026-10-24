
answers=["b", "a", "d", "c"]
correct=["b", "c", "d", "c"]
score = 0
for a,c in zip(answers, correct):
    if a == c:
        score = score + 1
print("Score:", score, "/", len(correct))
