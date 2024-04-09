import json

result = []

with open('data/english-vietnamese.txt', 'r', encoding='utf-8') as f:
    word = None
    pronounce = None
    definition = ''
    
    # Read each line in the file
    for line in f:
        line = line.strip()
        if line.startswith('@'):
            if(word is not None):
                result.append({
                    'word': word,
                    'pronounce': pronounce,
                    'definition': definition
                })
            index = line.find('/')
            if index == -1:
                index = None
            word = line[1:index].strip()
            pronounce = line[index:]
            definition = ''
        elif line != '': 
            definition += line + '\n'
        
        
with open('data/english-vietnamese.json', mode='w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

# with open('data/english-vietnamese.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
#     for item in data:
#         print(item['word'], item['pronounce'], item['definition'])