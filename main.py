from website import app

app = app.app

if __name__ == "__main__":
    app.run(debug=True, port=3000, use_reloader=True)

