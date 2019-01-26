def word_in_a_grid(grid, word):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if helper(grid, i, j, 0, word):
                return True
    return False


def helper(word_grid, row, column, index, word):
    if index == len(word):
        return True
    if row < 0 or column < 0 or row >= len(word_grid) or column >= len(word_grid[0]):
        return False
    if word_grid[row][column] != word[index]:
        return False
    return helper(word_grid, row + 1, column, index + 1, word) or \
           helper(word_grid, row - 1, column, index + 1, word) or \
           helper(word_grid, row, column + 1, index + 1, word) or \
           helper(word_grid, row, column - 1, index + 1, word)


grid = ["axmy", "brdf", "xeet", "rass"]
print word_in_a_grid(grid, "abxr")
