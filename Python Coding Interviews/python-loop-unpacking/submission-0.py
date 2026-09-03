from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    maximum = 0
    top_student = ""
    for name, score in scores:
        if score > maximum:
            maximum = score
            top_student = name
    return top_student


# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
