from itertools import product

# 논리 연산 함수
def implies(a, b):
    return (not a) or b

# 진리표 계산
print(f"{'p':^3} {'q':^3} {'r':^3} {'p∨q':^5} {'~p':^4} {'q∧r':^5} {'~p∨(q∧r)':^13} {'전체 명제':^10}")
print("-" * 55)

results = []

for p, q, r in product([True, False], repeat=3):
    pvq = p or q
    not_p = not p
    q_and_r = q and r
    rhs = not_p or q_and_r
    statement = implies(pvq, rhs)
    results.append(statement)

    # 출력
    print(f"{p!s:^3} {q!s:^3} {r!s:^3} {pvq!s:^5} {not_p!s:^4} {q_and_r!s:^5} {rhs!s:^13} {statement!s:^10}")

# 전체 명제 판단
if all(results):
    print("\n→ 이 명제는 **항진명제**입니다.")
elif not any(results):
    print("\n→ 이 명제는 **모순명제**입니다.")
else:
    print("\n→ 이 명제는 **사견명제**입니다.")