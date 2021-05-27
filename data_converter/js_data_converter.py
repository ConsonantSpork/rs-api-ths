from pyduk import Context, USE_GLOBAL_POLYFILL


REQUEST_FUNC = 'get_request'
RESPONSE_FUNC = 'parse_response'


class JSDataConverter:
    def __init__(self, source_code):
        self._engine = Context(USE_GLOBAL_POLYFILL)
        self._engine.run(source_code)

    def _construct_args(self, date, data_type):
        args = []
        if date is not None:
            args.append(f'"{date.isoformat()}"')
        if data_type is not None:
            args.append(f'"{data_type}"')
        return ', '.join(args)

    def _convert_bytearray(self, data):
        bytes_args = ', '.join(str(i) for i in data)
        return f'new Uint8Array({bytes_args})'

    def get_request(self, *, date=None, data_type=None):
        return self._engine.run(f'{REQUEST_FUNC}({self._construct_args(date, data_type)})')

    def parse_response(self, data, *, date=None, data_type=None):
        if isinstance(data, bytearray):
            data = self._convert_bytearray(data)
        args = data
        rest_args = self._construct_args(date, data_type)
        if rest_args:
            args += f', {rest_args}'
        return self._engine.run(f'{RESPONSE_FUNC}({args})')
