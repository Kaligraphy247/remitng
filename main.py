from website import app

app = app.app
c= 0
if __name__ == "__main__":
    app.run(debug=True, port=3000, use_reloader=True)

# print(app.app)