# Covid-telegram
   * **brief introduction** :
     * Telegram을 사용하여 특정시간에 코로나 확진률을 전송
   ![image](https://user-images.githubusercontent.com/103316263/195986307-06621030-e71f-4973-a047-26a635cb3641.png)
     * Github action을 통해 특정시간에 자동으로 메세지를 보냄
     * 작업환경에서 실행 할 수 있음
     
***
   ## File structure
    ├─ README.md
    └─ telegram_MSG.py
    ├─ crawlings.py
    ├─ .github
    │  └─ workflows
    │     └─ setting.yml
    ├─ .gitignore
    ├─ requirements.txt
      
***
   ## How to use
   * **Action secrets** :
      * 중요 정보를 github action secrets을 settings에서 등록함
   ![제목 없음](https://user-images.githubusercontent.com/103316263/195986270-56b2adc6-e8e2-41ef-b017-ab0e38b1bad4.png)
      * set in https://github.com/eeea1/Covid-telegram/blob/main/.github/workflows/setting.yml
   * **local working** :
      * Above repository and requirements.txt 다운로드
        ```
            git clone https://github.com/eeea1/Covid-telegram.git
            cd Covid-telegram
            pip install -r requirements.txt
        ```
      * crawlings : env 생성, 중요 정보 암호화
        ```
            #예시
            apikey = "발급받은 API키" # API 키를 다음 란에 입력해 주세요.
            korea = "https://api.corona-19.kr/korea/beta/?serviceKey="
            response = requests.get(korea + apikey)
            message = response.text
        ```
        * "https://api.corona-19.kr/" 에서 발급받기
      * telegram_MSG : env 생성, 중요 정보 암호화
        ```
            #예시
            Token = "발급받은 토큰"
            Chat_Id = "발급받은 Chat ID"
            bot = telegram.Bot(token=Token)
            chat_id = Chat_Id
        ```
        * To create a Bot
           ![image](https://user-images.githubusercontent.com/103316263/196686093-13c09a71-f6fc-4557-aaee-938c4869c342.png)
           ![image](https://user-images.githubusercontent.com/103316263/196686302-cd5b4e0d-cb11-420d-9811-e28c23d0e45d.png)
           ![image](https://user-images.githubusercontent.com/103316263/196686640-94962bea-940c-40c6-b96b-1727aceb7c67.png)
           

      * 실행
       ```
           python crawlings.py
 
           python telegram_MSG.py
       ```
***
   ### Tech stack
   * Language: Python 3.7 이상 
   * Tool: PyCharm (version 2022.02), Telegram Bot API (version 6.2) 
   * CI/CD: Github Action 
   * VCS(Version Control System): Git 
***
   ### Development period
   * 2022년 9월 3일 ~ 10월 17일 
***
   ### Developer
   * 박성민 
   * Email : dogrest0723@gmail.com 
