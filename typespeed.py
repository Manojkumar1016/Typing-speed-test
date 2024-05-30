from time import time

print('press enter to start typing or to break a new line')
print('press enter twice to finish typing')
input('..................................................')

#record timestamp when user starts typing
start= time()

text= []
while True:
    line = input()
    if not line:
        break
    text.append(line)

#record timestamp when user finishes typing
end= time()

print('..............................................')

elapsed_time = (end-start)/60
chars_count = sum(len(item) for item in text)
words_count = chars_count / 5

wpm = round(words_count / elapsed_time)
print(f'your avarage words per minute (wpm) is {wpm}')
if wpm < 30:
    print('you should learn the proper typing technique and practice more to improve your speed')
elif wpm <40:
    print('Not bad but still below avarage. focus on your technique and keep practicing')
elif wpm <50:
    print('your now avaragetypist. focus on your technique and keep practicing')
elif wpm <60:
    print('Congratulations!!!!!!!!! you are above avarage')
else:
    print('This is speed required for most jobs.')        