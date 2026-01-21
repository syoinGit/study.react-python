from ..core.db import SessionLocal
from ..models import User, Game, Post

def main():
    db = SessionLocal()
    try:
        users = [User(name="Yuki"), User(name="Mina"), User(name="Kenta")]
        db.add_all(users)
        db.flush()

        games = [
            Game(name="Elden Ring", summary="高難度アクションRPG", genre="ARPG"),
            Game(name="Hades", summary="ローグライトアクション", genre="Roguelite"),
            Game(name="Stardew Valley", summary="農場生活シム", genre="Sim"),
        ]
        db.add_all(games)
        db.flush()

        posts = [
            Post(title="難しいけど最高", body="序盤きついが理解すると面白い。", screenshot_url="https://example.com/ss/01.png", created_user_id=users[0].id, game_id=games[0].id),
            Post(title="中毒性やばい", body="テンポが良く何回でも遊べる。", screenshot_url="https://example.com/ss/02.png", created_user_id=users[1].id, game_id=games[1].id),
            Post(title="癒やし枠", body="生活のリズムが気持ちいい。", screenshot_url="https://example.com/ss/03.png", created_user_id=users[2].id, game_id=games[2].id),
            Post(title="探索が神", body="寄り道がメインになる。", screenshot_url="https://example.com/ss/04.png", created_user_id=users[0].id, game_id=games[0].id),
            Post(title="成長が楽しい", body="負けても納得感がある。", screenshot_url="https://example.com/ss/05.png", created_user_id=users[1].id, game_id=games[0].id),
            Post(title="爽快感ある", body="短時間でも達成感が出る。", screenshot_url="https://example.com/ss/06.png", created_user_id=users[2].id, game_id=games[1].id),
            Post(title="雰囲気が好き", body="音と色のセンスが良い。", screenshot_url="https://example.com/ss/07.png", created_user_id=users[0].id, game_id=games[2].id),
            Post(title="おすすめ", body="万人向け寄りの完成度。", screenshot_url="https://example.com/ss/08.png", created_user_id=users[1].id, game_id=games[2].id),
            Post(title="下書き", body="後で追記予定のメモ。", screenshot_url="https://example.com/ss/09.png", created_user_id=users[2].id, game_id=None),
            Post(title="良作", body="地味に完成度が高い。", screenshot_url="https://example.com/ss/10.png", created_user_id=users[0].id, game_id=None),
        ]

        db.add_all(posts)
        db.commit()
        print("seed done")

    except Exception:
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    main()
