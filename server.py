from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/send_log', methods=['POST'])
def receive_log():
    try:
        # Log the incoming request data
        logging.debug(f"Received request data: {request.json}")

        encrypted_log = request.json.get('log')
        if not encrypted_log:
            raise ValueError("No log data provided.")

        # Assume you have a decryption function
        log_content = decrypt_log(encrypted_log)

        # Process the log content (e.g., save to a file)
        with open("logged_data.txt", "a") as f:
            f.write(log_content + "\n")
        
        return jsonify({"message": "Log received", "status": "success"})
    
    except Exception as e:
        logging.error(f"Error processing log: {e}")
        return jsonify({"message": str(e), "status": "error"}), 500

def decrypt_log(encrypted_log):
    # Your decryption logic here
    return encrypted_log  # Modify this as per your logic

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
