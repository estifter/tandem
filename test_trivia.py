import pytest

import trivia

def test_randomize_choices():
    questions = trivia.get_questions('questions.json')
    for question in questions:
        assert len(question['incorrect']) + 1 == len(trivia.randomize_choices(question))
