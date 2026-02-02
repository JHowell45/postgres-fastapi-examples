from sqlmodel import Field, Relationship, SQLModel


class Album(SQLModel, table=True):
    id: int | None = Field(default=True, primary_key=True)
    name: int
    songs: list["Song"] = Relationship(back_populates="album")


class Song(SQLModel, table=True):
    __tablename__ = "songs"

    id: int | None = Field(default=None, primary_key=True)
    name: int
    length_in_secs: int

    album_id: int | None = Field(default=None, foreign_key="album.id")
    album: Album | None = Relationship(back_populates="songs")
