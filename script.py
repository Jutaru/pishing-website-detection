import csv
import data_extractor as ext


item = []
data = []

data.append(["url", "ip", "At", "Dots", "sensitivewords", "traffic", "depth", "Length", "Token", "redirection"," prefix","tinyUrl","label"])

with open('dataset/data.csv', 'r' ,newline='') as csvfile:
    reader = csv.reader(csvfile)
    i = 1
    for row in reader:
        try:
            item = [
                row[0],
                ext.haveIP(row[0]),
                ext.haveAt(row[0]),
                ext.nbDots(row[0]),
                ext.sensitiveWord(row[0]),
                ext.web_traffic(row[0]),
                ext.depthURL(row[0]),
                ext.getLength(row[0]),
                ext.httpToken(row[0]),
                ext.redirection(row[0]),
                ext.prefix(row[0]),
                ext.tinyURL(row[0]),
                row[1]

            ]
            data.append(item)
            print(i, "/22324")
            i += 1
        except:
            print(row)
            i += 1

with open('dataset/datafinal.csv', 'w' ,newline='') as csvfile:
    writer = csv.writer(csvfile)
    for row in data:
        writer.writerow(row);