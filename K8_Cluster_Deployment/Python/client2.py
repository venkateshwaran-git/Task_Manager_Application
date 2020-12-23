# docker run -p 6379:6379 --name redisjson redislabs/rejson:latest
# docker run -p 27017:27017 --name mongodb mongo:latest

from rejson import Client, Path
from datetime import timedelta
from timeloop import Timeloop
from pymongo import MongoClient

# start timeloop, connect to queue, connect to database
tl, rj, client = Timeloop(), Client(host='redis', port=6379, decode_responses=True), MongoClient('mongo', 27017)
db = client.mydb


# every 10 seconds, pop from queue
@tl.job(interval=timedelta(seconds=5))
def send_to_db():
    print("Listening for tasks the queue..")
    try:
        db['to-do'].insert_one(rj.jsonarrpop('tasks', Path.rootPath()))
        print("Found a task.. Sending it to database..")
    except:
        print('queue is empty..')


if __name__ == "__main__":  tl.start(block=True)
