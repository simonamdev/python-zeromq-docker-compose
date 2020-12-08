import zmq

print('Starting Client...')

context = zmq.Context()

socket = context.socket(zmq.SUB)
socket.connect("tcp://publisher:5555")

print('Starting Client loop now!')
while True:
    message = socket.recv()
    print('Received message: {}'.format(message))
