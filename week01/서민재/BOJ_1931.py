# 1931 회의실 배정
# 사용할 수 있는 최대 회의 개수
# Greedy
# 끝나는 시간 기준으로 정렬해야 이후 회의 시간을 고르는 데 유리함

N = int(input())
time = [list(map(int, input().split())) for _ in range(N)]
time.sort(key=lambda x: (x[1], x[0]))

answer = 0
end = 0

for i in range(N):
    if end > time[i][0]:
        continue

    end = time[i][1]
    answer += 1

print(answer)
