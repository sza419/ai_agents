import json

text = '''
Возьми зарядку, документы и воду. Если будет дождь, нужен зонт.
Поездка на 2 дня, активность - прогулка по городу.
'''
json_text = '''{
  "days": 2,
  "activity": "city walk",
  "weather": "rain",
  "items": ["зарядка", "документы", "вода", "зонт"]
}
'''
data = json.loads(json_text)

#print(data["days"])
#print(data["activity"])
#print(data["weather"])
#print(data["items"])
for i in data:
    print(data[i])