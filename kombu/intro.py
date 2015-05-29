from kombu import Connection

connection = Connection('amqp://guest:guest@localhost:5672//')

connection.connect()
#check whether connected boolean
connection.connected
connection.close()
#better practice, releases resource if in a connection pool else close
connection.release()


