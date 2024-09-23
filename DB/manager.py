import datetime
from DB.extensions import col


REQUEST_ID = "request_id"
AUTHOR = "author"
ACTION = "action"
FROM_BRANCH = "from_branch"
TO_BRANCH = "to_branch"
TIMESTAMP = "timestamp"

REFRESH_TIME = 15

prefix = {1: 'st', 2: 'nd', 3: 'rd'}

def insert_pull_req_action(data: dict, merge=False):
    pr = data["pull_request"]
    col.insert_one({
        REQUEST_ID: pr["id"],
        AUTHOR: pr["user"]["login"],
        ACTION: "MERGE" if merge else "PULL_REQUEST",
        FROM_BRANCH: pr["head"]["ref"],
        TO_BRANCH: pr["base"]["ref"],
        TIMESTAMP: datetime.datetime.now(datetime.UTC)
    })

def insert_push_action(data):
    col.insert_one({
        REQUEST_ID: data['after'],
        AUTHOR: data['pusher']['name'],
        ACTION: 'PUSH',
        FROM_BRANCH: data['ref'].split('/')[-1],
        TO_BRANCH: data['ref'].split('/')[-1],
        TIMESTAMP: datetime.datetime.now(datetime.UTC),
        })

def fetch_actions():
    # Use below if required last 15 seconds actions
    actions = col.find({"timestamp": {"$gte": datetime.datetime.now(datetime.UTC)-datetime.timedelta(seconds=REFRESH_TIME)}}).sort({"timestamp": -1})
    arr = [ele for ele in actions]
    for ele in arr:
        ele['date'] = ele[TIMESTAMP].strftime(r"%b %d, %Y")
        ele['time'] = ele[TIMESTAMP].strftime(r"%d %B %Y - %I:%M %p UTC").lstrip('0')
    return arr

