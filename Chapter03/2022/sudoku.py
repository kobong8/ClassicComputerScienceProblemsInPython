# Exercise 3.8 - 3
# title   : Sudoku
# version : 2022.03.20.
# author  : kobong
import time
import random
import copy
from typing import NamedTuple, List, Dict, Tuple, Optional
from csp import CSP, Constraint

Sudoku = List[List[int]]


class SudokuLocation(NamedTuple):
    row: int
    column: int


def sudoku_generator(sudoku: Sudoku, num_unknown: int) -> Sudoku:
    random.seed(42)
    new_sudoku = copy.deepcopy(sudoku)
    row_list = [random.randint(0, 8) for _ in range(num_unknown)]
    col_list = [random.randint(0, 8) for _ in range(num_unknown)]
    for row, col in zip(row_list, col_list):
        new_sudoku[row][col] = 0
    return new_sudoku


def display_sudoku(sudoku: Sudoku) -> None:
    for row in range(0, 9):
        for col in range(0, 9):
            print(f"{sudoku[row][col]}", end="")
        print()


def number_of_variables(sudoku: Sudoku) -> Dict[int, int]:
    variable: Dict[int, int] = {idx: 0 for idx in range(1, 10)}
    height: int = len(sudoku)
    width: int = len(sudoku[0])

    for row in range(height):
        for col in range(width):
            for idx in range(1, 10):
                if sudoku[row][col] == idx:
                    variable[idx] += 1
                else:
                    continue

    for idx in range(1, 10):
        variable[idx] = 9 - variable[idx]

    return variable


def generate_domain(sudoku: Sudoku, number: int) -> List[List[SudokuLocation]]:
    domain: List[List[SudokuLocation]] = []
    height: int = len(sudoku)
    width: int = len(sudoku[0])

    for row in range(height):
        for col in range(width):
            if sudoku[row][col] == 0:
                rs = row - row % 3
                re = rs + 3
                cs = col - col % 3
                ce = cs + 3               

                if ((number in sudoku[row]) or 
                    (number in [i[col] for i in sudoku]) or
                    (number in [sudoku[i][j] for i in range(rs, re) for j in range(cs, ce)])):
                    continue
                else:
                    domain.append([SudokuLocation(row, col)])
    return domain


def sudoku_solution(original_sudoku: Sudoku,
                    sudoku: Sudoku, numbers: List[Tuple],
                    solution: Dict[Tuple, List[SudokuLocation]]) -> Sudoku:
    for number in numbers:
        row = (solution[number])[0].row
        col = (solution[number])[0].column
        sudoku[row][col] = number[0]

    diff_sudoku = [[100 for _ in range(0, 9)] for _ in range(0, 9)]
    for row in range(0, 9):
        for col in range(0, 9):
            diff_sudoku[row][col] = original_sudoku[row][col] - sudoku[row][col]
    return sudoku, diff_sudoku


class LocationSearchConstraint(Constraint[Tuple, List[SudokuLocation]]):
    def __init__(self, numbers: List[Tuple]) -> None:
        super().__init__(numbers)
        self.numbers: List[Tuple] = numbers

    def generate_constraint(self, rpos: int, cpos: int) -> Tuple[List[List[int]]]:
        skl_row: List[SudokuLocation] = []
        skl_col: List[SudokuLocation] = []
        skl_rec: List[SudokuLocation] = []

        for i in range(0, 9):
            skl_row.append(SudokuLocation(rpos, i))
            skl_col.append(SudokuLocation(i, cpos))

        rs = rpos - rpos % 3
        re = rs + 3
        cs = cpos - cpos % 3
        ce = cs + 3

        for i in range(rs, re):
            for j in range(cs, ce):
                skl_rec.append(SudokuLocation(i, j))

        return skl_row, skl_col, skl_rec

    def satisfied(self, assignment: Dict[Tuple, List[SudokuLocation]]) -> bool:
        for key1 in assignment.keys():
            rpos = assignment[key1][0].row
            cpos = assignment[key1][0].column

            skl_row, skl_col, skl_rec = self.generate_constraint(rpos, cpos)

            for key2 in assignment.keys():
                if key1 != key2:
                    if assignment[key1][0] == assignment[key2][0]:
                        return False

                    if key1[0] == key2[0]:
                        if ((assignment[key2][0] in skl_row) or 
                            (assignment[key2][0] in skl_col) or
                            (assignment[key2][0] in skl_rec)):
                            return False

        return True


if __name__ == "__main__":
    t_start = time.time()
    # unknown: 51
    # unsolved_sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
    #                    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    #                    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    #                    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    #                    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    #                    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    #                    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    #                    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    #                    [0, 0, 0, 0, 8, 0, 0, 7, 9]]
   
    # test
    original_sudoku = [[8, 3, 9, 6, 5, 7, 2, 1, 4],
                       [6, 7, 2, 9, 4, 1, 5, 8, 3],
                       [1, 5, 4, 8, 3, 2, 9, 6, 7],
                       [5, 4, 1, 2, 8, 3, 7, 9, 6],
                       [2, 8, 7, 4, 9, 6, 3, 5, 1],
                       [9, 6, 3, 7, 1, 5, 4, 2, 8],
                       [7, 1, 8, 3, 2, 9, 6, 4, 5],
                       [3, 2, 5, 1, 6, 4, 8, 7, 9],
                       [4, 9, 6, 5, 7, 8, 1, 3, 2]]

    number_unknown = 34
    # random.seed(42) / 34 > 28 / 35 > 30 (X)
    unsolved_sudoku = sudoku_generator(original_sudoku, number_unknown)
    
    print(f"original sudoku")
    display_sudoku(original_sudoku)
    print()    
    
    print("sudoku problem")
    display_sudoku(unsolved_sudoku)
    print()

    novs: Dict[int, int] = number_of_variables(unsolved_sudoku)
    locations: Dict[Tuple, List[List[SudokuLocation]]] = {}

    numbers: List[Tuple] = []
    for i in range(1, 10):
        for j in range(novs[i]):
            numbers.append((i, j))

    print(f"unknown: {len(numbers)}")
    for number in numbers:
        locations[number] = generate_domain(unsolved_sudoku, number[0])

    print(f"start!")
    csp: CSP[Tuple, List[SudokuLocation]] = CSP(numbers, locations)
    csp.add_constraint(LocationSearchConstraint(numbers))
    solution: Optional[Dict[Tuple, List[SudokuLocation]]] = csp.backtracking_search()

    if solution is None:
        print("답을 찾을 수 없습니다.")
    else:
        print("solution sudoku")
        solved_sudoku, diff_sudoku = sudoku_solution(original_sudoku, unsolved_sudoku, numbers, solution)
        display_sudoku(solved_sudoku)
        print()
        print("diff. sudoku")
        display_sudoku(diff_sudoku)

    print(f"elapsed time: {time.time() - t_start}")
