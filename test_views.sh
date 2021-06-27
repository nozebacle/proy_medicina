coverage run --branch  --omit=*/.virtualenvs/*,*/migrations/* -m pytest --verbose --emoji --html=htmlcov/report.html --self-contained-html rubricas/tests_views/*
coverage html