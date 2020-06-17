import speech_recognition as sr
import re

#file from youtube
ysrtsubfilename = "captions.srt"
wavefilefromy = "makesubtitle.wav"
with open(ysrtsubfilename) as files:
    filestr = files.read()

starts=re.findall(r"\d\d:\d\d:\d\d,\d\d\d -->", filestr)
durations=re.findall(r" --> \d\d:\d\d:\d\d,\d\d\d", filestr)


#make it secound
temp=starts[0]
def makesecound(temp):
    nums =re.findall(r"[0-9]+", temp)
    point = nums.pop()
    sec = nums.pop()
    nums.append(sec+"."+point)
    fsec = float(nums.pop())
    imin = int(nums.pop())
    ihou = int(nums.pop())
    secound = fsec + (imin*60) + (ihou*60*60)
    return secound
	

Ssec = [makesecound(std) for std in starts]
Dsec = [makesecound(std) for std in durations]
r = sr.Recognizer()
files = sr.AudioFile(wavefilefromy)
pre = 0
audios = []
with files as src:
	for i in range(len(Ssec)):
		offset=Ssec[i]-pre
		duration = Dsec[i] - Ssec[i]
		pre = pre = Dsec[0]
		audios.append(r.record(src, offset = offset, duration = duration))

print(len(audios), "pitch")
try:
    rec = r.recognize_google(audios[5], "bn-BD")
    print(rec)
except sr.UnknownValueError:
    print("it not clear")
    
except sr.RequestError as e:
    print("Internet error")
