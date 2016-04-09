# nh2016

# Installation

```
pyvenv-3.5 venv
source venv bin activate
pip install -r requirements.txt
``` 

# Generation de la db

> python initdb.py

# Lancement du site

> sandman2ctl -d sqlite+pysqlite:///db.sqlite

# Utilisation de l'api

## Ajout d'un user

```
$ curl -X POST -d '{"name": "Jeff Knupp", "type": "patient"}' -H "Content-Type: application/json" http://127.0.0.1:5000/user
{
  "birthdate": null,
  "critical": null,
  "id": 1,
  "mail": null,
  "mobile": null,
  "name": "Jeff Knupp",
  "type": "patient"
}
```

## Ajout d'une data (reprendre l'id du user retourné précédemment)

```
$ curl -X POST -d '{"user_id": "1", "origine": "appli mobile", "type_data": "poids"}' -H "Content-Type: application/json" http://127.0.0.1:5000/data
{
  "date": null,
  "doc_url": null,
  "id": 1,
  "origine": "appli mobile",
  "type_data": "poids",
  "user_id": 1
}
```

## Ajout d'une ldata (reprendre le data_id précédent)

```
$curl -X POST -d '{"data_id": "1", "unit": "Kg", "value": "62"}' -H "Content-Type: application/json" http://127.0.0.1:5000/ldata
{
  "data_id": 1,
  "id": 1,
  "unit": "Kg",
  "value": "62"
}
```
