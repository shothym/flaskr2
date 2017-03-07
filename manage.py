from __future__ import print_function
from flask_script import Server, Manager
from flaskr import app, db

manager = Manager(app)
manager.add_command('runserver', Server(host='0.0.0.0', port=5000))

@manager.command
def init_db():
    db.create_all()

if __name__ == '__main__':
    manager.run()
