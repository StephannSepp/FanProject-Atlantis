from FanProject_Atlantis import create_app


if __name__ == '__main__':
    app = create_app(testing=True)
    app.run("localhost", 80, debug=True)
