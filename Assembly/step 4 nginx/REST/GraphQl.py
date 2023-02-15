from graphene import ObjectType, String, Schema


class Query(ObjectType):
    hello = String(name=String(default_value='stranger'))
    goodbye = String()

    def resolve_hello(self, info, name):
        return f'Hello, {name}'

    def resolve_goodbye(self, info):
        return 'by'


schema = Schema(query=Query)
