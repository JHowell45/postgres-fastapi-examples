import typer
from sqlalchemy.dialects.postgresql import insert
from sqlmodel import Session

from app.deps.db import engine
from app.models.music import Song

cli = typer.Typer(no_args_is_help=True)

SONGS = [
    ["Kubrick Stare", 199],
    ["Fuck Them All to Hell", 153],
    ["Shot Caller", 175],
    ["Can't Help Myself", 156],
    ["Clockworked", 180],
    ["Shocker", 211],
    ["Bodies in the Dark", 193],
    ["Can I have Your Autograph?", 173],
    ["You're Not That Guy", 171],
]


@cli.command()
def songs() -> None:
    models: list[dict] = []
    for song, length in SONGS:
        models.append(Song(name=song, length_in_secs=length).model_dump())
    with Session(engine) as session:
        stmt = insert(Song).values(models).on_conflict_do_update
