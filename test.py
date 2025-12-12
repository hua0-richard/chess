import tkinter as tk
from PIL import Image, ImageTk

from datetime import datetime

root = tk.Tk()
toolbar_height = 64
root.resizable(False, False)
width = 512
height = 512 + toolbar_height * 2
square_width = 64
root.geometry(f"{width}x{height}")
canvas = tk.Canvas(root, width=width, height=height, bg="black")
canvas.pack()

p2_timer = None

class Piece:
    def __init__(self):
        self.piece_id = None
        self.resource = None
        self.img = None
        self.sprite = None
        self.canvas = None

    def verifyMove(self, new_pos):
        x, y = new_pos
        if not self.active:
            self.active = True
        else:
            self.canvas.coords(self.piece_id, 200, 200)
        print("here")

    def removePiece():
        None

    def drawSelf(self, can, x_pos, y_pos):
        self.canvas = can
        sprite_img = ImageTk.PhotoImage(Image.open(self.resource))
        self.sprite = sprite_img
        self.piece_id = can.create_image(
            x_pos,
            y_pos,
            image=sprite_img,
            anchor="nw"
        )


class King(Piece):
    def __init__(self, side):
        super().__init__()
        self.resource = f"assets/king_{side}.png"


class Queen(Piece):
    def __init__(self, side):
        super().__init__()
        self.resource = f"assets/queen_{side}.png"


class Rook(Piece):
    def __init__(self, side):
        super().__init__()
        self.resource = f"assets/rook_{side}.png"


class Bishop(Piece):
    def __init__(self, side):
        super().__init__()
        self.resource = f"assets/bishop_{side}.png"


class Knight(Piece):
    def __init__(self, side):
        super().__init__()
        self.resource = f"assets/knight_{side}.png"


class Pawn(Piece):
    def __init__(self, side):
        super().__init__()
        self.resource = f"assets/pawn_{side}.png"


class Board:
    def __init__(self, canvas):
        self.canvas = canvas
        self.active_piece = None
        self.instance = None
        self.squares = [[None for r in range(8)] for c in range(8)]
        self.p2_timer = None
        self.p1_timer = None

    def snap():
        None

    def _drawBoard(self):
        for x in range(8):
            for y in range(8):
                if ((x % 2) + y) % 2 == 0:
                    color = "#EEEED2"
                else:
                    color = "#769656"
                board.squares[x][y] = canvas.create_rectangle(x * square_width, y * square_width + toolbar_height, x * square_width +
                                                              square_width, y * square_width + square_width + toolbar_height, fill=color)
                canvas.tag_bind(
                    board.squares[x][y], "<Button-1>", lambda event: self.updateActivePiece(event.x, event.y))

    def _drawToolbar(self):
        canvas.create_rectangle(10, 10, 54, 54, fill="#4D55B5")
        canvas.create_text(64, 10, text="AI", font=("TkFixedFont", 12, "bold"), anchor="nw")

        self.p1_timer = canvas.create_text(64, 54, text=datetime.now().strftime("%H:%M:%S"), font=("TkFixedFont", 12), anchor="sw")


        canvas.create_rectangle(10, 10 + 512 + 64, 54, 512 + 64 + 54, fill="#33BB2B")
        
        canvas.create_text(64, 512 + 64 + 10, text="Player", font=("TkFixedFont", 12, "bold"), anchor="nw")

        self.p2_timer = canvas.create_text(64, 512 + 64 + 54, text=datetime.now().strftime("%H:%M:%S"), font=("TkFixedFont", 12), anchor="sw")

    def _placePieces(self):
        self.instance = [
            [Rook(side="light"), Knight(side="light"), Bishop(side="light"), Queen(side="light"), King(
                side="light"), Bishop(side="light"), Knight(side="light"), Rook(side="light")],
            [Pawn(side="light") for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [Pawn(side="dark") for _ in range(8)],
            [Rook(side="dark"), Knight(side="dark"), Bishop(side="dark"), Queen(side="dark"), King(
                side="dark"), Bishop(side="dark"), Knight(side="dark"), Rook(side="dark")],
        ]

    def _drawPieces(self):
        for x in range(8):
            for y in range(8):
                offset = 11
                if self.instance[x][y] != None:
                    self.instance[x][y].drawSelf(
                        canvas, y * square_width + offset, x * square_width + offset + toolbar_height)
                    pid = self.instance[x][y].piece_id
                    canvas.tag_bind(self.instance[x][y].piece_id, "<Button-1>",
                                    lambda event, pid=pid: self.setActivePiece(pid, event.x, event.y))

    def drawBoard(self):
        self._drawBoard()
        self._drawToolbar()
        self._placePieces()
        self._drawPieces()

    def setActivePiece(self, piece, x, y):
        print("Active Piece Set")
        if self.active_piece and self.active_piece != piece:
            self.canvas.coords(self.active_piece, x - (x %
                               64) + 11, y - (y % 64) + 11)
            self.canvas.delete(piece)
            self.active_piece = None
        else:
            print(piece)
            self.active_piece = piece

    def updateActivePiece(self, x, y):
        if self.active_piece:
            print("Updated Position")
            self.canvas.coords(self.active_piece, x - (x %
                               64) + 11, y - (y % 64) + 11)
            self.active_piece = None
    
def update_time(time_item):
    canvas.itemconfig(time_item, text=datetime.now().strftime("%H:%M:%S"))
    root.after(16, lambda: update_time(time_item))


board = Board(canvas)
board.drawBoard()
update_time(board.p2_timer)
update_time(board.p1_timer)
root.mainloop()
