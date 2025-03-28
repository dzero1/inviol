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

#### fast CLI info
```
FastAPI CLI version: 0.0.7
```


### Flutter app

run with

```
flutter pub install
flutter run
```

#### Flutter CLI version info
```
Flutter 3.24.3 • channel stable • https://github.com/flutter/flutter.git
Framework • revision 2663184aa7 (7 months ago) • 2024-09-11 16:27:48 -0500
Engine • revision 36335019a8
Tools • Dart 3.5.3 • DevTools 2.37.3
```