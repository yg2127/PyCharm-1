name = input("학생의 이름을 입력하세요: ")
score = float(input("학생의 성적을 입력하세요: "))
print(f"학생의 이름: {name}")
print(f"학생의 성적: {score:.2f}")
is_graduated = input("학생이 졸업했는지 여부 (yes/no)를 입력하세요: ").lower() == 'yes'

if is_graduated:
    print("졸업생")
else:
    print("재학생")
subjects = ["Math", "Science", "History", "English", "Art"]
print("2번째, 3번째, 4번째 과목:", subjects[1:4])
student_info = {
    "name": name,
    "score": score,
    "is_graduated": is_graduated
}

print("학생 정보:", student_info)
print("학생 이름:", student_info["name"])

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"학생의 학점: {grade}")
if is_graduated:
    print("졸업 후 학점 계산")
else:
    print("현재 성적 유지")

for idx, subject in enumerate(subjects, start=1):
    print(f"{idx}. {subject}")

while True:
    score = float(input("학생의 성적을 입력하세요 (종료하려면 0 이하 입력): "))
    if score <= 0:
        break
    if score >= 80:
        print(f"{score:.2f}점: 합격")
def print_student_score(name, score):
    print(f"학생 이름: {name}, 성적: {score:.2f}")

print_student_score(name, score)

def get_max_min_scores(scores):
    max_score = max(scores)
    min_score = min(scores)
    return max_score, min_score

scores = [85, 92, 78, 88, 94]
max_score, min_score = get_max_min_scores(scores)
print(f"최고 성적: {max_score}, 최저 성적: {min_score}")