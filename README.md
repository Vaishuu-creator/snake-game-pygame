# Snake Game – Python Pygame Edition

A classic **Snake Game** built using **Python and Pygame**, featuring smooth movement, increasing difficulty, score tracking, game over screen, and intuitive controls.

This project demonstrates real-time game rendering, event handling, collision detection, and simple game loop mechanics using Python’s most popular game engine — Pygame.

---

## Project Overview

The Snake Game is a timeless arcade game where the player controls a snake to eat food and grow longer while avoiding collisions with the walls or its own tail. The game becomes progressively harder as the snake gets longer.

This version of Snake includes:
- Real-time movement
- Score tracking
- Game over screen with restart option
- Clean visuals and smooth controls
- Simple and extendable code base

---

## Features

- Real-time game loop with smooth animation
- Food spawning and growth logic
- Collision detection (with walls & self)
- Score display
- Restart after game over
- Keyboard controls (Arrow keys)

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| Pygame | Game rendering and input handling |

---

## Project Structure

snake-game-pygame/  
│  
├── main.py - Main game script  
├── assets/ - Images & sounds (optional)  
├── requirements.txt - Dependencies  
└── README.md - Project documentation  

---

## Installation & Requirements

### 1️. Clone the Repo

    git clone https://github.com/Vaishuu-creator/snake-game-pygame
    cd snake-game-pygame

### 2️. Create Virtual Environment (Optional)

    python -m venv venv
    source venv/bin/activate    # Linux / macOS
    venv\Scripts\activate       # Windows

### 3️. Install Dependencies

    pip install -r requirements.txt

This project requires Python 3.8+ and Pygame.

---

## How to Play

1. **Run the game**
   ```bash
   python main.py
2. Use **Arrow Keys** to move the snake:
    - Up  ↑ 
    - Down ↓ 
    - Left ← 
    - Right → 
3. Eat the **food** to score points and grow longer.
4. Avoid colliding with:
    - Your own tail
    - The game boundaries
5. Game ends on collision — restart to play again!

---

## Gameplay Controls

| Action | Keys |
|----------|------------|
| Move Up | ↑ |
| Move Down | ↓ |
| Move Left | ← |
| Move Right | → |
| Quit | ESC |

---

## Challenges & Concepts Covered

- Game Loop Design
- Real-Time Rendering
- Keyboard Input Handling
- Collision Detection
- Dynamic Object Spawning
- Score Keeping

---

## Future Enhancements

- Add levels and obstacles
- Add sound effects (beeps & score sounds)
- Add high score tracking
- Add powerups (speed boost, extra life, etc.)
- Mobile / touch controls

---

## License

This project is licensed under the MIT License.

---

## Author

### Vaishali Murugesan
Final Year Computer Technology Student  
Aspiring AI & Software Engineer  

If you enjoyed the game, please give it a star!
