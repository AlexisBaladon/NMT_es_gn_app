# NMT_es_gn_app

## BACKEND
sudo docker run --network host marian
sudo docker build -t marian .

## FRONTEND
sudo npm install
sudo npm run dev

## Pruebas

### Ejecución
sudo docker run -it --mount type=bind,source=./,target=/mnt marian