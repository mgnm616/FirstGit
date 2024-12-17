from flask import Flask, request, jsonify, render_template 
import serial 
 
app = Flask(__name__) 
 
# Настройка serial порта 
serial_port = 'COM11'  
baud_rate = 9600 
ser = serial.Serial(serial_port, baud_rate) 
 
@app.route('/') 
def index(): 
    return render_template('client.html')
 
@app.route('/temperature', methods=['GET']) 
def get_temperature(): 
    try: 
        if ser.in_waiting > 0: 
            line = ser.readline() 
            temperature = line.decode("utf-8").strip() 
            return jsonify({"temperature": temperature}) 
        else: 
            return jsonify({"error": "No data available"}), 300 
    except Exception as e: 
        return jsonify({"error": str(e)}), 300 
 
if __name__ == '__main__': 
    app.run(debug=False, port=5000)
