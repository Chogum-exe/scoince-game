import json
import numpy as np
import random

def GenerateQuestions(type, topic, weight, falloff):
    # type = (MultipleChoice or TrueFalse
    # topic = (Biology, Chemistry, Computer, or Earth)
    QuestionFile = open(type + '/' + topic + '.json', 'r')
    JsonData = json.load(QuestionFile)
    print(JsonData)

    WeightedRandom = str(int(round(np.random.normal(weight, falloff), 0)))
    print(WeightedRandom)

    GeneratedQuestion = JsonData[WeightedRandom]
    if len(GeneratedQuestion) > 0:
        Q = random.choice(GeneratedQuestion)
        # random.randint(0, len(GeneratedQuestion))
print(GenerateQuestions('MultipleChoice', 'Computer', 1, 0))
