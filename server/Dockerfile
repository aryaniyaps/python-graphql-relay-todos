ARG PYTHON_BASE=3.12.4-slim
# build stage
FROM python:$PYTHON_BASE AS builder

# install PDM
RUN pip install -U pdm
# disable update check
ENV PDM_CHECK_UPDATE=false

# copy files
COPY pyproject.toml pdm.lock ./project/
COPY ./app ./project/app

# install dependencies and project into the local packages directory
WORKDIR /project
RUN pdm install --check --prod --no-editable


# production stage
FROM python:$PYTHON_BASE

COPY --from=builder /project/.venv/ /project/.venv
ENV PATH="/project/.venv/bin:$PATH"
# set command/entrypoint, adapt to fit your needs
COPY app ./project/app
WORKDIR /project
CMD ["python", "app/server.py"]
