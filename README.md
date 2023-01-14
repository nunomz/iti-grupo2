# Check Folder/File Structure:
📦app \
 ┣ 📂files \
 ┃ ┣ 📂music \
 ┃ ┃ ┣ 📜90s_ArgoPad.wav \
 ┃ ┃ ┣ 📜... \
 ┃ ┃ ┗ 📜AM_VictorPad.wav \
 ┃ ┣ 📂uploads \
 ┃ ┗ 📂zips \
 ┣ 📂templates \
 ┃ ┣ 📜home.html \
 ┃ ┣ 📜logs.html \
 ┃ ┣ 📜style.css \
 ┃ ┗ 📜success.html \
 ┣ 📜Dockerfile \
 ┣ 📜requirements.txt \
 ┗ 📜server.py \
📦clientes \
 ┣ 📂client_files \
 ┃ ┣ 📜090000.jpg \
 ┃ ┣ 📜... \
 ┃ ┗ 📜090299.jpg \
 ┣ 📂client_gets \
 ┣ 📂umcliente \
 ┃ ┣ 📜get_client.py \
 ┃ ┗ 📜post_client.py \
 ┣ 📜auto_get_client.py \
 ┗ 📜auto_post_client.py \
📜.gitignore \
📜docker-compose.yml \
📜nginx.conf \
📜README.md \

# Usage:
0. For servers:
   - cd to for_server
   - docker-compose up --build
1. To build container:
   - docker-compose up --build --scale app=3
     - "--build": re-builds the container everytime. include if there are any changes to update
     - "--scale app=X": creates X instances of app. nginx will load balance to them from localhst
2. To create requests:
    1. open another terminal
    2. cd to clients
    3. run auto_post_client/auto_get_client