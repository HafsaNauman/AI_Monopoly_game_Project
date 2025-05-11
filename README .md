# Monopoly AI Game Variant

An AI-enhanced version of the classic Monopoly board game that integrates multiple AI strategies and features a modern graphical interface.

## Project Overview

This project transforms the traditional Monopoly experience by embedding artificial intelligence agents—Random, Minimax, Monte Carlo Tree Search (MCTS), and Reinforcement Learning (RL)—into gameplay. It offers a complete simulation environment for multi-agent decision-making and a user-friendly GUI built with both Pygame and PyQt6, supporting full game mechanics, state persistence, and AI performance evaluation.

## Core Functionalities

- **AI Strategies**  
  - **Random**: Baseline agent making arbitrary decisions.  
  - **Minimax**: Optimal decision-making via lookahead search.  
  - **MCTS**: Monte Carlo Tree Search with playout-based evaluation.  
  - **Reinforcement Learning (RL)**: Agents that learn from simulated outcomes.

- **Complete Game Mechanics**  
  - Dice rolling and token movement.  
  - Property transactions: buying, auctions, mortgaging, building houses/hotels.  
  - Rent collection, income/luxury taxes, and jail rules.  
  - Chance & Community Chest cards with varied actions (move, collect, pay).

- **Graphical User Interface**  
  - Pygame implementation for interactive board rendering and animations.  
  - PyQt6 integration for modern dialog windows and enhanced UI elements.  
  - In-game dialogs for purchases, rent payments, and card draws.  

- **State Persistence**  
  - Save and load game sessions to JSON files.  
  - Full serialization of players, board state, decks, and card history.

- **AI Performance Evaluation**  
  - Built-in simulation harness to measure win rates, survival time, and decision latency.  
  - Tools for comparing strategies over hundreds of automated matches.

## Installation

1. **Prerequisites**  
   - Python 3.7 or later  
   - Pygame (tested with 2.6.1)  
   - PyQt6 (for enhanced dialogs)  
   - Tkinter (for file dialogs)

2. **Install Dependencies**  
   ```bash
   pip install pygame pyqt6
   ```

## Project Structure

```
AI_PROJECT/
├── assets/             # Board, token, house, hotel, and dice images
├── board.py            # Board mechanics and turn logic
├── board_config.py     # Static layout and square definitions
├── cards.py            # Chance & Community Chest cards and decks
├── dice.py             # Dice roll abstraction
├── game.py             # High-level Game class integrating AI and GUI hooks
├── player.py           # Player data model, properties, and serialization
├── squares.py          # Square subclasses (Property, Utility, Railroad, etc.)
├── strategy.py         # AI strategy implementations (agents)
├── gui.py              # Pygame-based graphical interface
├── gui_pyqt.py         # (Optional) PyQt6 dialogs and enhancements
└── README.md           # Project documentation (this file)
```

## Usage

Run the Pygame GUI:
```bash
python gui.py
```
- Click **Roll Dice** to advance turns.  
- Use **Save Game** / **Load Game** for session persistence.  
- Interact with on-screen dialogs for purchases, auctions, and card effects.

(Optionally, launch PyQt6 dialogs via `python gui_pyqt.py` if available.)

## Future Improvements

- **Full Auction UI**: Interactive bidding interface for human and AI players.  
- **Trade Negotiation**: Dialogs for property and cash exchanges between players.  
- **Networked Multiplayer**: Real-time games over TCP/IP or WebSockets.  
- **Advanced AI**: Integration of hybrid MCTS+RL agents, deep learning approaches.  
- **UI Polish**: Responsive board scaling, sound effects, dynamic animations, and theme customizations.  
- **Performance Optimizations**: Profiling and refactoring for faster AI decision-making.

## Team

- **Hafsa Nauman**: AI decision logic (Minimax, MCTS, RL)  
- **Hafsa Fatima**: Core game mechanics, board and property logic  
- **Haneesh Ali**: Graphical interface design and integration

## Download

You can download the required file from Google Drive:

[Download the file](https://drive.google.com/file/d/13VUCnfP7RtrWlmqVu0RMdne6imxzWUm3/view?usp=sharing)

## References

- Russell, S., & Norvig, P. (2016). *Artificial Intelligence: A Modern Approach*.  
- Sutton, R., & Barto, A. (2018). *Reinforcement Learning: An Introduction*.  
- [Pygame](https://www.pygame.org/)  
- [Monopoly (Game) – Wikipedia](https://en.wikipedia.org/wiki/Monopoly_(game))
