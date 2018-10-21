import webbrowser
import time
totalbreaks = 4
breakcount = 0

print("STARTED ON  " +time.ctime())
while(breakcount < totalbreaks):
    time.sleep(1500)
    webbrowser.open("https://www.youtube.com/watch?v=58TBZnvyGwQ")
    breakcount = breakcount + 1
    print(breakcount)
    print("Tienes 5 minutos de descanso")
    time.sleep(300)
    webbrowser.open("https://www.youtube.com/watch?v=LHCob76kigA")
    print("Sé acabó el descanso, vuelta a trabajar")

