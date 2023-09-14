import requests
import json


class ConvertorValuta:
    @staticmethod
    def _get_rates(from_val: str, to_val: str) -> dict:

        """
        Запрашивает данные о двух веденных валютах со стороннего сервера, и проверяет,
         что обе валюты были найдены
        """

        response = requests.get(
            'https://openexchangerates.org/api/latest.json',
            params={
                'app_id': '41ae87d5920040f5b5667988ed2dd4f7',  # на рабочем проекте было бы в .env
                'symbols': f'{from_val},{to_val}'
            }
        )
        rates = json.loads(response.text)['rates']

        if len(rates) < 2:
            raise ValueError('Валюта не найдена')

        return rates

    def convert(self, from_val: str, to_val: str, value: float) -> float | int:

        """ Производит конвертацию валют """

        rates = self._get_rates(from_val, to_val)

        return (value / rates[from_val]) * rates[to_val]

