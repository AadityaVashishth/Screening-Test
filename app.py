from flask import Flask, redirect
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

def get_ist_time():
    """Get current time in IST timezone"""
    ist = pytz.timezone('Asia/Kolkata')
    return datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S %f")[:-3]

def get_top_output():
    """Get system stats using top command"""
    try:
        return subprocess.check_output(
            ['top', '-b', '-n', '1'], 
            stderr=subprocess.STDOUT,
            universal_newlines=True
        ).split('\n')[:20]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ["Error: Could not retrieve system stats"]

@app.route('/')
def home():
    return redirect('/htop')

@app.route('/htop')
def htop():

    name = "Aaditya Vashishth"
    username = os.getenv('USER', 'codespace')
    
    return f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {get_ist_time()}
    TOP output:
    {'\n'.join(get_top_output())}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)