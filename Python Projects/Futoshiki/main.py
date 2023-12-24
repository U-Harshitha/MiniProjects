class Futoshiki:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.constraints = []

    def set_fixed_value(self, row, col, value):
        self.grid[row][col] = value

    def set_inequality_constraint(self, row1, col1, row2, col2, symbol):
        self.constraints.append(((row1, col1), (row2, col2), symbol))

    def check_num_in_row(self, row, number):
        if number in self.grid[row]:
            return False
        return True

    def check_num_in_column(self, col, number):
        for row in range(self.size):
            if self.grid[row][col] == number:
                return False
        return True

    def check_inequality(self, row, col, number): 
        for constraint in self.constraints:
            (row1, col1), (row2, col2), symbol = constraint
            value1 = self.grid[row1][col1]
            value2 = self.grid[row2][col2]
            if value1 != 0 and value2 != 0:
                if (symbol == ">" and value1 <= value2) or (symbol == "<" and value1 >= value2):
                    return False
        return True

    def is_valid_number(self, row, col, number):
        return (self.check_num_in_row(row, number) and self.check_num_in_column(col, number) and self.check_inequality(row, col, number))

    def solve(self):
        return self.solve_recursive(0, 0)

    def solve_recursive(self, row, col):
        if row == self.size:
            return True

        next_col = (col + 1) % self.size
        next_row = row + 1 if next_col == 0 else row

        if self.grid[row][col] != 0:
            return self.solve_recursive(next_row, next_col)

        for number in range(1, self.size + 1):
            if self.is_valid_number(row, col, number):
                self.grid[row][col] = number

                if self.solve_recursive(next_row, next_col):
                    return True

                self.grid[row][col] = 0

        return False

    def display_grid(self):
        print("\n".join(map(str, self.grid)))


ob = Futoshiki(4)
ob.set_fixed_value(0, 3, 3)
ob.set_inequality_constraint(1, 1, 1, 2, ">")
ob.set_inequality_constraint(1, 2, 2, 2, ">")
ob.set_inequality_constraint(1, 3, 2, 3, ">")
ob.set_inequality_constraint(2, 0, 2, 1, "<")
ob.display_grid()
if ob.solve():
    print("\nFinal output:")
    ob.display_grid()
else:
    print("No")
