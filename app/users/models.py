from sqlalchemy import Computed
from sqlalchemy.orm import Mapped, mapped_column

from app.models import CustomBase, intpk, str_10, str_20, Base


class User(CustomBase):

    first_name: Mapped[str_10]
    last_name: Mapped[str_10]
    fullname: Mapped[str_20] = mapped_column(Computed("first_name || ' ' || last_name"), onupdate=True)


