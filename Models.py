from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

db = SQLAlchemy()

class UserTabel(db.Model):
    ID: Mapped[int] = mapped_column(primary_key=True)
    userName: Mapped[str] = mapped_column(unique=True)
    passWord: Mapped[str] = mapped_column()
    License: Mapped[str] = mapped_column(default="Allowed")
    Token: Mapped[int] = mapped_column(default=100)
    friends: Mapped[int] = mapped_column(default=0)
    Date:Mapped[str] = mapped_column(default=f"{datetime.now().year}:{datetime.now().month}:{datetime.now().day}")