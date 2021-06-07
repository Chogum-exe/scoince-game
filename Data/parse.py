import nested_dict as nd

with open('ScienceGame - Data.csv') as csv:
    QuestionDiff = nd.nested_dict()
    for line in csv.readlines()[1:]:
        print(line)
        QData = line.strip().split(',')
        print(QData)
        QType = QData[0]
        QTopic = QData[1]
        QDiff = QData[2]
        Qquestion = QData[3]
        Qanswers =  []
        for a in QData[4:8]:
            if a:
                Qanswers.append(a)
        Qresult = QData[8]
        data = {
            'question': Qquestion,
            'answer': Qanswers,
            'result': Qresult,
        }
        QuestionDiff[QType][QTopic][QDiff] = data
        print(QuestionDiff)
    import json
    print(json.dumps(QuestionDiff, indent=4))
