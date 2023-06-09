Generic single-database configuration.
```
> cd src
> .\venv\Scripts\activate (Windows) or source .\venv\bin\activate (macos)  ... 仮想環境に入る
> alembic upgrade head

```

Create revision
```
>alembic revision -m "new_revision"
```

Create revision from models
```
>alembic revision --autogenerate -m "Delete m_account"
```