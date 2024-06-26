from dependency_injector import containers, providers
from core_api.apps.tags.services.tags import TagService


class ServiceContainer(containers.DeclarativeContainer):
    tag_service = providers.Factory(TagService)


service_container = ServiceContainer()
