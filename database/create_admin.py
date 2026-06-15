from database.session import SessionLocal
from database.models import User

from auth.password_utils import hash_password


db = SessionLocal()

existing = (
    db.query(User)
    .filter(User.username == "admin")
    .first()
)

if not existing:

    admin = User(
        username="admin",
        password=hash_password("Admin@123"),
        role="admin",
        is_active=True
    )

    db.add(admin)
    db.commit()

    print("Admin user created.")

else:
    print("Admin already exists.")

db.close()