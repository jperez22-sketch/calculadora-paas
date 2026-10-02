# Calculadora Cloud - PaaS

Aplicación web sencilla desarrollada con Python y Flask y preparada para desplegarse en Google Cloud Run.

## Ejecución local

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Abrir: http://localhost:8080

## Despliegue en Google Cloud Run

Desde esta carpeta:

```bash
gcloud run deploy calculadora-cloud --source . --region us-central1 --allow-unauthenticated
```

Cloud Run construye y despliega el servicio desde el código fuente.
