import math
from fpdf import FPDF

class WythoffNimBook:
    def __init__(self):
        self.pdf = FPDF()
        self.board_size = 160  # Size of the chessboard
        self.tile_size = self.board_size // 8  # Size of each tile
        self.no1_image = 'no1.png'  # Path to the no1 image
        self.no2_image = 'no2.png'  # Path to the no2 image
        self.final_image = 'final.png'  # Path to the final image
        self.target1_image = 'target1.png'  # Path to the target1 image
        self.target2_image = 'target2.png'  # Path to the target2 image
        self.winning_positions = [
            (0, 2), (0, 5), (1, 1), (1, 4), (1, 7),
            (2, 0), (2, 3), (2, 6), (3, 2), (3, 5), 
            (4, 1), (4, 4), (4, 7), (5, 0), (5, 3), 
            (5, 6), (6, 2), (6, 5), (7, 1), (7, 4), 
            (7, 7)
        ]
        self.row_labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        self.col_labels = ['1', '2', '3', '4', '5', '6', '7', '8']

    def get_valid_moves(self, pos):
        moves = []
        x, y = pos
        for i in range(1, 3):  # Only 1 or 2 steps
            if x + i < 8:
                moves.append((x + i, y))  # Move vertically down
            if y + i < 8:
                moves.append((x, y + i))  # Move horizontally right
            if x + i < 8 and y + i < 8:
                moves.append((x + i, y + i))  # Move diagonally down-right
        return moves

    def computer_move(self, pos):
        valid_moves = self.get_valid_moves(pos)
        if not valid_moves:
            return None  # No valid moves available

        # Check if there's a winning move available in the predefined winning positions
        for move in valid_moves:
            if move in self.winning_positions:
                return move

        # If no winning move is found, choose the first valid move
        return valid_moves[0]

    def display_board(self, pos, move, user_moves, user_reached_target, computer_reached_target):
        # Draw chessboard with 'Q' for Queen and 'T' for Target
        for i in range(8):
            for j in range(8):
                x, y = 25 + j * self.tile_size, 65 + i * self.tile_size
                if (i + j) % 2 == 0:
                    self.pdf.set_fill_color(230, 230, 230)  # Light color for white tiles
                else:
                    self.pdf.set_fill_color(62, 180, 137)  # Dark color for black tiles
                self.pdf.rect(x, y, self.tile_size, self.tile_size, 'F')

                # Place images on the board
                if (i, j) == pos:
                    self.pdf.image(self.no1_image, x+1, y+1.3, self.tile_size-2, self.tile_size-2)
                elif (i, j) == (7, 7):
                    if user_reached_target:
                        self.pdf.image(self.target1_image, x+1, y+1.3, self.tile_size-2, self.tile_size-2)
                    elif computer_reached_target:
                        self.pdf.image(self.target2_image, x+1, y+1.3, self.tile_size-2, self.tile_size-2)
                    else:
                        self.pdf.image(self.final_image, x+2, y+1.3, self.tile_size-2, self.tile_size-2)
                elif (i, j) == move and (i, j) not in user_moves:
                    self.pdf.image(self.no2_image, x+1, y+1.3, self.tile_size-2, self.tile_size-2)

        # Add row labels
        self.pdf.set_font("Arial", size=12)
        for idx, label in enumerate(self.row_labels):
            self.pdf.set_xy(15, 65 + idx * self.tile_size + self.tile_size / 2 - 5)
            self.pdf.cell(10, 10, txt=label, align='C')

        # Add column labels
        for idx, label in enumerate(self.col_labels):
            self.pdf.set_xy(25 + idx * self.tile_size + self.tile_size / 2 - 5, 15)
            self.pdf.cell(10, 90, txt=label, align='C')

    def pos_to_label(self, pos):
        x, y = pos
        return f"{self.row_labels[x]}{self.col_labels[y]}"

    def add_page_to_pdf(self, pos, user_moves):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=20)

        # Draw border around the page
        self.pdf.rect(10, 10, 190, 270)

        # Center-align the title
        self.pdf.cell(340, -10, txt=f"Position: {self.pos_to_label(pos)}", ln=True, align="C")

        # Center-align the game board
        computer_move = self.computer_move(pos)
        user_reached_target = (7, 7) in user_moves
        computer_reached_target = computer_move == (7, 7)

        self.display_board(pos, computer_move, user_moves, user_reached_target, computer_reached_target)

    def generate_book(self):
        initial_position = (0, 0)
        positions_to_generate = [(initial_position, [])]
        generated_positions = set()
        pages = []

        while positions_to_generate:
            pos, user_moves = positions_to_generate.pop(0)
            if pos in generated_positions:
                continue

            pages.append((pos, user_moves))
            generated_positions.add(pos)

            valid_moves = self.get_valid_moves(pos)
            for move in valid_moves:
                if move not in generated_positions:
                    positions_to_generate.append((move, user_moves + [pos]))

        # Sort pages by position label
        pages.sort(key=lambda x: self.pos_to_label(x[0]))

        # Add sorted pages to PDF
        for pos, user_moves in pages:
            self.add_page_to_pdf(pos, user_moves)

        self.pdf.output("WythoffNimGameBook_8x8.pdf")
        print("Game book for 8x8 grid saved to WythoffNimGameBook_8x8.pdf")

if __name__ == "__main__":
    book = WythoffNimBook()
    book.generate_book()
