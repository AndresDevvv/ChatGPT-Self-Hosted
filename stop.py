import subprocess

def kill_tmux_session():
    try:
        subprocess.run(['tmux', 'kill-session'])
        print("tmux session killed successfully")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    kill_tmux_session()
# WARNING THIS WILL KILL ALL TMUX SESSIONS!
