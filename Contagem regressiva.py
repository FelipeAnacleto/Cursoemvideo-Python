from time import sleep
import emoji

for c in range(10, -1, -1):
    sleep(0.5)
    print(c)
print(emoji.emojize(':fireworks:', language='alias'))
