import io
import csv
import json
jsfile=open(r"D:\DB\EC\BLr\bbmp_south.json")
gs=json.load(jsfile)
data=gs["d"]
pts=data["Points"]

f=open(r"D:\DB\EC\BLr\Points_bbmp_south.csv", 'wb')
csv_file=csv.writer(f)
for i in pts:
	csv_file.writerow([i["Latitude"], i["Longitude"],i["InfoHTML"].encode('utf-8')])
f.close