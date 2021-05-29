from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
{
'id' : 1,
'contact' : u'9987644456',
'name':u'raju',
'done': False
},
{
'id' : 2,
'contact' : u'9973920272',
'name':u'rahul',
'done': False
}
]
@app.route('/')
def helloworld():
    return('hello world')
@app.route('/add-data', methods = ['POST'])
def addtask():
    if not request.json:
        return jsonify({
        'status' : 'error',
        'message' : 'please provide the data'
        },400)
    task = {
    'id' : tasks[-1]['id'] + 1,
    'contact':request.json['contact'],
    'name' : request.json.get('name', ''),
    'done' : False
    }
    tasks.append(task)
    return jsonify({
        'status' : 'success',
        'message' : 'task added successfully'
    })
@app.route('/getdata')
def gettask():
    return jsonify({
        'data' : tasks
    })
if (__name__ == '__main__'):
    app.run(debug = True)
