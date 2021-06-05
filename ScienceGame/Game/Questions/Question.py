import json
import numpy as np
import random

def GenerateQuestions(type, topic, weight, falloff):
    # type = (MultipleChoice or TrueFalse
    # topic = (Biology, Chemistry, Computer, or Earth)
    QuestionFile = open(type + '/' + topic + '.json', 'r')
    JsonData = json.load(QuestionFile)

    WeightedRandom = str(round(np.random.normal(weight, falloff), 0))
    print(WeightedRandom)

    GeneratedQuestion = JsonData[WeightedRandom]
    if len(GeneratedQuestion) > 0:
        return random.choice(GeneratedQuestion)
        # random.randint(0, len(GeneratedQuestion))
    else:
        return GeneratedQuestion
print(GenerateQuestions('MultipleChoice', 'Computer', 1, 0))
