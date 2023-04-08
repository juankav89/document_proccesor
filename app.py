from flask import Flask, request
from src.domain.constants import Constants
from src.domain.decorators import api_response_handler
from src.application.reader import Reader
from src.application.writer import Writer

app = Flask(__name__)

virtual_db = {
    "root_document": {
        "name": "root_document",
        "text": "Some text here",
        "sections": [
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
            },
            {
                "name": "subtitle_2",
                "text": "Text for Subtitle 2",
                "sections": []
            }
        ]
    }
}


@app.route("/")
def init():
    return {"hello": "API load correctly"}


@app.get("/document")
@api_response_handler
def get_document():
    __args = request.args.to_dict()
    api_manager = Reader(db=virtual_db)
    return api_manager.get_document(__args)

@app.post("/document")
@api_response_handler
def add_document():
    __args = request.get_json()
    api_manager = Writer(db=virtual_db)
    api_manager.add_document(__args)
    print(virtual_db)
    return "ok"
