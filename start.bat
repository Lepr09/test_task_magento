:: python -m pytest Tests/GoodsPrices_test.py -sv
:: python -m pytest Tests/Review_test.py -sv
:: python -m pytest -sv
python -m pytest -n 2 -sv
.\allure\bin\allure serve .\allure-results\