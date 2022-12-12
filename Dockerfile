FROM continuumio/anaconda3:latest

RUN pip install pipenv

WORKDIR /app    

COPY requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8502

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["Flask_Diab_Pred_app.py"] 

