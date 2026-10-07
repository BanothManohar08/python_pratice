def min(marks):
    min_marks = marks[0]
    for mark in marks:
        if mark < min_marks:
            min_marks = mark
    return min_marks
def max(marks):
    max_marks = marks[0]
    for mark in marks:
        if mark > max_marks:
            max_marks = mark
    return max_marks
def avg(marks):
    total = 0
    for mark in marks:
        total += mark
    average = total / len(marks)
    return average
marks = [85, 90, 78, 92, 88]
print( min(marks))
print(max(marks)) 
print(avg(marks))
