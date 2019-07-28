import csv
from app import db
from app.models import GlobalData

def addGlobal():
    path = 'app/global_data/'
    data = []
    with open(path + 'temp.csv') as f:
        d = csv.DictReader(f)
        for row in d:
            year = int(row['Year'])
            val = (float(row['Anomaly']) + 0.23) * 9 / 5 + 57
            data.append([year, val])

    with open(path + 'precip.csv') as f:
        d = csv.DictReader(f)
        for i, row in enumerate(d):
            val = float(row['Anomaly']) + 38.9764
            data[i].append(val)

    with open(path + 'seaLevel.csv') as f:
        d = csv.DictReader(f)
        for i, row in enumerate(d):
            val = float(row['Anomaly']) - 1.110236213
            data[i].append(val)

    with open(path + 'storms.csv') as f:
        d = csv.DictReader(f)
        for i, row in enumerate(d):
            val = float(row['Named Storms'])
            data[i].append(val)

    for i in data:
        entry = GlobalData(year=i[0],
                temp= i[1],
                precip=i[2],
                seaLevel=i[3],
                storms=i[4])
        db.session.add(entry)
    db.session.commit()
