from typing import Any

from sqlalchemy import exc

from core_api.apps.tags.models import Tag
from core_api.apps.core.db import DBSession
from core_api.apps.core.error_codes import Errors
from core_api.apps.core.exceptions import TagAlreadyExistsError, TagNotFoundError


class TagService:
    async def create_tag(self, **kwargs: dict[Any, Any]) -> None:
        try:
            with DBSession() as session:
                new_tag = Tag(**kwargs)
                session.add(new_tag)
                session.commit()

                return {
                    "id": new_tag.id,
                    "name": new_tag.name,
                }

        except exc.IntegrityError:
            raise TagAlreadyExistsError(Errors.TAG_ALREADY_EXISTS.value)

    async def _get_by(self, **kwargs: dict[Any, Any]) -> tuple[Tag] | None:
        with DBSession() as session:
            tag = session.query(Tag).filter_by(**kwargs).first()
            if tag:
                return tag

            return None

    async def get_tag(self, tag_id: int) -> tuple:
        if tag := self._get_by(id=tag_id):
            return (
                tag.id,
                tag.name,
            )

        raise TagNotFoundError(Errors.TAG_NOT_FOUND.value)

    async def list_tags(self, **filters) -> list[int | str]:
        with DBSession() as session:
            query = session.query(Tag)

            for key, value in filters.items():
                query = query.filter(getattr(Tag, key) == value)

            tags = query.all()

            return [
                {
                    "id": tag.id,
                    "name": tag.name,
                }
                for tag in tags
            ]

    async def delete_tag(self, tag_id: str):
        with DBSession() as session:
            if tag := self._get_by(id=tag_id):
                session.delete(tag)
                session.commit()
            else:
                raise TagNotFoundError(Errors.TAG_NOT_FOUND.value)
