import pygame
import math

# 1. pygame 초기화 및 화면 생성
pygame.init()
screen = pygame.display.set_mode((700, 750))

# 2. 코트(배경) Surface 생성
court_surface = pygame.Surface((700, 750))
court_surface.fill((255, 255, 255))  # 흰색 배경

# 농구 코트 그리기 (예시)
pygame.draw.rect(court_surface, (0, 0, 0), (0, 0, 700, 750), 5)  # 코트 테두리
pygame.draw.circle(court_surface, (0, 0, 0), (410, 375), 60, 1)  # 중간 서클
pygame.draw.line(court_surface, (0, 0, 0), (410, 255), (410, 495), 1)  # 중간 서클 수직선
pygame.draw.line(court_surface, (0, 0, 0), (410, 255), (700, 255), 1)  # 박스
pygame.draw.line(court_surface, (0, 0, 0), (410, 495), (700, 495), 1)  # 박스
pygame.draw.line(court_surface, (0, 0, 0), (620, 45), (700, 45), 1)  # 3점 라인 직선
pygame.draw.line(court_surface, (0, 0, 0), (620, 705), (700, 705), 1)  # 3점 라인 직선
pygame.draw.circle(court_surface, (0, 0, 0), (0, 375), 60, 1)  # 센터 서클
pygame.draw.circle(court_surface, (0, 0, 0), (620, 375), 11, 1)  # 골대
pygame.draw.line(court_surface, (0, 0, 0), (640, 325), (640, 425), 1)  # 백판

arc_center = (620, 375)
arc_radius = 330
rect = pygame.Rect(arc_center[0] - arc_radius,arc_center[1] - arc_radius,arc_radius * 2,arc_radius * 2)
pygame.draw.arc(court_surface, (0, 0, 0), rect, math.pi/2, -math.pi/2, 1) # 3점 라인 아크
# 필요에 따라 더 추가

# 3. 메인 루프
import numpy as np
state = np.random.rand(22)  # 10명 선수(x, y) + 공(x, y)

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 4. 코트(배경) Surface를 화면에 blit
    screen.blit(court_surface, (0, 0))

    # 5. 선수와 공을 매 프레임마다 그리기
    for i in range(0, 20, 2):
        x = int(50 + state[i] * 500)
        y = int(50 + state[i+1] * 300)
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 10)  # 선수

    ball_x = int(50 + state[20] * 500)
    ball_y = int(50 + state[21] * 300)
    pygame.draw.circle(screen, (0, 0, 255), (ball_x, ball_y), 8)  # 공

    pygame.display.flip()
    clock.tick(20)

    # 상태 업데이트 (예시: 랜덤 이동)
    state += (np.random.rand(22) - 0.5) * 0.05
    state = np.clip(state, 0, 1)

pygame.quit()
