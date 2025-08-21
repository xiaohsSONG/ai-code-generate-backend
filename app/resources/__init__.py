from flask_restful import Resource,reqparse


class CommonResource(Resource):
    """通用资源类，所有资源类可以继承此类"""
    allow_methods = []

    def get_parser_args(self,configs):
        parser = reqparse.RequestParser()
        for config in configs:
            parser.add_argument(
                config['key'],
                type=config.get('type',str),
                required=config.get('required',False),
                help=config.get('help',None),
                action=config.get('action','store'),
                location=config.get('location', ('json', 'values',)),
                default=config.get('default',None),
            )
        return parser.parse_args()