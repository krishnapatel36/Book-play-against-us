# Wythoff Nim Game Book

## Overview

The Wythoff Nim Game Book is a PDF document that provides a comprehensive guide to the Wythoff Nim game on an 8x8 chessboard. This book contains visual representations of various game states and their corresponding moves, designed to help players understand and strategize the game better.

## Features

- **Game Board Visualization**: Each page of the book features a chessboard layout with images representing game positions.
- **Game States**: Displays different game states with the Queen's position, target positions, and possible moves.
- **Winning Moves**: Highlights predefined winning positions to guide players.
- **Move Options**: Shows valid moves from the current position and their effects.

## Requirements

- **Python 3.x**: Ensure you have Python installed on your system.
- **fpdf Library**: The `fpdf` library is used to generate the PDF. Install it using pip:

  ```bash
  pip install fpdf
  ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd yourrepository
   ```

3. Install the required Python libraries:

   ```bash
   pip install fpdf
   ```

## Usage

1. **Prepare Images**: Place the following images in the same directory as the script:
   - `no1.png` - Image representing the Queen's initial position.
   - `no2.png` - Image representing a possible move.
   - `final.png` - Image representing the final game state.
   - `target1.png` - Image for the user reaching the target.
   - `target2.png` - Image for the computer reaching the target.

2. **Run the Script**:

   ```bash
   python WythoffNimBook.py
   ```

   This will generate a PDF named `WythoffNimGameBook_8x8.pdf` in the same directory.

## Code Explanation

- **Class `WythoffNimBook`**:
  - **`__init__`**: Initializes the PDF object, board size, tile size, image paths, and predefined winning positions.
  - **`get_valid_moves`**: Calculates valid moves from the current position.
  - **`computer_move`**: Determines the best move for the computer.
  - **`display_board`**: Draws the chessboard with images and labels.
  - **`pos_to_label`**: Converts a board position to a chess notation label.
  - **`add_page_to_pdf`**: Adds a page to the PDF with the current game state.
  - **`generate_book`**: Generates the entire PDF book with all possible game states.
