from flask import Blueprint, json, request, render_template
from DB.manager import insert_pull_req_action, insert_push_action, fetch_actions

webhook = Blueprint('Webhook', __name__)

@webhook.route('/')
def home():
    print("accessed")
    logs_arr = [[{'action': 'merge', 'time': 123}, {'time': 123, 'action': 'push'}], [{'time': 456, 'action': 'merge'}], [{'time': 789, 'action': 'pull_request'}]]
    return render_template("index.html", logs=logs_arr, to_branch='Main', author="Triggered41", timestamp="21:00:42:56")

@webhook.route("/github", methods=["POST"] )
def github_hook():
    data = request.json
    event = request.headers.get("X-Github-Event")
    #pr = data['pull_request']
    #insert_pull_req(data)

    print("\n\n\n==========START==========\n\n\n")
    if (event == 'pull_request'):
        if (data['action'] == 'closed'):
            if data['pull_request']['merged']:
                insert_pull_req_action(data, True)
                pass
        else:
            datetime = data['pull_request']['created_at'].split('T')
            insert_pull_req_action(data)
    elif event == 'push':
        insert_push_action(data)
        pass
    print(data)
    print("\n\n\n===========END===========\n\n\n")
    return {}, 200

@webhook.route('/receiver', methods=["POST"])
def receiver():
    return {'helo': 'hi'}, 200

@webhook.route('/fetchActions')
def getActions():
    data = fetch_actions()
    return data

@webhook.route("/a")
def a():
    logs_arr = [[{'action': 'merge', 'time': 1},{'time': 1, 'action': 'push'}]]
    return render_template("index.html", logs=logs_arr, to_branch='Main', author="Triggered41", timestamp="123")


