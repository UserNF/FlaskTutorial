from website import create_app #when you import the name of the folder you can import anything you find in that folder

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
