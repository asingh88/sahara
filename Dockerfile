from python:3.7-slim-buster
COPY src/requirement.txt requirement.txt
RUN pip install -r requirement.txt
COPY src/app.py app.py

CMD ["python", "app.py"]

