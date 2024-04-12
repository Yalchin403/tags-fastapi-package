from fastapi import APIRouter, HTTPException, status
from core_api.apps.tags.services.containers import service_container
from core_api.apps.tags.schemas import TagSerializer, TagInSerializer

tag_service = service_container.tag_service()
router = APIRouter()


@router.get(
    "/tags",
    tags=["tags"],
    response_model=list[TagSerializer],
    status_code=status.HTTP_200_OK,
)
async def list_keys():
    try:
        return await tag_service.list_tags()

    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err.args))


@router.post(
    "/tags",
    tags=["tags"],
    response_model=TagSerializer,
    status_code=status.HTTP_201_CREATED,
)
async def create_tag(tag_in: TagInSerializer):
    try:
        return await tag_service.create_tag(name=tag_in.name)
    except ValueError as err:
        raise HTTPException(status_code=400, detail=str(err.args))
