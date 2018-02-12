import sys
 
file = sys.argv[1]
lines = 0
words = 0
symbols = 0
 
for line in open(file, encoding='utf-8'):
    lines += 1
    symbols += len(line)
 
    position = 'out'
    for letter in line:
        if letter != ' ' and position == 'out':
            words += 1
            position = 'in'
        elif letter == ' ':
            position = 'out'
            
file_to_write = open('results/'+sys.argv[1], 'w+')
file_to_write.write("lines: "+ str(lines)+'\n')
file_to_write.write("words: "+ str(words)+'\n')
file_to_write.write("symbols: "+ str(symbols)+'\n')
 
