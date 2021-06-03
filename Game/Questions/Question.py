from json import load
from random import gauss

def GenerateQuestions(type, topic, weight, falloff):
    # type = (MultipleChoice or TrueFalse
    # topic = (Biology, Chemistry, Computer, or Earth)
    QuestionFile = open(type + '/' + topic + '.json', 'r')
    JsonData = json.load(QuestionFile)
    WeightedRandom = round(random.guass(weight, falloff), 1)
    GeneratedQuestion = JsonData[WeightedRandom]
    return GeneratedQuestion
