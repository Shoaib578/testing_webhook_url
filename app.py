from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/testing_webhook', methods=['GET'])
def webhook():
    # Get data from query parameters
    data = request.args.to_dict()
    
    # Log the received data
    print(f"Received data: {data}")

    # Send a response back to the sender
    return jsonify({"status": "success", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True,port=80)