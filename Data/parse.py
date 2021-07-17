import os
import json
import nested_dict as nd

with open('ScienceGame - Data.tsv') as csv:
    Questions = nd.nested_dict()
    for line in csv.readlines()[1:]:
        print(line)
        QData = line.strip().split('\t')
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
        Questions[QType][QTopic][QDiff] = data
        print(Questions)

with open (os.path.dirname(os.getcwd()) + '/ScienceGame/Questions/Question.json', 'w', encoding='utf-8') as file:
    json.dump(Questions, file, indent=4)
# with open
#     json.dump()
#     print(json.dumps(Questions, indent=4))
