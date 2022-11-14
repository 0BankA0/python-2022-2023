from multiprocessing.resource_tracker import ResourceTracker
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello world'

@app.route("/datums")
def datums():
    return 'Sodien ir 14,11'

@app route('/lietotajs/<vards>/<vecums>')
def lietotajs(vards,vecums):
    dati= {vards:vecums}
    dati_jason 
    with open("letotaji.jason",'w',encoding="utf-8") as fails:


app.run(host='0.0.0.0', port=81)