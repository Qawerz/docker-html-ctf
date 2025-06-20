# docker-html-ctf

## Установка 
```
pip install uvicorn docker jinja2 fastapi python-socketio
```
или 
```
pip install -r req.txt
```
## Запуск
```
python3 main.py
```

---

## Работа с Docker
Для работы на вашей тачке, надо сбилдить образы. Для этого используем `docker build`:
```
docker build -t alpine-ssh-ctf ./ssh-docker-alpine
docker build -t nginx-ctf ./nginx-docker
```
После запуска сервера и запуска одного из контейнеров можно воспользоваться коммандой `docker ps -a`, что выведет все имеющиеся контейнеры 

Для удаления контейнера воспользуйтесь `docker rm -f <cid>`, где cid - идентификатор контейнера. Он выглядит примерно так - *95da261b9acd*. Вписывать полностью его не нужно, можно обойтись первыми 3 символами - *95а*.

Если контейнеров скопилось много, можно удалять скопом `docker rm -f $(docker ps -aq)`.
