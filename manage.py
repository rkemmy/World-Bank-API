from flask_script import Manager, Server
from app import create_app, db
from app.data.models import Catalog, Metatype
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager



app = create_app('default')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app, db = db, Catalog = Catalog, Metatype = Metatype )

if __name__ == '__main__':
    manager.run()