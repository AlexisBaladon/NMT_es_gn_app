# NMT_es_gn_app

## BACKEND

```
cd backend
sudo docker build -t marian .
sudo docker run --network host marian
```

## FRONTEND

```
cd frontend/guarani-spanish-translator-frontend
sudo npm install
sudo npm run dev
```

## Use container

```
cd backend
sudo docker run -it --mount type=bind,source=./,target=/mnt marian
```