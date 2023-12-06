FROM python:3.9-slim
RUN git clone https://github.com/SewerLabs1/literouter
WORKDIR "literouter"
RUN apt-get update && \
    apt-get install python3
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 4000/tcp
ENV PORT 4000
ENV DEFAULT_MODEL gryphe/mythomist-7b
ENV OR_API_KEY os.environ/OR_API_KEY
CMD ["--port", "4000", "app.py"]
