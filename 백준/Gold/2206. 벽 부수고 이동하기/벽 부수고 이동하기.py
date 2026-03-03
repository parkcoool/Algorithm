import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
# 문자열을 하나씩 쪼개서 정수 리스트로 변환
grid = [list(map(int, list(input().strip()))) for _ in range(N)]

# visited[broken][y][x]
# broken: 0 (안 부숨), 1 (부숨)
# 공간을 [2][N][M]으로 잡는 것이 캐시 메모리 접근에 약간 더 유리합니다.
visited = [[[0] * M for _ in range(N)] for _ in range(2)]

def bfs():
    # 큐에는 (y, x, 벽 부숨 여부) 를 넣습니다.
    # 0: 안 부숨, 1: 부숨
    q = deque([(0, 0, 0)])
    visited[0][0][0] = 1 # 시작점 방문 처리 (거리는 1부터 시작)

    while q:
        y, x, broken = q.popleft()

        # 목적지 도착 시 즉시 거리 반환 (BFS이므로 가장 먼저 도착한 게 최단거리)
        if y == N - 1 and x == M - 1:
            return visited[broken][y][x]

        for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            ny, nx = y + dy, x + dx

            if 0 <= ny < N and 0 <= nx < M:
                # 1. 다음 칸이 벽인데, 내가 아직 벽을 한 번도 안 부쉈다면?
                if grid[ny][nx] == 1 and broken == 0:
                    if visited[1][ny][nx] == 0: # 부순 세계선에서 방문한 적 없다면
                        visited[1][ny][nx] = visited[0][y][x] + 1
                        q.append((ny, nx, 1)) # 상태를 1(부숨)로 바꿔서 큐에 넣음
                
                # 2. 다음 칸이 빈 칸이라면? (내가 벽을 부쉈든 안 부쉈든 이동 가능)
                elif grid[ny][nx] == 0:
                    if visited[broken][ny][nx] == 0: # 내 현재 세계선에서 방문한 적 없다면
                        visited[broken][ny][nx] = visited[broken][y][x] + 1
                        q.append((ny, nx, broken)) # 상태 유지한 채로 큐에 넣음
                        
    return -1

print(bfs())