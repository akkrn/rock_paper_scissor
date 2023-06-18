FROM python:3.10
WORKDIR /rock_paper_scissors
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["python", "bot.py"]
