from flask import Flask, request, jsonify
import logging
import json

app = Flask(__name__)

@app.route('/new_user', methods=['POST'])
def new_user():
    data = request.data

    json_string = data.decode('utf-8')

    # Step 2: Parse the string into a JSON object
    json_data = json.loads(json_string)

    # # Extract required fields
    # user = {
    #     'id': data.get('id'),
    #     'email': data.get('email'),
    #     'created_at': data.get('created_at'),
    #     'updated_at': data.get('updated_at'),
    #     'first_name': data.get('first_name'),
    #     'last_name': data.get('last_name'),
    #     'orders_count': data.get('orders_count'),
    #     'total_spent': data.get('total_spent'),
    #     'note': data.get('note'),
    #     'verified_email': data.get('verified_email'),
    #     'tags': data.get('tags', 'sample, '),  # Default to "sample, "
    #     'last_order_name': data.get('last_order_name'),
    #     'currency': data.get('currency', 'ZAR'),  # Default to ZAR
    #     'phone': data.get('phone'),
        
    #     'sms_marketing_consent': data.get('sms_marketing_consent'),
    #     'admin_graphql_api_id': data.get('admin_graphql_api_id'),
    # }
    # app.logger.info(f"Received user data: {user}")


    app.logger.info(f"JSON data :{json_data}")
    
    # Return a response
    return jsonify({'message': 'User added successfully','user':json_data})



if __name__ == '__main__':
    app.run(debug=True,port=80)