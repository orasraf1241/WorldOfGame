FROM python:3.8
COPY . /opt/app
WORKDIR /opt/app
RUN pip install -r requirements.txt
EXPOSE 8777
CMD ["python","/app/test/e2e.py"]