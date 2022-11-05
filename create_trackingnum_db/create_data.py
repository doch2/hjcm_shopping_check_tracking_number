import json

dataDictionary = {}

for dataKind in ['name', 'phoneNum', 'trackingNum']:
    dataFilePath = "data/" + dataKind + ".txt"

    with open(dataFilePath) as f:
        dataDictionary[dataKind] = f.readlines()


finalResult = dict()
for phoneNum in dataDictionary['phoneNum']:
    indexNum = (dataDictionary['phoneNum']).index(phoneNum)

    if (indexNum+1) != len(dataDictionary['phoneNum']): #마지막 사람이 아닐 경우
        finalResult[phoneNum[:-1]] = dict()
        finalResult[phoneNum[:-1]]['name'] = (dataDictionary['name'][indexNum])[:-1]
        finalResult[phoneNum[:-1]]['trackingNum'] = (dataDictionary['trackingNum'][indexNum])[:-1]
    else:
        finalResult[phoneNum] = dict()
        finalResult[phoneNum]['name'] = dataDictionary['name'][indexNum]
        finalResult[phoneNum]['trackingNum'] = dataDictionary['trackingNum'][indexNum]


with open('finalData.json', 'w') as w:
    json.dump(finalResult, w, indent='\t', ensure_ascii=False)