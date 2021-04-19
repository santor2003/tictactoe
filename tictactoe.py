class InvalidMove(Exception):
  pass

class GameTied(Exception):
  pass

class Game:
  def __init__(self, size=3):
    
    self.size = size
    self.board = []
    self.cells = {}
    cnt = 0
    for y in list(range(size)):
      row = []
      for x in list(range(size)):
        cnt += 1
        row.append('')
        self.cells[cnt] = [y, x]
      self.board.append(row)

  def _check_array(self, array, symbol):

    for i in array:
      if i != symbol:
        return False
    return True

  def valid_moves(self):
 
    return self.cells.keys()

  def make_move(self, move, symbol):
    
    
    try:
      move = int(move)
    except:
      raise InvalidMove
    else:
      if move in self.valid_moves():
        y, x = self.cells[move]
        self.board[y][x] = symbol
        del self.cells[move]
      else:
        raise InvalidMove
      
  def check_winner(self, symbol):

    b = self.board
    sections = [] # An array of sections to check
    diag1 = []
    diag2 = []

    for y in list(range(self.size)):
      sections.append(b[y]) # Row y
      sections.append([r[y] for r in b]) # Col y
      for x in list(range(self.size)):
        if y == x:
          diag1.append(b[y][x])
        if y == (self.size - x - 1):
          diag2.append(b[y][x])

    sections.append(diag1)
    sections.append(diag2)
    for section in sections:
      if self._check_array(section, symbol):
        return True

    if len(self.valid_moves()) == 0:
      raise GameTied

    return False