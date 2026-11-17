# Meters to Feet

A small Flask utility by Joshua Serie. Use the browser form or send a request to the JSON API.

```sh
python -m pip install -r requirements.txt
python -m flask --app m_to_ft run
```

Open [localhost:5000](http://localhost:5000/). The endpoint `GET /api/convert?meters=0.3048` returns `{"meters":"0.3048","feet":"1.000000"}`. Feet are rounded to six decimal places using the [NIST international foot definition](https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors). The original plain-text integer endpoint remains at `GET /meters/2`.

Run `python -m unittest` to verify the form, API, and original endpoint.

The [original Flask exercise](https://github.com/jdserie/m_to_ft_api/commit/cf852e64c7fd4a950fa15e77d96a6f34adfbf8b1) dates to April 2019. The AI-assisted portfolio refresh adds the browser app, JSON validation, and reproducible dependencies. Make a fresh virtual environment from `requirements.txt`.
