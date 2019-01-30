from flask import Flask
from flask_socketio import SocketIO, send

app = Flask(__name__)

app.config['SECRET KEY'] = 'muneervee#' 
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
        print('Message: ' + msg)
        send(msg, broadcast = True)

if __name__ == '__main__':
        socketio.run(app)
	
