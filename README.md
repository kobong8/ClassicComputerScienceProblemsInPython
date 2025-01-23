# 고전 컴퓨터 알고리즘 인 파이썬 (Classic Computer Science Problems in Python)

- 모든 자료의 내용은 "[고전 컴퓨터 알고리즘 인 파이썬; 데이비드 코펙 지음, 최길우 옮김; 한빛미디어 (2019)](https://www.hanbit.co.kr/store/books/look.php?p_code=B2018898164)" 상의 내용을 기반으로 작성되었습니다.

- 저자의 GitHub 링크: [davecom/ClassicComputerScienceProblemsInPython](https://github.com/davecom/ClassicComputerScienceProblemsInPython)

## 3장 제약 충족 문제

### 3.8 연습문제

3. 제약 충족 문제 해결 프레임워크를 이용하여 스도쿠 문제를 해결할 수 있는 프로그램을 작성하라.

- 스도쿠 문제의 풀이 (LocationSearchConstraint 클래스)
- 스도쿠 보드 시각화 (draw_sudoku_board 함수)
- 코드: [sudoku.py](https://github.com/kobong8/ClassicComputerScienceProblemsInPython/blob/main/Chapter03/2022/sudoku.py)

![sodoku](https://user-images.githubusercontent.com/83524779/163752718-ad870b69-a73a-4b7d-a4de-bb496ced1a38.png)

## 4장 그래프 문제

### 4.4 네트워크 구축 비용 최소화

#### 4.4.2 최소 신장 트리 찾기

- Jarnik's algorithm (Prim's algorithm)을 활용하여 최소 신장 트리 (minimum spanning tree, mst) 구축
- 네트워크 구축 비용 최소화 과정에서 단계별 우선순위 큐 (priority queue)의 시각화 (visualize_priority_queue 및 show_result 함수)
- show_result 개발자: [keizikang](https://keizikang.github.io/)
- 코드: [mst.py](https://github.com/kobong8/ClassicComputerScienceProblemsInPython/blob/main/Chapter04/2022/mst.py)

![msa_mst](https://user-images.githubusercontent.com/83524779/163836165-fcd966fe-ff7e-42c9-93ab-0e1dbc472c3d.gif)

