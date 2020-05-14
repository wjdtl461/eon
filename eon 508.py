n_input = int(input("작업 수 : "))
j_input = int(input("작업 번호 : "))
work_jinzza = list(map(int,input("우선순위 : ").split()))
work_gazza = list(range(len(work_jinzza)))
min = 0

while True:
    work_max = max(work_jinzza)
    if (work_max == work_jinzza[0]):
        min += 1
        if work_gazza[0] == j_input:
            break
        work_jinzza.pop(0)
        work_gazza.pop(0)
    else:
        work_gazza.append(work_gazza.pop(0))
        work_jinzza.append(work_jinzza.pop(0))

print(min, "분")
