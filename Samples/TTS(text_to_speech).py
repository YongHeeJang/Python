from gtts import gTTS
from playsound import playsound

# tts(text to speech) : text를 speech로 변환하기 

text = '안녕하세요. 마이크로소프트 에이아이 스쿨에 오신 것을 환영합니다.'
text_en = 'Hi. Welcome to MS AI School'

tts = gTTS(text = text, lang='ko')
tts.save('h1.mp3')
# playsound는 mp3 파일을 재생시켜준다.
playsound('./h1.mp3') # 현재 dir가 아닌 다른 dir에 파일이 있으면, 위치를 지정해준다. './'는 상위 dir로 이동하는 것을 의미한다. 

tts_en = gTTS(text = text_en, lang='en')
tts_en.save('h2.mp3')
playsound('./h2.mp3')