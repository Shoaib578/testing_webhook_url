import json
from flask import Blueprint,request,jsonify,render_template
from datetime import datetime
 

from application.models.models import *

routes = Blueprint('routes', __name__)

@routes.route('/new_user', methods=['POST'])
def new_user():
    data = request.data

    # Step 1: Decode and parse the incoming JSON data
    json_string = data.decode('utf-8')
    json_data = json.loads(json_string)

    # Step 2: Extract the relevant attributes from the parsed JSON data using `.get()`
    new_user = User(
        id=json_data.get('id'),
        email=json_data.get('email'),
        created_at=datetime.fromisoformat(json_data['created_at']) if json_data.get('created_at') else None,
        updated_at=datetime.fromisoformat(json_data['updated_at']) if json_data.get('updated_at') else None,
        first_name=json_data.get('first_name'),
        last_name=json_data.get('last_name'),
        orders_count=json_data.get('orders_count', 0),  # Default to 0 if missing
        total_spent=json_data.get('total_spent', '0.00'),
        note=json_data.get('note'),
        verified_email=json_data.get('verified_email', False),
        tags=json_data.get('tags', ''),
        last_order_name=json_data.get('last_order_name'),
        currency=json_data.get('currency'),
        phone=json_data.get('phone'),
        email_marketing_consent=json_data.get('email_marketing_consent'),
        sms_marketing_consent=json_data.get('sms_marketing_consent'),
        admin_graphql_api_id=json_data.get('admin_graphql_api_id')
    )

    # Add the new user record to the session and commit it to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully', 'user_id': new_user.id}), 201



    

@routes.route('/start_checkout', methods=['POST'])
def start_checkout():
    data = request.data

    # Step 1: Decode and parse the incoming JSON data
    json_string = data.decode('utf-8')
    json_data = json.loads(json_string)

    # Step 2: Extract the relevant attributes from the parsed JSON data
    checkout = Checkout(
        id=json_data.get('id'),
        token=json_data.get('token'),
        cart_token=json_data.get('cart_token'),
        email=json_data.get('email'),
        gateway=json_data.get('gateway'),
        buyer_accepts_marketing=json_data.get('buyer_accepts_marketing'),
        buyer_accepts_sms_marketing=json_data.get('buyer_accepts_sms_marketing'),
        sms_marketing_phone=json_data.get('sms_marketing_phone'),
        created_at=datetime.fromisoformat(json_data.get('created_at')) if json_data.get('created_at') else None,
        updated_at=datetime.fromisoformat(json_data.get('updated_at')) if json_data.get('updated_at') else None,
        landing_site=json_data.get('landing_site'),
        note=json_data.get('note'),
        referring_site=json_data.get('referring_site'),
        taxes_included=json_data.get('taxes_included'),
        total_weight=json_data.get('total_weight'),
        currency=json_data.get('currency'),
        completed_at=datetime.fromisoformat(json_data.get('completed_at')) if json_data.get('completed_at') else None,
        phone=json_data.get('phone'),
        customer_locale=json_data.get('customer_locale'),
        subtotal_price=json_data.get('subtotal_price'),
        total_price=json_data.get('total_price'),
        total_discounts=json_data.get('total_discounts'),
        total_tax=json_data.get('total_tax'),
        abandoned_checkout_url=json_data.get('abandoned_checkout_url')
    )

    # Add the checkout record to the session and commit it to the database
    db.session.add(checkout)
    db.session.commit()

    return jsonify({'message': 'Checkout data stored successfully', 'checkout_id': checkout.id}), 201



# Endpoint to handle POST request and store cart data
@routes.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    data = request.data

    # Step 1: Decode and parse the incoming JSON data
    json_string = data.decode('utf-8')
    json_data = json.loads(json_string)

    # Step 2: Extract the relevant attributes from the parsed JSON data
    new_cart = Cart(
        id=json_data.get('id'),
        token=json_data.get('token'),
        line_items=json_data.get('line_items'),  # JSON field, directly stored
        note=json_data.get('note', ''),
        updated_at=datetime.fromisoformat(json_data['updated_at'].replace('Z', '+00:00')) if json_data.get('updated_at') else None,
        created_at=datetime.fromisoformat(json_data['created_at'].replace('Z', '+00:00')) if json_data.get('created_at') else None
    )

    # Add the new cart record to the session and commit it to the database
    db.session.add(new_cart)
    db.session.commit()

    return jsonify({'message': 'Cart added successfully', 'cart_id': new_cart.id}), 201



# Endpoint to handle POST request and store purchase data
@routes.route('/purchase', methods=['POST'])
def purchase():
    data = request.data

    # Step 1: Decode and parse the incoming JSON data
    json_string = data.decode('utf-8')
    json_data = json.loads(json_string)

    # Step 2: Create a new Purchase record
    new_purchase = Purchase(
        id=json_data.get('id'),
        admin_graphql_api_id=json_data.get('admin_graphql_api_id'),
        app_id=json_data.get('app_id'),
        browser_ip=json_data.get('browser_ip'),
        buyer_accepts_marketing=json_data.get('buyer_accepts_marketing'),
        cancel_reason=json_data.get('cancel_reason'),
        cancelled_at=datetime.fromisoformat(json_data['cancelled_at'].replace('Z', '+00:00')) if json_data.get('cancelled_at') else None,
        cart_token=json_data.get('cart_token'),
        checkout_id=json_data.get('checkout_id'),
        checkout_token=json_data.get('checkout_token'),
        client_details=json_data.get('client_details'),
        closed_at=datetime.fromisoformat(json_data['closed_at'].replace('Z', '+00:00')) if json_data.get('closed_at') else None,
        confirmation_number=json_data.get('confirmation_number'),
        confirmed=json_data.get('confirmed'),
        contact_email=json_data.get('contact_email'),
        created_at=datetime.fromisoformat(json_data['created_at'].replace('Z', '+00:00')) if json_data.get('created_at') else None,
        currency=json_data.get('currency'),
        current_subtotal_price=json_data.get('current_subtotal_price'),
        current_subtotal_price_set=json_data.get('current_subtotal_price_set'),
        current_total_additional_fees_set=json_data.get('current_total_additional_fees_set'),
        current_total_discounts=json_data.get('current_total_discounts'),
        current_total_discounts_set=json_data.get('current_total_discounts_set'),
        current_total_duties_set=json_data.get('current_total_duties_set'),
        current_total_price=json_data.get('current_total_price'),
        current_total_price_set=json_data.get('current_total_price_set'),
        current_total_tax=json_data.get('current_total_tax'),
        current_total_tax_set=json_data.get('current_total_tax_set'),
        customer_locale=json_data.get('customer_locale'),
        device_id=json_data.get('device_id'),
        discount_codes=json_data.get('discount_codes'),
        duties_included=json_data.get('duties_included'),
        email=json_data.get('email'),
        estimated_taxes=json_data.get('estimated_taxes'),
        financial_status=json_data.get('financial_status'),
        fulfillment_status=json_data.get('fulfillment_status'),
        landing_site=json_data.get('landing_site'),
        landing_site_ref=json_data.get('landing_site_ref'),
        location_id=json_data.get('location_id'),
        merchant_business_entity_id=json_data.get('merchant_business_entity_id'),
        merchant_of_record_app_id=json_data.get('merchant_of_record_app_id'),
        name=json_data.get('name'),
        note=json_data.get('note'),
        note_attributes=json_data.get('note_attributes'),
        number=json_data.get('number'),
        order_number=json_data.get('order_number'),
        order_status_url=json_data.get('order_status_url'),
        original_total_additional_fees_set=json_data.get('original_total_additional_fees_set'),
        original_total_duties_set=json_data.get('original_total_duties_set'),
        payment_gateway_names=json_data.get('payment_gateway_names'),
        phone=json_data.get('phone'),
        po_number=json_data.get('po_number'),
        presentment_currency=json_data.get('presentment_currency'),
        processed_at=datetime.fromisoformat(json_data['processed_at'].replace('Z', '+00:00')) if json_data.get('processed_at') else None,
        reference=json_data.get('reference'),
        referring_site=json_data.get('referring_site'),
        source_identifier=json_data.get('source_identifier'),
        source_name=json_data.get('source_name'),
        source_url=json_data.get('source_url'),
        subtotal_price=json_data.get('subtotal_price'),
        subtotal_price_set=json_data.get('subtotal_price_set'),
        tags=json_data.get('tags'),
        tax_exempt=json_data.get('tax_exempt'),
        tax_lines=json_data.get('tax_lines'),
        taxes_included=json_data.get('taxes_included'),
        test=json_data.get('test'),
        token=json_data.get('token'),
        total_discounts=json_data.get('total_discounts'),
        total_discounts_set=json_data.get('total_discounts_set'),
        total_line_items_price=json_data.get('total_line_items_price'),
        total_line_items_price_set=json_data.get('total_line_items_price_set'),
        total_outstanding=json_data.get('total_outstanding'),
        total_price=json_data.get('total_price'),
        total_price_set=json_data.get('total_price_set'),
        total_shipping_price_set=json_data.get('total_shipping_price_set'),
        total_tax=json_data.get('total_tax'),
        total_tax_set=json_data.get('total_tax_set'),
        total_tip_received=json_data.get('total_tip_received'),
        total_weight=json_data.get('total_weight'),
        updated_at=datetime.fromisoformat(json_data['updated_at'].replace('Z', '+00:00')) if json_data.get('updated_at') else None,
        user_id=json_data.get('user_id'),
        billing_address=json_data.get('billing_address'),
        customer=json_data.get('customer'),
        discount_applications=json_data.get('discount_applications'),
        fulfillments=json_data.get('fulfillments'),
        line_items=json_data.get('line_items'),
        payment_terms=json_data.get('payment_terms'),
        refunds=json_data.get('refunds'),
        shipping_address=json_data.get('shipping_address'),
        shipping_lines=json_data.get('shipping_lines')
    )

    # Add the new purchase record to the session and commit it to the database
    db.session.add(new_purchase)
    db.session.commit()

    return jsonify({'message': 'Purchase added successfully', 'purchase_id': new_purchase.id}), 201



@routes.route('/users', methods=['GET'])
def show_users():
    users = User.query.all()
    return render_template('index.html', users=users)

@routes.route('/checkouts')
def show_checkouts():
    checkouts = Checkout.query.all()  # Fetch all checkout records
    return render_template('checkouts.html', checkouts=checkouts)