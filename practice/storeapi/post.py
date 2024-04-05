from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from storeapi import crud
from storeapi.deps import get_db
from storeapi.schemas import (
    Comment,
    CommentIn,
    UserPost,
    UserPostIn,
)

router = APIRouter(prefix="/posts")


@router.get("/", response_model=List[UserPost])
def get_all_posts(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = crud.get_posts(db)
    return posts


@router.get("/{post_id}", response_model=UserPost)
def get_post_with_commnets(post_id: int, db: Session = Depends(get_db)):
    post = crud.get_post_with_comments(db, post_id=post_id)
    return post


@router.post("/", response_model=UserPost)
def create_post(post: UserPostIn, db: Session = Depends(get_db)):
    db_post = crud.create_post(db, post)
    return db_post


@router.get("/{post_id}/comments", response_model=List[Comment])
def get_comments_for_post(post_id: int, db: Session = Depends(get_db)):
    commnets = crud.get_comments_on_post(db, post_id=post_id)
    return commnets


@router.post("/{post_id}/comments", response_model=Comment)
def create_comment_for_post(
    post_id: int, comment: CommentIn, db: Session = Depends(get_db)
):
    return crud.create_post_comment(db, comment=comment, post_id=post_id)
