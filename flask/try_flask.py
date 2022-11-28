#try_flask

from flask import Flask
import json
import datetime
from flask_cors import CORS
app = Flask(__name__)
app.config["JSON_AS_ASCII"]=False
CORS(app)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/lasit')
def lasit():
    with open ("chat.json",'r', encoding='utf-8') as f:
        zinas = f.read()
        
    return zinas
        

@app.route('/sutit/<vards>/<vecums>')
def sutit(vards,zina):
    tagad= datetime.now()
    laiks = tagad.starftime("%y/%n/%d, %H:%M:%S")
    print(vards,zina,laiks)

    rinda = [{
        "zina":zina,
        "vards":vards,
        "laiks":laiks
    }]

    with open ("chat.jason","r",encoding = 'utf-8') as f:
         vecasZinas= f.read()
         veciejson= json.loads(vecasZinas)

    veciejson.append(rinda)

    with open("chat.jason","w",encoding = 'utf-8') as f:
        f.write(json.dumps(veciejson,indent=2,ensure_ascii=False))
    return 'ok'
@app.route('/datums')
def datums():
    return "Šodien ir 14.novembris"

@app.route('/lietotajs/<vards>/<vecums>')
def lietotajs(vards,vecums):
    #return f"{vards} un {vecums}"
    dati = {vards:vecums}
    dati_json = json.dumps(dati)
    #return dati_json
    with open("lietotaji.json","w",encoding="utf-8") as fails:
        json.dump(dati_json,fails,indent=2,ensure_ascii=False)


app.run(host='0.0.0.0', port=81)