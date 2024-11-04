from flask import Flask, request, jsonify, render_template
from brolang_interpreter import execute_command  # Import the Brolang interpreter function

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run", methods=["POST"])
def run_code():
    code = request.json.get("code")
    output = []

    # Split code into lines and execute each line
    for line in code.strip().splitlines():
        try:
            result = execute_command(line)
            if result is not None:
                output.append(str(result))
        except Exception as e:
            output.append(f"that's a {type(e).__name__}, bro")

    return jsonify({"output": "\n".join(output)})

if __name__ == "__main__":
    app.run(debug=True)
