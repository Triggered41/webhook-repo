from itertools import groupby
from flask import Blueprint, json, request, render_template
from DB.manager import insert_pull_req_action, insert_push_action, fetch_actions

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')

@webhook.route('/')
def home():
    print("accessed")
    logs_arr = [[{'action': 'MERGE', 'time': 123}, {'time': 123, 'action': 'PUSH'}], [{'time': 456, 'action': 'MERGE'}], [{'time': 789, 'action': 'PULL_REQUEST'}]]
    return render_template("index.html", logs=logs_arr, to_branch='Main', author="Triggered41", timestamp="21:00:42:56")

@webhook.route("/receiver", methods=["POST"] )
def github_hook():
    data = request.json
    event = request.headers.get("X-Github-Event")

    match event:
        case 'pull_request':
            if (data['action'] == 'closed'):
                if data['pull_request']['merged']:
                    insert_pull_req_action(data, True)
                    return
                insert_pull_req_action(data)
        case 'push':
            if data['commits'][0]['message'].startswith('Merge pull request'): return
            insert_push_action(data)
        case _:
            return {}, 200

@webhook.route('/fetchActions')
def getActions():
    data = fetch_actions()    
    logs_arr = [list(j) for i, j in groupby(data, lambda x: x['time'])]
    return render_template("cardsList.html", logs=logs_arr)
