FROM python:3.11-slim

WORKDIR /app

COPY ./src/ /app

COPY ./pyproject.toml /code/pyproject.toml
RUN pip install /code/.

EXPOSE 8501

CMD ["sh", "entrypoint.sh"]