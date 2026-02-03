# use PowerShell instead of sh:

set shell := ["powershell.exe", "-c"]

alias cm := create-migration
alias stop := dev-stop

dev:
    docker-compose watch

dev-stop:
    docker-compose down

reload:
    docker-compose down
    docker-compose watch

create-migration message:
    docker-compose exec app alembic revision --autogenerate -m {{ message }}""

cli:
    docker-compose exec app python app/cli.py
