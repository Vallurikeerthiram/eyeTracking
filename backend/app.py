from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive gaze data
@app.route('/track', methods=['POST'])
def track():
    data = request.json
    gaze_data = data.get('gazeData')

    # Here you can add your logic to analyze gaze_data
    # Example: Check if gaze data covers a significant portion of the text
    if gaze_data and len(gaze_data) > 10:  # Example condition
        return jsonify({"text_read": True})
    else:
        return jsonify({"text_read": False})

if __name__ == "__main__":
    app.run(debug=True)
