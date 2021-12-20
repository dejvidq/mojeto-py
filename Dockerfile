FROM python:3.10.1-slim-bullseye

# setup pytest user
RUN adduser --disabled-password --gecos "" --uid 7357 pytest
COPY ./ /home/pytest
WORKDIR /home/pytest
RUN chown -R pytest:pytest /home/pytest
RUN chmod 755 /home/pytest
ENV MOJETO_CONFIG_LOCATION=/tmp/mojeto

# setup the python and pytest environments
RUN pip install --upgrade pip setuptools pytest coverage[toml]
RUN pip install --upgrade -r requirements.txt
RUN python setup.py develop

# setup entry point
USER pytest
ENTRYPOINT ["coverage"]
