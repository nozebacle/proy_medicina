coverage run --branch  --omit=*/.virtualenvs/*,*/migrations/*,*test_* -m pytest --verbose --emoji --html=htmlcov/report.html --self-contained-html 
coverage html