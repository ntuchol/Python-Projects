import random

questions = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "What is 2 + 2?": ["4", "3", "5", "6"],
    "What is the largest planet in our solar system?": ["Jupiter", "Earth", "Mars", "Saturn"],
    "Who wrote 'To Kill a Mockingbird'?": ["Harper Lee", "Mark Twain", "Ernest Hemingway", "F. Scott Fitzgerald"],
    "What is the boiling point of water?": ["100°C", "90°C", "110°C", "120°C"]
}

num_quizzes = 5

for quiz_num in range(1, num_quizzes + 1):
    quiz_file = open(f'quiz_{quiz_num}.txt', 'w')
    answer_key_file = open(f'quiz_{quiz_num}_answers.txt', 'w')

    quiz_file.write(f'Quiz {quiz_num}\n\n')

    question_list = list(questions.keys())
    random.shuffle(question_list)

    for question_num, question in enumerate(question_list, 1):
        correct_answer = questions[question][0]
        answer_options = questions[question][:]
        random.shuffle(answer_options)

        quiz_file.write(f'{question_num}. {question}\n')
        for i, option in enumerate(answer_options):
            quiz_file.write(f'    {"ABCD"[i]}. {option}\n')
        quiz_file.write('\n')

        answer_key_file.write(f'{question_num}. {"ABCD"[answer_options.index(correct_answer)]}\n')

    quiz_file.close()
    answer_key_file.close()

print(f'{num_quizzes} quiz files generated successfully!')
