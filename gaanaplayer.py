import webbrowser
import time

total_breaks = 3
break_count = 0

print("This program started one "+time.ctime())
while (break_count < total_breaks):
    time.sleep(1800)
    webbrowser.open("http://gaana.com/song/let-me-love-you-415")
    break_count = break_count + 1
    
