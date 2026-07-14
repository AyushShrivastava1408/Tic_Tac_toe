import pygame
import sys
import random

# Initialize engine
pygame.init()
pygame.font.init()

# --- CONSTANTS & CONFIG ---
WIDTH, HEIGHT = 500, 650
FPS = 60

# Palette (Premium Midnight Theme)
COLOR_BG = (15, 23, 42)          # Deep Slate
COLOR_PANEL = (30, 27, 75)       # Deep Indigo
COLOR_GRID = (51, 65, 85)        # Slate Border
COLOR_X = (56, 189, 248)         # Cyan Neon
COLOR_O = (244, 63, 94)          # Pink Neon
COLOR_TEXT = (248, 250, 252)     # Off-white
COLOR_MUTED = (148, 163, 184)    # Gray
COLOR_WIN_BG = (99, 102, 241)    # Indigo Accent

# Setup Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Premium Tic-Tac-Toe")
clock = pygame.time.Clock()

# Typography Setup
try:
    FONT_TITLE = pygame.font.SysFont("Segoe UI", 36, bold=True)
    FONT_SUB = pygame.font.SysFont("Segoe UI", 16)
    FONT_STATUS = pygame.font.SysFont("Segoe UI", 20, bold=True)
    FONT_MARK = pygame.font.SysFont("Segoe UI", 64, bold=True)
    FONT_BTN = pygame.font.SysFont("Segoe UI", 18, bold=True)
except:
    FONT_TITLE = pygame.font.Font(None, 44)
    FONT_SUB = pygame.font.Font(None, 20)
    FONT_STATUS = pygame.font.Font(None, 24)
    FONT_MARK = pygame.font.Font(None, 74)
    FONT_BTN = pygame.font.Font(None, 22)

# Game State Variables
board = [""] * 9
current_player = "X"
is_game_active = True
vs_computer = True
winning_combo = []
status_msg = "Turn: Player X"
ai_timer = 0  

# Layout Calculations
GRID_SIZE = 360
GRID_OFFSET_X = (WIDTH - GRID_SIZE) // 2
GRID_OFFSET_Y = 160
CELL_SIZE = GRID_SIZE // 3

# UI Buttons (x, y, w, h)
btn_mode = pygame.Rect(320, 100, 110, 32)
btn_reset = pygame.Rect(GRID_OFFSET_X, 550, GRID_SIZE, 45)

WIN_CONDITIONS = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], 
    [0, 3, 6], [1, 4, 7], [2, 5, 8], 
    [0, 4, 8], [2, 4, 6]             
]

def draw_text_center(text, font, color, center_x, center_y):
    surface = font.render(text, True, color)
    rect = surface.get_rect(center=(center_x, center_y))
    screen.blit(surface, rect)

def check_result():
    global is_game_active, status_msg, winning_combo, current_player
    
    for condition in WIN_CONDITIONS:
        a, b, c = condition
        if board[a] and board[a] == board[b] == board[c]:
            is_game_active = False
            winning_combo = condition
            status_msg = f"Player {current_player} Wins! 🎉"
            return

    if "" not in board:
        is_game_active = False
        status_msg = "It's a Draw! 🤝"
        return

    current_player = "O" if current_player == "X" else "X"
    status_msg = f"Turn: Player {current_player}"

def find_best_move(player):
    for condition in WIN_CONDITIONS:
        marks = [board[idx] for idx in condition]
        if marks.count(player) == 2 and marks.count("") == 1:
            return condition[marks.index("")]
    return None

def trigger_computer_move():
    global ai_timer
    if not is_game_active or current_player != "O" or not vs_computer:
        return
    
    available = [i for i, val in enumerate(board) if val == ""]
    if not available:
        return

    choice = find_best_move("O")
    if choice is None:
        choice = find_best_move("X")
    if choice is None:
        choice = random.choice(available)

    board[choice] = "O"
    check_result()

def reset_game():
    global board, current_player, is_game_active, winning_combo, status_msg
    board = [""] * 9
    current_player = "X"
    is_game_active = True
    winning_combo = []
    status_msg = "Turn: Player X"

# --- MAIN LOOP ---
while True:
    mouse_pos = pygame.mouse.get_pos()
    
    # FIX: Changed pygame.event.get_events() to pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if btn_mode.collidepoint(mouse_pos):
                vs_computer = not vs_computer
                reset_game()
                
            if btn_reset.collidepoint(mouse_pos):
                reset_game()
                
            if is_game_active and not (vs_computer and current_player == "O"):
                x, y = mouse_pos
                if (GRID_OFFSET_X <= x <= GRID_OFFSET_X + GRID_SIZE and 
                    GRID_OFFSET_Y <= y <= GRID_OFFSET_Y + GRID_SIZE):
                    
                    col = (x - GRID_OFFSET_X) // CELL_SIZE
                    row = (y - GRID_OFFSET_Y) // CELL_SIZE
                    idx = row * 3 + col
                    
                    if board[idx] == "":
                        board[idx] = current_player
                        check_result()
                        if is_game_active and vs_computer:
                            ai_timer = pygame.time.get_ticks() + 400 

    if is_game_active and vs_computer and current_player == "O" and ai_timer != 0:
        if pygame.time.get_ticks() >= ai_timer:
            trigger_computer_move()
            ai_timer = 0

    # --- RENDERING ENGINE ---
    screen.fill(COLOR_BG)

    draw_text_center("TIC TAC TOE", FONT_TITLE, COLOR_TEXT, WIDTH // 2, 45)
    draw_text_center("Experience the classic with premium design", FONT_SUB, COLOR_MUTED, WIDTH // 2, 80)

    panel_rect = pygame.Rect(GRID_OFFSET_X, 100, GRID_SIZE, 42)
    pygame.draw.rect(screen, COLOR_PANEL, panel_rect, border_radius=10)
    
    status_color = COLOR_X if "Player X" in status_msg else (COLOR_O if "Player O" in status_msg else COLOR_TEXT)
    status_surface = FONT_STATUS.render(status_msg, True, status_color)
    screen.blit(status_surface, (panel_rect.x + 15, panel_rect.y + (panel_rect.h - status_surface.get_height()) // 2))

    mode_hover = btn_mode.collidepoint(mouse_pos)
    pygame.draw.rect(screen, (50, 45, 110) if mode_hover else COLOR_GRID, btn_mode, border_radius=6)
    mode_txt = "VS Computer" if vs_computer else "VS Player 2"
    draw_text_center(mode_txt, FONT_SUB, COLOR_TEXT, btn_mode.centerx, btn_mode.centery)

    grid_rect = pygame.Rect(GRID_OFFSET_X, GRID_OFFSET_Y, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, COLOR_GRID, grid_rect, width=1, border_radius=16)

    for i in range(9):
        row, col = i // 3, i % 3
        cell_x = GRID_OFFSET_X + col * CELL_SIZE
        cell_y = GRID_OFFSET_Y + row * CELL_SIZE
        cell_rect = pygame.Rect(cell_x + 5, cell_y + 5, CELL_SIZE - 10, CELL_SIZE - 10)

        if i in winning_combo:
            pygame.draw.rect(screen, COLOR_WIN_BG, cell_rect, border_radius=12)
            color_mark = COLOR_TEXT
        else:
            is_hovered = cell_rect.collidepoint(mouse_pos) and board[i] == "" and is_game_active
            if is_hovered and not (vs_computer and current_player == "O"):
                pygame.draw.rect(screen, (24, 30, 60), cell_rect, border_radius=12)
            else:
                pygame.draw.rect(screen, COLOR_PANEL, cell_rect, border_radius=12)
            color_mark = COLOR_X if board[i] == "X" else COLOR_O

        if board[i] != "":
            draw_text_center(board[i], FONT_MARK, color_mark, cell_rect.centerx, cell_rect.centery)

    reset_hover = btn_reset.collidepoint(mouse_pos)
    pygame.draw.rect(screen, (220, 225, 235) if reset_hover else COLOR_TEXT, btn_reset, border_radius=12)
    draw_text_center("Restart Match", FONT_BTN, COLOR_BG, btn_reset.centerx, btn_reset.centery)

    pygame.display.flip()
    clock.tick(FPS)