"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView

import graphene
from graphql_auth import mutations
from graphql_auth.schema import UserQuery, MeQuery
from django.views.decorators.csrf import csrf_exempt

from user.schema import AuthMutation, UserQuery
from menu.schema import MenuMutation, MenuQuery
from cart.schema import CartMutation, CartQuery
from order.schema import OrderMutation, OrderQuery

class Query(UserQuery, MenuQuery, CartQuery, OrderQuery, graphene.ObjectType):
    pass

class Mutation(AuthMutation, MenuMutation, CartMutation, OrderMutation, graphene.ObjectType):
   pass

schema = graphene.Schema(query=Query, mutation=Mutation)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema = schema))),
]
