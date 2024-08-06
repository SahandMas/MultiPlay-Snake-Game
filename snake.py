import consts

class Snake:
    dx = {'UP': 0, 'DOWN': 0, 'LEFT': -1, 'RIGHT': 1}
    dy = {'UP': -1, 'DOWN': 1, 'LEFT': 0, 'RIGHT': 0}

    def __init__(self, keys, game, pos, color, direction):
        self.keys = keys
        self.cells = [pos]
        self.game = game
        self.game.add_snake(self)
        self.color = color
        self.direction = direction
        game.get_cell(pos).set_color(color)

    def get_head(self):
        return self.cells[-1]

    def val(self, x):
        if x < 0:
            x += self.game.size

        if x >= self.game.size:
            x -= self.game.size

        return x

    def handle(self, keys):
        for key in keys:
            if key in self.keys:
                new_direction = self.keys[key]
                if (new_direction == 'UP' and self.direction != 'DOWN') or \
                   (new_direction == 'DOWN' and self.direction != 'UP') or \
                   (new_direction == 'LEFT' and self.direction != 'RIGHT') or \
                   (new_direction == 'RIGHT' and self.direction != 'LEFT'):
                    self.direction = new_direction
                    break

    def next_move(self):
        head_x, head_y = self.get_head()
        new_x = self.val(head_x + self.dx[self.direction])
        new_y = self.val(head_y + self.dy[self.direction])
        new_pos = (new_x, new_y)

        cell = self.game.get_cell(new_pos)
        if cell.color != consts.back_color and cell.color != consts.fruit_color:
            self.game.kill(self)
        else:
            if cell.color == consts.fruit_color:
                self.cells.append(new_pos)
                cell.set_color(self.color)
            else:
                tail = self.cells.pop(0)
                self.game.get_cell(tail).set_color(consts.back_color)
                self.cells.append(new_pos)
                cell.set_color(self.color)
