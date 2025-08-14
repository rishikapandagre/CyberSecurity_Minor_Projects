from flask import Flask, request, jsonify, render_template
import socket
from concurrent.futures import ThreadPoolExecutor

app=Flask(__name__)

def scan_port(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result=s.connect_ex((ip,port))
            return port if result==0 else None
    except:
        return None

@app.route('/')
def index():
    return render_template('homepage.html')

@app.route('/scan', methods=['POST'])
def scan():
    data=request.get_json('ip')
    ip=data.get('ip') if data else None
    if not ip:
        return jsonify({'error': "IP address is required..."}), 400
    ports=range(1, 1025)
    open_ports=[]

    with ThreadPoolExecutor(max_workers=100) as executor:
        results= executor.map(lambda p: scan_port(ip, p), ports)
        open_ports=[p for p in results if p]
    
    return jsonify({'open_ports': open_ports})

if __name__ =='__main__':
    app.run(debug=True)