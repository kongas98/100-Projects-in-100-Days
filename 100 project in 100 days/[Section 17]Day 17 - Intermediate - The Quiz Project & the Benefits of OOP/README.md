# Quiz Game

This project is a simple console-based quiz game. The game presents a series of true/false questions to the user, tracks their score, and provides feedback on their answers. The project is implemented in Python and is designed to be easily extendable with additional questions or features.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- Presents a series of true/false questions to the user.
- Tracks and displays the user's score.
- Provides immediate feedback on each answer.
- Supports adding new questions easily.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quiz-game.git
2. Navigate to the project directory:
```bash
cd quiz-game
```
## Usage
Run the main script to start the quiz:

```bash
python main.py
````
The user will be prompted with a series of true/false questions. Enter your answer and receive immediate feedback.

## Project Structure
* **`main.py`**: The main script that runs the quiz game.
* **`question_model.py`**: Contains the **`Question class`**, which models a quiz question with text and answer attributes.
* **`data.py`**: Contains a list of dictionaries, where each dictionary represents a quiz question with a text and an answer.
* **`quiz_brain.py`**: Contains the **`QuizBrain class`**, which handles the quiz logic, including checking answers, keeping track of the score, and moving to the next question.

### main.py
This script is the entry point of the quiz game. It initializes the quiz questions from **`data.py`**, creates a **`QuizBrain`** instance, and runs the quiz loop.

### question_model.py
This script defines the **`Question class`**, which models a quiz question with text and answer attributes.

### data.py
This script contains a list of dictionaries called **`question_data`**. Each dictionary in this list represents a quiz question with a **`text`** (the question) and an **`answer`** (True/False).

### quiz_brain.py
This script defines the **`QuizBrain class`**, which:

* Manages the list of questions.
* Keeps track of the current question number and the user's score.
* Asks the user the next question.
* Checks if the user's answer is correct.
* Provides feedback to the user.

## Contributing
Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.
