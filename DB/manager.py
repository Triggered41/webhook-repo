import datetime
from DB.extensions import col


REQUEST_ID = "request_id"
AUTHOR = "author"
ACTION = "action"
FROM_BRANCH = "from_branch"
TO_BRANCH = "to_branch"
TIMESTAMP = "timestamp"

MILLISECOND_START_INDEX = 20

prefix = {1: 'st', 2: 'nd', 3: 'rd'}
utc_datetime = datetime.datetime.now(datetime.UTC)
utc_datetime = utc_datetime.strftime(r"%-d %B %Y - %I:%M %p UTC").split(' ')
last_letter = int(utc_datetime[0][-1])
if last_letter in prefix:
    utc_datetime = ' '.join([utc_datetime[0] + prefix[last_letter]] + utc_datetime[1:])

def insert_pull_req_action(data: dict):
    pr = data["pull_request"]
    col.insert_one({
        REQUEST_ID: pr["id"],
        AUTHOR: pr["user"]["login"],
        ACTION: "PULL_REQUEST",
        FROM_BRANCH: pr["head"]["ref"],
        TO_BRANCH: pr["base"]["ref"],
        TIMESTAMP: pr["created_at"]
    })

def insert_push_action(data):
    col.insert_one({
        REQUEST_ID: data['after'],
        AUTHOR: data['pusher']['name'],
        ACTION: 'PUSH',
        FROM_BRANCH: data['base_ref'],
        TO_BRANCH: data['base_ref'],
        TIMESTAMP: utc_datetime
        })