FROM python:3.9.0-slim AS dependencies
WORKDIR /
COPY poetry.lock pyproject.toml ./
ADD ./src /src

RUN apt-get update \
    && apt-get install -y build-essential libssl-dev libffi-dev curl \
    && python -m pip install 'poetry==1.1.4' \
    && poetry config virtualenvs.create false


FROM dependencies as development
ENV PYTHONPATH=/src
RUN poetry install \
    && apt-get remove -y build-essential \
    && apt -y autoremove \
    && rm poetry.lock

WORKDIR /src/service

CMD ["tomodachi", "run", "app.py"]


FROM dependencies as release
ENV PYTHONPATH=/src
RUN poetry install \
    && apt-get remove -y build-essential \
    && apt -y autoremove \
    && rm poetry.lock

WORKDIR /src/service

CMD ["tomodachi", "run", "app.py", "--production"]
