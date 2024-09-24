from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize a Tic-Tac-Toe board
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"

def check_winner():
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] != "":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != "":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]
    
    return None

def is_draw():
    for row in board:
        if "" in row:
            return False
    return True

@app.route("/move", methods=["POST"])
def make_move():
    global current_player
    data = request.get_json()
    row = data["row"]
    col = data["col"]

    # Check if the move is valid
    if board[row][col] == "":
        board[row][col] = current_player

        # Check for a winner after the move
        winner = check_winner()
        if winner:
            return jsonify({"status": f"Player {winner} wins!"})

        # Check if it's a draw
        if is_draw():
            return jsonify({"status": "It's a draw!"})

        # Switch players
        current_player = "O" if current_player == "X" else "X"

        return jsonify({
            "status": "Move accepted",
            "board": board,
            "next_player": current_player
        })
    else:
        return jsonify({"status": "Invalid move. Spot already taken."}), 400

@app.route("/board", methods=["GET"])
def get_board():
    return jsonify({"board": board})

@app.route("/reset", methods=["POST"])
def reset_board():
    global board, current_player
    board = [["" for _ in range(3)] for _ in range(3)]
    current_player = "X"
    return jsonify({"status": "Game reset", "board": board})

if __name__ == "__main__":
    app.run(debug=True)
