import subprocess

def run_command(command, session_name):
    tmux_cmd = f'tmux new-session -d -s {session_name} "{command}"'
    subprocess.run(tmux_cmd, shell=True)

def main():
    # Task 1: Run python3 app.py in tmux session from /home/andresperozo884/ChatGPT-Self-Hosted-main
    command1 = 'cd /home/andresperozo884/ChatGPT-Self-Hosted-main && python3 app.py'
    run_command(command1, 'session1')
    print(f'Starting session1: {command1}')

    # Task 2: Run ./freechatgpt in tmux session from /home/andresperozo884/ChatGPT-Self-Hosted-main/api
    command2 = 'cd /home/andresperozo884/ChatGPT-Self-Hosted-main/api && ./freechatgpt'
    run_command(command2, 'session2')
    print(f'Starting session2: {command2}')

    # Task 3: Run docker-compose up in tmux session from /home/andresperozo884/invidious
    command3 = 'cd /home/andresperozo884/invidious && docker-compose up'
    run_command(command3, 'session3')
    print(f'Starting session3: {command3}')

if __name__ == "__main__":
    main()
