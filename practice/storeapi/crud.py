from fastapi import HTTPException
from sqlalchemy.orm import Session

from storeapi.models import Comment, Post
from storeapi.schemas import CommentIn, UserPostIn


def get_post_with_comments(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    # query(entities)
    # stmt = select(Post).order_by(Post.id).offset(skip).limit(limit)
    # return db.execute(stmt).scalars().all()
    # or
    # db.qurey(Post).offset(skip).limit(limit).all()
    return db.query(Post).order_by(Post.id.desc()).offset(skip).limit(limit)


def create_post(db: Session, post: UserPostIn):
    # print(post.model_dump())
    db_post = Post(**post.model_dump())

    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def get_comments_on_post(db: Session, post_id: int, skip: int = 0, limit: int = 10):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="게시물이 존재하지 않습니다")

    return db.query(Comment).filter(Comment.post_id == post.id).all()


def create_post_comment(db: Session, comment: CommentIn, post_id: int):
    post = db.query(Post).where(Post.id == post_id)

    if not post:
        raise HTTPException(status_code=404, detail="게시물이 존재하지 않습니다")

    db_comment = Comment(**comment.model_dump(), post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment
