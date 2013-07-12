from pyramid.config import Configurator
from sqlalchemy import engine_from_config

from .models import (
    DBSession,
    Base,
    )


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)

    # Application routes
    config.add_route('home', '/')

    # Raster API
    config.add_route('raster_api_v1', '/api/raster/1*traverse')
    config.add_route('raster_api', '/api/raster*traverse')

    # Point API
    config.add_route('point_api_v1', '/api/point/1*traverse')
    config.add_route('point_api', '/api/point*traverse')

    # Base API (API Collection)
    config.add_route('api', '/api*traverse')

    config.scan()
    return config.make_wsgi_app()
