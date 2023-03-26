from flask import Flask, request
from src.domain.constants import Constants
from src.domain.decorators import api_response_handler
from src.application.reader import Reader
from src.application.writer import Writer

app = Flask(__name__)

root_document = {
    "name": "root_document",
    "text": "Some text here",
    "sections": [
        {
            "name": "subtitle_3",
            "text": "Text for title 3",
        },
        {
            "name": "subtitle_1",
            "text": "Text for title 1",
            "sections": [
                {
                    "name": "title_1",
                    "text": "Text for title 1",
                    "sections": []
                }
            ]
        }
    ]
}


@app.route("/")
def init():
    return {"hello": "API load correctly"}


@app.get("/document")
@api_response_handler
def get_document():
    __args = request.args.to_dict()
    api_manager = Reader(db=root_document)
    return api_manager.get_document(__args)

@app.post("/document")
@api_response_handler
def add_document():
    __args = request.args.to_dict()
    api_manager = Writer(db=root_document)
    return api_manager.add_document(__args)
