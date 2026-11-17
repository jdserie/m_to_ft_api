"""Flask application for converting meters to international feet."""
import re
from decimal import Decimal, ROUND_HALF_UP

from flask import Flask, render_template, request

app = Flask(__name__)
METERS_PER_FOOT = Decimal('0.3048')
NUMBER = re.compile(r'[+-]?(?:[0-9]{1,12}(?:\.[0-9]{1,8})?|\.[0-9]{1,8})')


def convert(raw):
    raw = (raw or '').strip()
    if not NUMBER.fullmatch(raw):
        raise ValueError('Enter a decimal number with up to 12 whole digits and 8 decimal places.')
    meters = Decimal(raw)
    feet = (meters / METERS_PER_FOOT).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)
    return format(meters, 'f'), format(feet, 'f')


@app.get('/')
def base_page():
    raw = request.args.get('meters')
    if raw is None:
        return render_template('converter.html')
    try:
        meters, feet = convert(raw)
    except ValueError as error:
        return render_template('converter.html', value=raw, error=str(error)), 400
    return render_template('converter.html', value=meters, feet=feet)


@app.get('/meters/<int:meters>')
def km_to_fathoms(meters):
    return f'{meters} meters equals {meters * 3.28084} feet.'


@app.get('/api/convert')
def convert_api():
    try:
        meters, feet = convert(request.args.get('meters'))
    except ValueError as error:
        return {'error': str(error)}, 400
    return {'meters': meters, 'feet': feet}


if __name__ == '__main__':
    app.run()
