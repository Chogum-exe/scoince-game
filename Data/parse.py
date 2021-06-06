def Compare(Lines):
    CSVData = Lines.split(',')
    QType   = CSVData[0]
    QTopic  = CSVData[1]
    QDiff   = CSVData[2]
    return QType + QType + QTopic + QDiff

with open('ScienceGame - Data.csv') as csv:
    QuestionDiff = []
    for CurrentSearch in csv.readlines()[1:]:
        Find = Compare(CurrentSearch)
        print(Find)
        for SimilarSearches in csv.readlines()[1:]:
            Find2 = Compare(SimilarSearches)
            if Find == Find2:
                SimilarData = SimilarSearches.split(',')
                SimilarDiff = SimilarData[2]
                QuestionDiff[SimilarDiff] = SimilarSearches
                # Makes a python dict by the format Difficulty: [Question1], [Question2]
    for QuestionStrength in range(1, 20):
        # f.write('\t\"' + QuestionStrength + '\" : ' + '[{' + '\n')
        # Here we start the json dict
        for Questions in QuestionDiff[QuestionStrength]:
            CSVData = Questions.split(',')
            QType   = CSVData[0]
            QTopic  = CSVData[1]
            QDiff   = CSVData[2]
            QPrompt = CSVData[3]
            QA1     = CSVData[4]
            QA2     = CSVData[5]
            if len(CSVData) > 5:
                QA3 = CSVData[6]
            if len(CSVData) > 6:
                QA4 = CSVData[7]
            # Here we add json data
        f.write('\t\t' + '\"Question\"' + QPrompt)
