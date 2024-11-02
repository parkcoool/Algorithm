N, r, c = map(int, input().split())


def sol(row, col, start, size):
  if size == 1:
    if row == r and col == c:
      print(start)
      exit()
    else:
      return

  half = int(size / 2)

  if r < row + half and c < col + half:
    sol(row, col, start, half)
  elif r < row + half and c >= col + half:
    sol(row, col + half, start + int(size**2 / 4), half)
  elif r >= row + half and c < col + half:
    sol(row + half, col, start + int(size**2 / 2), half)
  else:
    sol(row + half, col + half, start + int(size**2 * 3 / 4), half)

sol(0, 0, 0, 2**N)
