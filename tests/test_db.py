from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='Donald Trump',
        email='trump@email.com',
        password='trumpSecret',
    )

    session.add(user)
    session.commit()

    result = session.scalar(
        select(User).where(User.email == 'trump@email.com')
    )
    assert user.id == 1
    assert result.username == 'Donald Trump'
    # assert user.username == 'Donald Trump'
