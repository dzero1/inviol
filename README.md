# app

Inviol Event App Challenge

## Folder structure
$api$ - FastAPI app
$app$ - Flutter app


### Fast api
Docker included.
to run
```
docker-compose build && docker-compose up
```

or directly from cli

```
cd api
pip install --no-cache-dir --upgrade -r requirements.txt

cd app
fastapi dev main.py
```


### Flutter app

run with

```
flutter pub install
flutter run
```