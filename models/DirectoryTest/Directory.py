from flask_sqlalchemy import SQLAlchemy

class Directory(db.Models):
  """Table of directory of all projects"""

  __tablename__ = "directory"
  
  