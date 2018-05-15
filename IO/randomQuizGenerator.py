#! python3
#  randomQuizGenerator.py - Creates quizzes with qurstions and answers in random order, along with the answer key.

import random

# The quiz data.Keys are states and values are their capitals.
capitals = {'Alabama':'Montgomery', 'Alaska':'Juneau', 'Arizona':'Phonenix', 'Arkansas':'Little Rock', 'California':'Sacramento', 
            'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida':'Tallahassee', 'Georgia':'Atlanta', 
            'Hawaii':'Honolulu', 'Idaho':'Boise', 'Illinois':'Springfield', 'Indiana':'Indianapolis', 'Iowa':'Des Moines'}

# Generate 35 quiz files.
for quizNum in range(35):
    #TODO:Create the quiz and answer key files.
    quizFile = open('capitalsquiz%s.txt'%(quizNum+1), 'w')
    answerKeyFile = open('capitalsquiz_answer%s.txt'%(quizNum+1), 'w')
    #TODO:Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' '*20) + 'State Capitals Quiz (Form %s)'%(quizNum+1))
    quizFile.write('\n\n')
    #TODO:Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)
    #TODO:Loop through all states,making a qurstion for each.
    for questionNum in range(len(capitals)):
        # Get right and wrong answers.
        correctAnswers = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswers)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswer + correctAnswers
        random.shuffle(answerOptions)
        #TODO:Write the question and answer options to the quiz file.
        #TODO:Write the answer key to a file.
    