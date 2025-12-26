# 🎯 Python Quiz Game

> *Test your knowledge with this interactive quiz game! Create, manage, and play custom quizzes with a beautiful terminal interface.*

## 🌟 Highlights

- **Interactive CLI** - Beautiful terminal interface with formatted menus
- **Question Management** - Add, edit, delete, and shuffle questions easily
- **Smart Validation** - Handles user errors gracefully with robust input validation
- **Multiple Save Slots** - Save and load different quiz sets as JSON files
- **Flexible Gameplay** - Play with any number of questions (1+)

## ℹ️ Overview

**Python Quiz Game** is a feature-rich terminal application that allows users to create, manage, and play custom quizzes. Built with Python's standard library, it demonstrates clean code architecture, robust error handling, and user-friendly design principles. Whether you're learning programming concepts, studying for exams, or just having fun, this quiz game provides an engaging experience.

## 🚀 Quick Start

```python
# Clone and run the game
python quiz_game.py

# From the main menu:
# 1. Play Game - Test your knowledge
# 2. Manage Questions - Create your own quiz sets
# 3. View Questions - Review what you've learned
# 4. Quit - Exit the application
```

## 🎮 Features

### 📚 **Quiz Gameplay**
- Random question selection
- Case-insensitive answer checking
- Score tracking with percentages
- Flexible play with any number of questions

### 🛠️ **Question Management**
- Add new questions and answers
- Edit existing questions
- Delete specific questions or clear all
- Preview with truncation for long text

### 💾 **Save System**
- Multiple save slots (math.json, geography.json, etc.)
- Auto-save/load functionality
- JSON-based storage for easy sharing
- File management (list, delete saves)

### 🎨 **User Experience**
- Clean terminal interface with centered headers
- Robust input validation (handles spaces, case, errors)
- Confirmation dialogs for destructive actions
- Clear navigation with consistent menus

## 📋 Example Session

```
========================================
            QUIZ MAIN MENU
========================================

1. Start Game
2. Manage Questions
3. View Questions
4. Quit

Choice (1-4): 1

========================================
              QUIZ GAME
========================================

Question 1/5:
  What is the capital of France?
Answer: paris
✓ Correct!

Your score: 4/5 (80.0%)
```

## ⬇️ Installation

### Requirements
- Python 3.8 or higher
- Standard library only (no external dependencies!)

### Quick Install
```bash
# Clone the repository
git clone https://github.com/yourusername/quiz-game.git
cd quiz-game

# Run directly
python quiz_game.py
```

### Running from Source
```python
# The game is a single file - just download and run!
python quiz_game.py
```

## 🏗️ Project Structure

```
quiz_game.py          # Main application
quiz_saves/           # Auto-created save folder
    ├── math.json     # Example save file
    ├── geography.json
    └── autosave.json # Auto-saved questions
```

## 🧩 Code Architecture

### Key Functions
- `main_menu()` - Central navigation hub
- `game()` - Core quiz logic with scoring
- `manage_questions()` - CRUD operations for questions
- `save_questions()` / `load_questions()` - Persistent storage
- `gt_vld_in()` - Robust input validation

### Design Patterns
- **Modular Functions** - Each does one thing well
- **Global State Management** - Clear variable scope
- **Error Handling** - Graceful degradation
- **User Feedback** - Consistent messaging

## 📚 Learning Points

This project demonstrates:
- Python basics (functions, loops, conditionals)
- Data structures (lists, tuples)
- File I/O (JSON reading/writing)
- User input validation
- Terminal UI design
- Error handling
- Code organization

## 🔧 Development

### For Beginners
Great learning project! You can:
1. Add new question types (multiple choice, true/false)
2. Implement a timer for each question
3. Add difficulty levels
4. Create categories/tags for questions
5. Add a leaderboard system

### For Developers
The code is structured for easy extension:
- Clear function boundaries
- Consistent naming conventions
- Comprehensive comments
- Robust error handling

## 💭 Feedback and Contributing

Found a bug? Have a feature request? Want to contribute?

1. **Report Issues**: Open an issue on GitHub with detailed information
2. **Suggest Features**: Share your ideas for making the quiz game better
3. **Contribute Code**: Fork the repo and submit a pull request
4. **Share Quizzes**: Create and share your question sets with others!

### Contribution Areas
- New question formats (multiple choice, image-based)
- Enhanced scoring systems
- Network multiplayer support
- GUI version using tkinter/PyQt
- Additional language support

## 📄 License

This project is open source

## 🌟 Show Your Support

Give a ⭐️ if this project helped you or inspired your learning journey!

---

*Happy Quizzing! 🎯*
