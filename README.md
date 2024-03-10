# SECURITY WEB
Cíl bylo vytvořit jednoduchý web splňující požadavky jako zda váš web nemá bezpečnostní problémy jako XSS, XSRF, SQL Injection apod.

## Spuštění
- nejdříve si stáhneme projekt z [githubu](https://github.com/cesarjakub/web_security)
- musíme si vztvořit databázi pro mysql podle souboru `schema.sql`
- aby jsem se připojili do datábze musíme vytvořit soubot `.env` kam vložíme toto
```.env
DB_NAME = `nazev databaze`
DB_HOST = `hosta databaze`(většinou je to localhost)
DB_USER = `usera databaze`(většinou je to root)

TOKEN = `zde můžeme napsat co chcema`
```
- jsetli máme tohle tak můžeme spustit aplikaci příkazem `python app.py`
- otevřeme oblíbený vebový prohlížeč a napíšeme `127.0.0.1:5000`
- můžeme web používat

## Knihovny
- zde jsou knihovny, které jsou třeba pro [spuštění apliakce](#spuštění) 
    - **flask**
    - **dotenv**
    - **flask_mysqldb**
    - **os**
    - **hashlib**

## Server
- je zde možnost připojit se na server na kterém webovka běží
- [http://16.16.68.180:5000/](http://16.16.68.180:5000/)