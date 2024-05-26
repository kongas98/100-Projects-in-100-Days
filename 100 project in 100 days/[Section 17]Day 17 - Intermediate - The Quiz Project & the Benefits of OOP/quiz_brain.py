class QuizBrain:
    """A class to manage the quiz process, including questions and scoring."""

    def __init__(self, bank):
        """
        Initialize a new QuizBrain instance.

        :param bank: A list of Question objects representing the question bank.
        """
        self.question_number = 0        # Initialize the question number to track the current question
        self.question_list = bank       # Store the list of questions
        self.score = 0                  # Initialize the score to track the user's score

    def still_has_questions(self):
        """
        Check if there are more questions left in the quiz.

        :return: True if there are more questions, False otherwise.
        """
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        """
        Display the next question to the user and prompt for an answer.
        Check the answer and update the score accordingly.
        """
        if self.question_number < 12:
            current_question = self.question_list[self.question_number]  # Get the current question from the list
            self.question_number += 1  # Increment the question number for the next round
            while True:
                q = input(f"Question {self.question_number}: {current_question.text} (True/False): ").lower()
                if q == "true" or q == "false":  # Validate user input
                    break
                print("Not a valid answer. Valid answers are True or False")
            if q == current_question.answer.lower():  # Check if the answer is correct
                self.score += 1  # Increment the score if the answer is correct
                print(f"You got it right!\nThe correct answer was: {current_question.answer}.\nYour current score is: {self.score}/{self.question_number}.")
            else:
                print(f"You got it wrong...\nThe correct answer was: {current_question.answer}.\nYour current score is: {self.score}/{self.question_number}.")
