from drf_spectacular.utils import extend_schema,OpenApiParameter,extend_schema_view

from drf_spectacular.types import OpenApiTypes

from .serializers import ProductSerializer
from .docstring import *
product_list_docs = extend_schema(
    responses = ProductSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name="category",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description = "the Category of products to retrive"
        ),
        OpenApiParameter(
            name="qty",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description = "the quantity of products to retrive"
        ),
    ]
)

product_viewset_docs = extend_schema_view(
    list = extend_schema(
        summary='list all products',
        description=LIST_DOCS
    ),
    retrieve = extend_schema(
        summary='retreve all products',
        description=RETRIEVE_DOCS
    ),
    create = extend_schema(
        summary='create all products',
        description=CREATE_DOCS
    ),
    update = extend_schema(
        summary='update all products',
        description=UPDATE_DOCS
    ),
    partial_update = extend_schema(
        summary='partial update all products',
        description=PARTIAL_UPDATE_DOCS
    ),
    destroy = extend_schema(
        summary='destroy all products',
        description=DELETE_DOCS
    ),
)