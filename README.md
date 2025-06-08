> 과목 : AI 개발 실무  
> 주제 : TF‑IDF + Cosine Similarity → **레벤슈타인 거리 기반** 챗봇으로 변경  
> 학습 데이터 : `ChatbotData.csv` (14주차 실습 자료)

1. 파일 구성

| 파일명            | 설명                                      |
| ----------------- | ----------------------------------------- |
| `chatbot_lev.py`  | 레벤슈타인 거리 기반 챗봇 메인 소스 파일   |
| `ChatbotData.csv` | 학습 데이터 (질문 `Q`, 답변 `A` 컬럼)      |
| `README.md`       | 실행 방법·환경·설명                        |

2. 실행 방법

```bash
$ python chatbot_lev.py
```

종료하려면 `종료`, `exit`, `quit` 중 하나를 입력하세요.

3. 코드 설명

모든 함수와 변수에는 세부 주석이 포함되어 있으며, 변수 명명 규칙은 `chatbot_lev.py` 상단 Docstring에 정리했습니다.
