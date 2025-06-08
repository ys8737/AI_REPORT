"""
14주차 AI 개발 실무 과제 – 레벤슈타인 거리 기반 챗봇 (콘솔 버전)

VARIABLE NAMING CONVENTIONS
---------------------------
len1, len2 : 문자열 길이 (성능·가독성)

dp         : dynamic‑programming 테이블
QUESTIONS  : 학습 질문 리스트
ANSWERS    : 학습 답변 리스트 
user_input : 사용자 질문

distances  : 레벤슈타인 거리 리스트
best_idx   : 최소 거리 인덱스
"""

import pandas as pd
from typing import List, Tuple

# 1. 레벤슈타인 거리 계산 함수

def levenshtein(s1: str, s2: str) -> int:
    """두 문자열 간 레벤슈타인(편집) 거리 계산"""
    len1, len2 = len(s1), len(s2)
    dp: List[List[int]] = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    # 첫 행·열 초기화 (빈 문자열과의 거리)
    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    # 테이블 채우기
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,        # 삭제
                dp[i][j - 1] + 1,        # 삽입
                dp[i - 1][j - 1] + cost  # 교체
            )
    return dp[len1][len2]

# 2. 데이터 로드 함수

def load_data(filepath: str) -> Tuple[List[str], List[str]]:
    """CSV 파일을 읽어 (질문, 답변) 리스트 반환"""
    df = pd.read_csv(filepath)
    questions = df['Q'].astype(str).tolist()
    answers   = df['A'].astype(str).tolist()
    return questions, answers

# 3. 챗봇 응답 함수

def get_best_answer(user_input: str, questions: List[str], answers: List[str]) -> str:
    """user_input과 가장 유사한 질문의 답변 반환"""
    distances = [levenshtein(user_input, q) for q in questions]
    best_idx  = distances.index(min(distances))
    return answers[best_idx]

# 4. 메인 루프 (콘솔 I/O)

def main() -> None:
    try:
        QUESTIONS, ANSWERS = load_data('ChatbotData.csv')
    except FileNotFoundError:
        print('[Error] ChatbotData.csv 파일을 찾을 수 없습니다. 같은 폴더에 두세요.')
        return

    print('===== 레벤슈타인 거리 기반 챗봇 =====')
    print('"종료" 또는 "exit" 입력 시 챗봇을 종료합니다.\n')

    while True:
        user_input = input('You: ').strip()
        if not user_input:
            continue
        if user_input.lower() in {'종료', 'exit', 'quit'}:
            print('Chatbot: 이용해 주셔서 감사합니다.안녕히 가세요.')
            break

        response = get_best_answer(user_input, QUESTIONS, ANSWERS)
        print(f'Chatbot: {response}')

# 5. 스크립트 직접 실행 시 main() 호출

if __name__ == '__main__':
    main()