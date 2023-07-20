# Parking_lot

## Project Introduction

이 프로젝트는 두 가지 서비스로 구성되어 있습니다.

### 웹 사이트 서비스
웹 사이트 서비스는 사용자가 목적지를 입력하면 주변 주차장의 위치와 전체 주차 면수, 잔여 면수를 보여주는 서비스를 제공합니다. 사용자는 웹 사이트를 통해 원하는 목적지를 입력하면, 해당 위치 주변에 있는 주차장들의 정보를 지도를 통해 확인할 수 있습니다.

### 슬랙 ChatBot 서비스
슬랙 ChatBot 서비스는 사용자의 메세지에서 위치 키워드를 추출하여 해당 위치에서의 최적의 주차장에 대한 안내를 제공합니다. 사용자는 슬랙 메세지로 요청을 하면, 해당 위치에서의 최적의 주차장에 대한 정보를 슬랙으로 안내해줍니다. 이를 통해 사용자는 편리하게 주차장 정보를 얻을 수 있습니다.

## demo

- web

[web_demo_f 파일 참조]

- chatbot

 ![chatbot_demo](https://github.com/ella00100/Parking_lot/assets/103167624/25928fdf-57c2-4bc1-ae4d-6f734b15f62a)

## Tech Stack

### web site
- python
- cloud 9
- AWS Lightsail 
- django
- javaScript
- BootStrap
- HTML
- CSS

### chatBot
- python
- cloud 9
- AWS DynamoDB
- AWS EC2 
- slack

## How to Run
웹페이지를 돌리기위해 다음과 같은 작업을 실시해 주어야한다.

1. pip install django, pip install requests 등 import한 모듈을 전부 깔아준다
2. main 디렉토리의 apps.py 파일에서는 공공데이터 포털의 api를 받아온다. 하지만 서비스 키 부분을 공란으로 남겨두었기
때문에 공공데이터 포털에 접속후 해당 api 사용 신청을하고 받은 서비스 키를 8번줄에 있는 코드에 추가해야한다.
3. 링크는 그대로 사용하면 될 것이지만 만약 ssl인증서 오류가 난다면 링크의 주소를 https말고 http로 사용해야한다.(링크가 두개 있으니 오류나면 둘다 바꿔주는 것이 좋을 듯)

4. 다음은 main의 templates 디렉토리에 index.html 파일의 155번쨰 줄의 src = 부분 링크에 본인 카카오맵 api키를 추가하고 소괄호는 지워주면 된다.
5. 카카오맵 api에 본인이 서비스한 ip주소를 추가해야 맵에서 정보를 받아올 수 있다

6. 마지막으로 config 디렉토리에 sttings.py 파일의 29번쨰 줄 allowed_hosts에 본인이 서비스 할 ip를 추가해주어야 한다.
만약 로컬에서 돌라는거면 127.0.0.1만 있어도 된다.

7. 이제 서버를 돌릴때 터미널창에 python manage.py runserver 명령어를 치고 포트 8000번으로 접속한다. 

## Aurhors
- 윤서영 (Yun Seo Young) - Frontend & Server
- 김민규 (Kim Min Gyu) - Data Analysis
- 권성준 (Kwon Sung Jun) - Backend & Server
- 김건유 (Kim Geon Yu) - Backend
- 전진욱 (Jeon Jin Wook) - Planner
