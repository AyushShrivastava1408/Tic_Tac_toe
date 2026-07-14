# 🎮 Tic Tac Toe

A modern Tic Tac Toe game built entirely in **Python** using **Tkinter**. The game offers both **Player vs Player** and **Player vs Computer** modes with three AI difficulty levels: Easy, Medium, and Hard.

---A



## 📂 Project Structure

```
tic_tac_toe/
│
├── tictactoe.py
├── README.md

---

## 🛠 Technologies Used

- Python 3.x
- Tkinter
- Random
- Time
- Winsound (Windows)

No external libraries are required.

---

## 🎮 Game Modes

### 👥 Player vs Player

- Two players play on the same computer.
- Player X starts first.
- Turns alternate automatically.

### 🤖 Player vs Computer

Choose one of the following AI levels:

### Easy

- Computer selects random moves.

### Medium

- Takes winning move if available.
- Blocks opponent's winning move.
- Otherwise plays strategically with some randomness.

### Hard

- Uses the Minimax Algorithm with Alpha-Beta Pruning.
- Impossible to defeat.

---

## 📋 Rules

- The game is played on a 3×3 grid.
- Players take turns placing X and O.
- First player to get three marks in a row wins.
- Horizontal
- Vertical
- Diagonal
- If all cells are filled without a winner, the game ends in a draw.

---

## 🎯 Controls

| Action | Description |
|----------|-------------|
| Mouse Click | Place X or O |
| Restart | Start a new game |
| Main Menu | Return to menu |
| R | Restart Game |
| Esc | Back to Main Menu |

---

## 📊 Scoreboard

The game tracks:

- Player X Wins
- Player O / Computer Wins
- Draws

Scores remain until the application is closed.

---

## 🎨 UI Features

- Modern Color Theme
- Clean Layout
- Responsive Buttons
- Winner Highlight
- Game Status Display
- Attractive Dialog Boxes

---

## ▶️ How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/tic-tac-toe.git
```

### Open Project

```bash
cd tic-tac-toe
```

### Run

```bash
python main.py
```

---

## 💻 Requirements

- Python 3.8 or above

No additional packages are needed.

---


## 📸 Screens

- Main Menu
- Difficulty Selection
- Gameplay
- Winner Screen
- Draw Screen

---

This project is created for learning and educational purposes.

Feel free to modify and improve it.