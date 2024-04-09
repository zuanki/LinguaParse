import json
from tqdm import tqdm

result = []

for number in range(29):
    with open(f'data/japanese-vietnamese/term_bank_{number+1}.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in tqdm(data):
        word = item[0]
        pronounce = item[1]
        type = item[2]
        definition = ''
        for i in item[5]:
            definition += i + '\n'
            
        result.append({
            'word': word,
            'pronounce': pronounce,
            'type': type,
            'definition': definition
        })
        
with open('data/japanese-vietnamese.json', mode='w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=4)