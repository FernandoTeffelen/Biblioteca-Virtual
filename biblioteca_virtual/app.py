from biblioteca_virtual import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)