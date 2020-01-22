import json
import sqlite3
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    notification = '{ "rule_violation_id": 100, "staff_id": 1, "priority": "HIGH", "message": "Test message",' \
                   '"notification_date": "01.01.2019 00:00:00", "error_message": "test notification error." }'
    # parse notification:
    notification = json.loads(notification)
    print(notification)
    emit('message', notification, broadcast=True, namespace='/')
    return notification


if __name__ == '__main__':
    #app.run()
    socketio.run(app)