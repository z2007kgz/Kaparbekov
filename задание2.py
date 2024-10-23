
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

students_scores = dict(zip(names, scores))
max_score_student = max(students_scores, key=students_scores.get)

print("Словарь студентов и их оценок:", students_scores)
print("Студент с максимальной оценкой:", max_score_student, "с оценкой", students_scores[max_score_student])
