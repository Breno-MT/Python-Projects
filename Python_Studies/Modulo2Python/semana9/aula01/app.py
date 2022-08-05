import click

from flask.cli import with_appcontext

from src.app import create_app
from src.app.utils import populate_db
from src.app.db import db

app = create_app()

@click.command(name='populate_db')
@with_appcontext
def call_command():
    populate_db()

app.cli.add_command(call_command)

@click.command(name='delete_tables')
@with_appcontext
def delete_tables():
  db.drop_all()


app.cli.add_command(call_command)
app.cli.add_command(delete_tables)


if __name__ == "__main__":
    app.run(debug=True)

