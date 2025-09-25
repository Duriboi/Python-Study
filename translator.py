from deep_translator import GoogleTranslator

while True:
    lang = input('도착어 선택(영어, 일본어, 독일어, 종료): ')
    if lang == '종료':
        # 종료 입력 시
        print('프로그램을 종료합니다.')
        break
    # while 문 종료
    elif lang == '영어':
        # 도착어가 영어인 경우
        translator = GoogleTranslator(source='auto', target='en')
    # 도착어가 영어인 경우
    elif lang == '일본어':
        # 도착어가 일본어인 경우
        translator = GoogleTranslator(source='auto', target='ja')
    elif lang == '독일어':
        # 도착어가 독일어인 경우
        translator = GoogleTranslator(source='auto', target='de')
    else:
        print('지원하지 않는 언어입니다. 다시 선택하세요.')
        continue
        # 입력 오류 메시지 출력
        # 다음 반복으로 이동
    src = input('번역할 내용을 입력하세요: ')
    result = translator.translate(src)
    print(f'번역 결과: {result}')