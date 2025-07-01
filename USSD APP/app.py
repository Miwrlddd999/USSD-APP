from flask import Flask, request
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_user",
        password="your_password",
        database="your_database"
    )

@app.route('/ussd', methods=['POST'])
def ussd():
    session_id = request.form.get('sessionId')
    service_code = request.form.get('serviceCode')
    phone_number = request.form.get('phoneNumber')
    text = request.form.get('text', '')

    user_response = text.strip().split("*")

    if text == "":
        response = "CON Welcome to Academic Info\n"
        response += "1. View Profile\n"
        response += "2. Check GPA\n"
        response += "3. View Fees Balance\n"
        response += "4. Exit"

    elif text == "1":
        response = "CON Enter your index number:"

    elif len(user_response) == 2 and user_response[0] == "1":
        index = user_response[1].strip().upper()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, program FROM students WHERE index_number = %s", (index,))
        result = cursor.fetchone()
        conn.close()

        if result:
            name, program = result
            response = f"END Profile for {index}:\n{name}\nProgram: {program}"
        else:
            response = f"END No record found for {index}"

    elif text == "2":
        response = "CON Enter your index number:"

    elif len(user_response) == 2 and user_response[0] == "2":
        index = user_response[1].strip().upper()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT gpa FROM students WHERE index_number = %s", (index,))
        result = cursor.fetchone()
        conn.close()

        if result:
            gpa = result[0]
            response = f"END GPA for {index}: {gpa}"
        else:
            response = f"END No GPA record found for {index}"

    elif text == "3":
        response = "CON Enter your index number:"

    elif len(user_response) == 2 and user_response[0] == "3":
        index = user_response[1].strip().upper()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT fees_paid, fees_outstanding FROM students WHERE index_number = %s", (index,))
        result = cursor.fetchone()
        conn.close()

        if result:
            paid, outstanding = result
            response = f"END Fees Paid: GHS {paid:.2f}\nOutstanding: GHS {outstanding:.2f}"
        else:
            response = f"END No fee record found for {index}"

    elif text == "4":
        response = "END Thank you for using Academic Info"

    else:
        response = "END Invalid option"

    return response, 200, {'Content-Type': 'text/plain'}

if __name__ == '__main__':
    app.run(debug=True)