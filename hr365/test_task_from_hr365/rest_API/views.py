from rest_framework.views import APIView
from rest_framework.response import Response
from .valute_convertor import ConvertorValuta


convertor_valuta = ConvertorValuta()


class ConvertAPIView(APIView):
    @staticmethod
    def _validate_get_data(from_val, to_val, value):

        try:
            float(value)
        except ValueError:
            raise ValueError("некоректно указанно количество конвертируемой валюты")

        if len(from_val) != 3 or len(to_val) != 3:
            raise ValueError(
                'Некоректно указан буквенный код валюты, должен состоять из 3 символов'
            )

        if not from_val.isalpha() or not to_val.isalpha():
            raise ValueError('код должен быть указан в латинскими буквами')

    def get(self, request, *args, **kwargs):

        from_val = request.GET.get('from', None)
        to_val = request.GET.get('to', None)
        value = request.GET.get('value', None)

        try:
            self._validate_get_data(from_val, to_val, value)
        except ValueError as e:
            return Response({'detail': str(e)})

        value = float(value)

        try:
            convert_value = convertor_valuta.convert(from_val, to_val, value)
        except ValueError as e:
            return Response({'detail': str(e)})

        return Response({convert_value})

