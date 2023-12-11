
pip install flask gunicorn

gunicorn -w 4 -b 0.0.0.0:8000 --reload Flask:app

