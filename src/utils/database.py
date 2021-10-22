from flask_sqlalchemy import SQLAlchemy

# To avoid circular dependencies
# database variable was taken out
# in his own file.
db = SQLAlchemy()