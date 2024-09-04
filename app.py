from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

@app.route('/testing_webhook', methods=['POST'])
def webhook():
    # Get data from query parameters
    data = request.data
    # Log the received 
    print(f"Received data: {data}")
    app.logger.info(f"Received data: {data}")
    # Send a response back to the sender
    return jsonify({"status": "success", "data": "Hello"}), 200

if __name__ == '__main__':
    app.run(debug=True,port=80)