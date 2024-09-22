from flask import Flask
from appref import views

app = Flask(__name__)

@app.route('/')
def index():
    return views.index()

# app.run(debug=True)

for i in {1:100,2:200,3:300}:
    print(i)
else:
    print("loop is end")