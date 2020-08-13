FROM continuumio/anaconda3:4.4.0
COPY . /c/Users/slage/Desktop/mydata/Code/Project/BankNote/Docker
EXPOSE 5000
WORKDIR /c/Users/slage/Desktop/mydata/Code/Project/BankNote/Docker
RUN pip install -r requirement.txt
CMD python flasgger_app.py