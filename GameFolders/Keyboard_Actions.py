import Figure_Actions
import Gameplay_Actions


def movement(figure, pg, event):
    import Gameplay_Actions
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_LEFT:
            Gameplay_Actions.clear_board()
            if not check_collision_on_sides(figure, -1):
                figure.x_left -= 1
                figure.x_right -= 1
            Gameplay_Actions.put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))

        elif event.key == pg.K_RIGHT:
            Gameplay_Actions.clear_board()
            if not check_collision_on_sides(figure, 1):
                figure.x_left += 1
                figure.x_right += 1
            Gameplay_Actions.put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))

        elif event.key == pg.K_UP:
            old_structure = [row[:] for row in figure.structure]
            old_x_left = figure.x_left
            old_x_right = figure.x_right
            old_y_top = figure.y_top
            old_y_bot = figure.y_bot
            Figure_Actions.rotate_figure(figure)
            Gameplay_Actions.clear_board()
            if check_collision_on_sides(figure, 0) or check_collision_on_bottom(figure):
                Figure_Actions.undo_rotate_figure(figure, old_structure)
                figure.x_left = old_x_left
                figure.x_right = old_x_right
                figure.y_top = old_y_top
                figure.y_bot = old_y_bot
            Gameplay_Actions.put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))

        elif event.key == pg.K_DOWN:
            Gameplay_Actions.clear_board()
            if not check_collision_on_bottom(figure):
                figure.y_top += 1
                figure.y_bot += 1
            Gameplay_Actions.put_structure_on_board(figure, (figure.x_left, figure.x_right, figure.y_top, figure.y_bot))

def check_collision_on_sides(figure, direction):
    for fig_y in range(figure.height):
        for fx in range(figure.width):
            if fig_y < len(figure.structure) and fx < len(figure.structure[fig_y]) and figure.structure[fig_y][fx] == 1:
                board_x = figure.x_left + fx + direction
                board_y = figure.y_top + fig_y
                if board_x < 0:
                    return True
                if board_x >= len(Gameplay_Actions.game_board[0]):
                    return True
                val = Gameplay_Actions.game_board[board_y][board_x]
                if val != 0 and val != 1:
                    return True
    return False


def check_collision_on_bottom(figure):
    for fig_x in range(figure.width):
        for fy in range(figure.height - 1, -1, -1):
            if fig_x < len(figure.structure[fy]) and figure.structure[fy][fig_x] == 1:
                board_x = figure.x_left + fig_x
                below_y = figure.y_top + fy + 1
                if below_y >= len(Gameplay_Actions.game_board) or (Gameplay_Actions.game_board[below_y][board_x] != 0 and Gameplay_Actions.game_board[below_y][board_x] != 1):
                    return True
                break
    return False



