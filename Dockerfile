FROM python:3.8
ADD knights.py /
ENV DIMENSION 30
CMD [ "python3.8", "./knights.py" ]