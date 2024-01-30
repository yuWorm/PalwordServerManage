FROM python:3.11.6

WORKDIR /code

COPY Pipfile ./

RUN pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple && pip install pipenv && pipenv install

COPY . ./

EXPOSE 8080

CMD ["sh", "-c", "/code/run.sh"]