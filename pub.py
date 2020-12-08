
import time
import zmq

print('Starting Server...')

context = zmq.Context()
socket = context.socket(zmq.PUB)

# socket.bind("tcp://*:5555") # both these options work
socket.bind("tcp://0.0.0.0:5555")

print('Starting Server Loop now!')
while True:
    time.sleep(1)
    message = 'Sent message at {}'.format(time.time())
    print(message)
    socket.send_string(message)
