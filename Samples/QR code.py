# QR code 생성하기(web site연결)

import qrcode

qr_data = "www.naver.com"
qr_image = qrcode.make(qr_data)

qr_image.save(qr_data + '.png')


# with open하고 block안에 작업을 하면, block안의 코드가 끝나면 파일이 자동으로 닫혀짐.


with open('./site_list.txt', 'rt', encoding='UTF8') as f: # as f : 파일이름을 f라고 부를 것이라고 선언
# = with open('C:\Users\user\Documents\Github\Python\site_list.txt', 'rt', encoding='UTF8') as f:
    
    read_lines = f.readlines() # .readlines() : 전체 라인을 가져오겠다는 것

    for line in read_lines:
        line = line.strip() # .strip : 순수한 text만 들어가도록, 글자 이외에 쓸데 없는 것은 다 발라냄
        print(line)

        qr_data = line
        qr_image = qrcode.make(qr_data)

        qr_image.save(qr_data + '.png')

# print(read_lines)