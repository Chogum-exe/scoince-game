import json
import random

def GenerateQuestions(type, topic, weight, falloff):
    global JsonData
    # type = (MultipleChoice or TrueFalse
    # topic = (Biology, Chemistry, Computer, or Earth)
    if "JsonData" not in globals():
        QuestionFile = open('Question.json', 'r')
        JsonData = json.load(QuestionFile)
        QuestionFile.close()
        print('make')
    else:
        print('skip')
    # print(JsonData)
    WeightedRandom = str(int(round(np.random.normal(weight, falloff), 0)))
    GeneratedQuestion = JsonData[type][topic][WeightedRandom]
    if len(GeneratedQuestion) > 3:
        # Not 1 because there are 3 values
        GeneratedQuestion = random.choice(GeneratedQuestion)
    return GeneratedQuestion
print(GenerateQuestions('Multiple', 'Computer', 1, 0))
print(GenerateQuestions('Multiple', 'Computer', 1, 0))
print(GenerateQuestions('Multiple', 'Computer', 1, 0))
print(GenerateQuestions('Multiple', 'Computer', 1, 0))
