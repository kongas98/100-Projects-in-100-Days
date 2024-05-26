class Question:
    """A class to model a question with its corresponding answer."""

    def __init__(self, text, answer):
        """
        Initialize a new Question instance.

        :param text: The text of the question.
        :param answer: The answer to the question (e.g., 'True' or 'False').
        """
        self.text = text      # Store the question text
        self.answer = answer  # Store the answer to the question
