FROM mageai/mageai:latest

ARG PROJECT_NAME=ml_demo
ARG MAGE_CODE_PATH=/home/mage_code
ARG USER_CODE_PATH=${MAGE_CODE_PATH}/ml_demo

WORKDIR ${MAGE_CODE_PATH}

COPY ml_demo ml_demo

# Set the USER_CODE_PATH variable to the path of user project.
# The project path needs to contain project name.
ENV USER_CODE_PATH=${USER_CODE_PATH}

# Install custom Python libraries
RUN pip3 install -r ${USER_CODE_PATH}/requirements.txt
# # Install custom libraries within 3rd party libraries (e.g. dbt packages)
# RUN python3 /app/install_other_dependencies.py --path ${USER_CODE_PATH}

ENV PYTHONPATH="${PYTHONPATH}:/home/mage_code"

CMD ["/bin/sh", "-c", "/app/run_app.sh"]
