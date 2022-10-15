# Covid-telegram
   * **brief introduction** :
     * Telegram을 사용하여 특정시간에 코로나 확진률을 전송
   ![image](https://user-images.githubusercontent.com/103316263/195986307-06621030-e71f-4973-a047-26a635cb3641.png)
     * Github action을 통해 특정시간에 자동으로 메세지를 보냄
     * 작업환경에서 실행 할 수 있음
     
***
   ## File structure
   
   
    ├─ .github
    │  └─ workflows
    │     └─ setting.yml
    ├─ images
    │  └─ example.jpeg
    │  └─ github secrets.png
    ├─ .gitignore
    ├─ README.md
    ├─ requirements.txt
    ├─ crawlings.py
    └─ telegram_MSG.py
     
   ## How to use
   * **Action secrets** :
      * 중요 정보를 github action secrets을 settings에서 등록함
   ![제목 없음](https://user-images.githubusercontent.com/103316263/195986270-56b2adc6-e8e2-41ef-b017-ab0e38b1bad4.png)
      * set in https://github.com/eeea1/Covid-telegram/blob/main/.github/workflows/setting.yml
   * **local **
