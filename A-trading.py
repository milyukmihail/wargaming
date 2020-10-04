import threading
import sys

args = input()

args = args.split()
arg1ForDef = int((int(args[0]) + 1) / 2)
arg2ForDef = int(args[0])
argStart = 1
arg2 = int(args[1])

def multi(arg1ForDef = arg1ForDef, arg2ForDef = arg2ForDef, argStart = argStart, arg2 = arg2):
    global count
    count = 0
    if arg1ForDef - 1 < arg1ForDef:
        for i in range(argStart, arg1ForDef): 
            for j in range(argStart, arg2ForDef + 1):
                if i * j == arg2:
                    count = count + 1

def multi1(arg1ForDef = arg1ForDef, arg2ForDef = arg2ForDef, argStart = argStart, arg2 = arg2):
    global count1
    count1 = 0
    if arg1ForDef + 1 > arg1ForDef:
        for i in range(arg1ForDef, arg2ForDef + 1):
            for j in range(argStart, arg2ForDef + 1):
                if i * j == arg2:
                    count1 = count1 + 1
                
                    

thread_video = threading.Thread(target=multi, name="proc_video")
thread_audio = threading.Thread(target=multi1, name="proc_audio")

thread_video.start()
thread_audio.start()

thread_video.join()
thread_audio.join()

allCount = count + count1

sys.stdout.write(str(allCount))
