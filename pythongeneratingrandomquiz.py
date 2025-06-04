import random

# Sample data: questions and their corresponding answers
questions = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "What is 2 + 2?": ["4", "3", "5", "6"],
    "What is the largest planet in our solar system?": ["Jupiter", "Earth", "Mars", "Saturn"],
    "Who wrote 'To Kill a Mockingbird'?": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
    "What is the boiling point of water?": ["100°C", "90°C", "110°C", "120°C"]
}

# Number of quizzes to generate
num_quizzes = 5

for quiz_num in range(1, num_quizzes + 1):
    # Create the quiz and answer key files
    quiz_file = open(f'quiz_{quiz_num}.txt', 'w')
    answer_key_file = open(f'quiz_{quiz_num}_answers.txt', 'w')

    # Write header for the quiz
    quiz_file.write(f'Quiz {quiz_num}\n\n')

    # Shuffle the order of questions
    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question_num, question in enumerate(question_list, 1):
        # Get the correct answer and shuffle the answer options
        correct_answer = questions[question][0]
        answer_options = questions[question][:]
        random.shuffle(answer_options)

        # Write the question and answer options to the quiz file
        quiz_file.write(f'{question_num}. {question}\n')
        for i, option in enumerate(answer_options):
            quiz_file.write(f'    {"ABCD"[i]}. {option}\n')
        quiz_file.write('\n')

        # Write the answer key
        answer_key_file.write(f'{question_num}. {"ABCD"[answer_options.index(correct_answer)]}\n')

    # Close the files
    quiz_file.close()
    answer_key_file.close()

print(f'{num_quizzes} quiz files generated successfully!')
