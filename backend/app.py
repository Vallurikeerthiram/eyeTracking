from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    gaze_data = data.get('gazeData')
    
    # Simple logic to check if the user covered most of the text
    if gaze_data and len(gaze_data) > 10:  # Example condition
        return jsonify({"text_read": True})
    else:
        return jsonify({"text_read": False})

if __name__ == "__main__":
    app.run(debug=True)
