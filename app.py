from flask import Flask, jsonify, request

app = Flask(__name__)


def fibonacci(n):
    raise NotImplementedError("The Fibonacci method is not yet implemented.")


@app.route("/fibonacci", methods=["GET"])
def get_fibonacci():
    try:
        n = int(request.args.get("n", 10))  # Get the number of terms, default is 10
        if n <= 0:
            return jsonify({"error": "Please provide a positive integer for 'n'"}), 400
        fib_sequence = fibonacci(n)
        return jsonify(fib_sequence)
    except NotImplementedError as e:
        return jsonify({"error": str(e)}), 501
    except ValueError:
        return (
            jsonify(
                {"error": "Invalid input. Please provide a valid integer for 'n'."}
            ),
            400,
        )


if __name__ == "__main__":
    app.run(debug=True)
