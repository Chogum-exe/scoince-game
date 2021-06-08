import json
import numpy as np
import random

def GenerateQuestions(type, topic, weight, falloff):
    # type = (MultipleChoice or TrueFalse
    # topic = (Biology, Chemistry, Computer, or Earth)
    QuestionFile = open('Question.json', 'r')
    JsonData = json.load(QuestionFile)

    WeightedRandom = str(int(round(np.random.normal(weight, falloff), 0)))

    GeneratedQuestion = JsonData[type][topic][WeightedRandom]

    if len(GeneratedQuestion) < 2:
        Q = random.choice(GeneratedQuestion)
    return GeneratedQuestion
print(GenerateQuestions('Multiple', 'Computer', 1, 0))
