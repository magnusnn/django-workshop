# django-workshop
Noen enkle eksempel-applikasjoner i Django

## Requirements
- Python 3.7
- Pip installert
- Virtual env (optional but recommended!)
- Visual Studio Code eller tilsvarende


## Oppsett av løsningen lokalt
NOTE: Alle navigeringer/kommandoer er gjort via terminalen og har tatt rot-mappen til repoet som utgangspunkt.

Clone ned repositoriet og opprett et virtual env inne i mappen:
```
virtualenv -p path\to\python3x\python.exe env
```

Aktiver virtual env:
(Windows)
```
env\Scripts\activate
```

Verifiser at verson 3.7 av python kjører i virtualenv: 
```python```
```Ctrl+Z -> Enter``` - for å gå ut av pythonvinduet

Installer alle nødvendige pakker via pip:
```
pip install -r requirements.txt
```

Når installasjonen er ferdig er det på tide å migrere databasen og kopiere static-filer:
```
python theoffice\manage.py makemigrations
python theoffice\manage.py migrate
python theoffice\manage.py collectstatic
```


Når migrering av databasen er ferdig kan en starte serveren:
```
python theoffice\manage.py runserver
```

Serveren vil nå starte på `http://127.0.0.1:8000/`. Forsøk å åpne siden for å sjekke at installasjonen var vellykket.

Opprett så en admin-bruker fra terminal:
```
python theoffice\manage.py createsuperuser
```

Start serveren på nytt og logg inn i admin-panelet på `http://127.0.0.1:8000/`