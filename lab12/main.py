import firebase_admin
from firebase_admin import db

cred = firebase_admin.credentials.Certificate('firebase.json')
firebase_admin.initialize_app(cred, {"databaseURL": "https://lab12-312a2-default-rtdb.europe-west1.firebasedatabase.app/"})
ref = firebase_admin.db.reference('/')

print('Initializing Firebase')

ref.child('Messages').push({
    "name": "John",
    "message": "Hello World"
})

def stream_handler(message):
    print(message.data)


messages_stream = ref.child('Messages').listen(stream_handler)
messages_stream.close()

