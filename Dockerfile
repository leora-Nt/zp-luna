FROM python:3.9.10

WORKDIR /luna
COPY . /luna
 
RUN pip install -r requirements.txt
 
ENTRYPOINT ["python"]
CMD ["-m", "luna"]
