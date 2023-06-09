from contextlib import contextmanager
from api.models import session


@contextmanager
def transaction():
    try:
        yield
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
