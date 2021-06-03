from json import load
from random import gauss
from random import randint

def GenerateQuestions(type, topic, weight, falloff):
    # type = (MultipleChoice or TrueFalse
    # topic = (Biology, Chemistry, Computer, or Earth)
    QuestionFile = open(type + '/' + topic + '.json', 'r')
    JsonData = json.load(QuestionFile)
    WeightedRandom = round(random.guass(weight, falloff), 1)
    GeneratedQuestion = JsonData[WeightedRandom]
    if len(GeneratedQuestion) > 0:
        return GeneratedQuestion[random.randint(0, len(GeneratedQuestion))]
    else:
        return GeneratedQuestion
