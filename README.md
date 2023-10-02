# Google Function etl-storage-bigquery


Esta Cloud function lee el archivo bank.csv ubicado en el bucket: curso_datos_bucket
parsea los datos y los guarda en una table de Bigqeury bank en el conjunto de datos curso-datos 


## Como correr la función 
```shell
curl -X GET  'https://xxxxx.cloudfunctions.net/etl-storage-bigquery?key=VALOR-KEY'
```


Para ejecutar la función se debe ejecutar utilizando un KEY TOKEN
* key token = Preguntar al Profesor del Curso


## Running automatically
This function is not scheduled to run automatically

## Bigquery

bucket  > bank

## Deployment
Esta función no se despliega automáticamente

## Dependencias
* functions-framework==3.*
* google-cloud-bigquery
* google-cloud-storage
