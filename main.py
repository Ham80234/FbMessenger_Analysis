
import json, collections, numpy
words = []
person = []
for x in range(1,7): 
    filetoUse = './Jsons/message_'+ str(x) +'.json'
    with open(filetoUse) as json_file:
        data = json.load(json_file)
        for p in data['messages']:
            for item in p:
                person.append(p['sender_name'])
                if 'content' not in item:
                    print('')
                else:
                    for word in p['content'].split(): 
                        words.append(word)   
c = collections.Counter(words)
name = collections.Counter(person)
for current in c.most_common():
    if current[0].lower() == '':
        print(current)
        #the_file.write("".join((current)).encode('utf-8').strip())
        #the_file.write(",")
print(name)