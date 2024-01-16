from flask import Flask, render_template, request, jsonify, redirect, make_response, abort
from chatgpt import chat_with_gpt
import json

app = Flask(__name__)

# Load user data from the database
with open('database.json', 'r') as file:
    users = json.load(file)

def set_user_cookie(username, response):
    # Set a cookie with the username
    response.set_cookie('username', username)


@app.route('/')
def index():
    # Check if the user has a valid cookie
    username = request.cookies.get('username')
    if username and username in users:
        return redirect('/chat')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check if the username exists in the database
    if username in users:
        user = users[username]

        # Check if the entered password matches the stored password
        if password == user['password']:
            # Set a cookie with the username
            resp = make_response(redirect('/chat'))
            set_user_cookie(username, resp)

            return resp
        else:
            return "Invalid password"
    else:
        return "Invalid username"
@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']

    # Check if the username already exists
    if username in users:
        return "Username already exists. Choose a different username."
    else:
        # Create a new user in the database
        users[username] = {'password': password, 'trials_left': 5}
        update_database(users)

        # Redirect to chat after successful registration
        resp = make_response(redirect('/chat'))
        set_user_cookie(username, resp)

        return resp

@app.route('/chat')
def chat():
    # Check if the user has a valid cookie
    username = request.cookies.get('username')
    if username and username in users:
        user = users[username]
        return render_template('chat.html', username=username, trials_left=user['trials_left'])
    else:
        return redirect('/')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.form['user_input']
    username = request.cookies.get('username')

    # Check if the user has a valid cookie
    if username and username in users:
        user = users[username]

        # Check if the user has trials left
        if user['trials_left'] > 0:
            gpt_response = chat_with_gpt(user_input, user['trials_left'])

            # Decrement trials_left after successful message
            user['trials_left'] -= 1
            update_database(users)

            return jsonify({'response': gpt_response})
        else:
            return jsonify({'response': 'You have reached your trial limit. Request more trials by logging in again.'})
    else:
        return jsonify({'response': 'Invalid user'})
    
@app.route('/admin')
def admin_panel():
    username = request.cookies.get('username')
    if username and username in users and users[username].get('admin', False):
        return render_template('admin.html', users=users)
    else:
        abort(403)  # Forbidden


# Updated route to edit a user
@app.route('/admin/edit/<username>', methods=['GET', 'POST'])
def edit_user(username):
    if username in users:
        if request.method == 'POST':
            # Update user information based on the form data
            users[username]['password'] = request.form['new_password']
            users[username]['trials_left'] = int(request.form['new_trials_left'])
            
            update_database(users)

            return redirect('/admin')

        return render_template('edit_user.html', username=username, user=users[username])
    else:
        return "User not found"

# New route to delete a user
@app.route('/admin/delete/<username>')
def delete_user(username):
    if username in users:
        del users[username]
        update_database(users)
        return f"Deleted user: {username}"
    else:
        return "User not found"


def update_database(users_data):
    # Update the database file with the new user data
    with open('database.json', 'w') as file:
        json.dump(users_data, file)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
