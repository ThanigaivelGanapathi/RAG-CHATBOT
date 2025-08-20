
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
#, request
#, render_template

# from fastapi import FastAPI
# from fastapi.middleware.wsgi import WSGIMiddleware

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma, FAISS
import google_api_key.generativeai as genai

google_api_key = "AIzaSyCsA5TDatptsoQMLptfVNtaPJF1VXGaU3A"
genai.configure(api_key=google_api_key)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


@app.route("/ping")
def ping():
    user = ""
    loader = PyPDFLoader("attention.pdf")
    documents = loader.load()
    print(documents)
    # Chroma DB
    db = Chroma.from_documents(documents, GoogleGenerativeAIEmbeddings(model="models/embedding-001",
                                                                        google_api_key=google_api_key))
    user = "tell me the authors of attention is all you need"
    result = db.similarity_search(user)
    print(result[0].page_content)
    return "pong", 200


# @app.route("/ping")
# def ping():
#     print('hello')
#     return "pong", 200



@app.route("/upload", methods=["POST"])
def upload_pdf():
    print("hello")
    # try:
    #     # Get PDF bytes from request body
    #     pdf_bytes = request.data
    #
    #     # Save to file (optional)
    #     with open("received_file.pdf", "wb") as f:
    #         f.write(pdf_bytes)
    #
    #     return {"message": "PDF received successfully", "size": len(pdf_bytes)}
    # except Exception as e:
    #     return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)


# from flask import Flask, render_template
# from fastapi import FastAPI
# from fastapi.middleware.wsgi import WSGIMiddleware
#
# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_community.vectorstores import Chroma, FAISS
# import google_api_key.generativeai as genai
#
# google_api_key = "AIzaSyCsA5TDatptsoQMLptfVNtaPJF1VXGaU3A"
# genai.configure(api_key=google_api_key)
#
#
# # Flask app
# flask_app = Flask(__name__)
#
# @flask_app.route("/")
# def home():
#     user = ""
#     loader = PyPDFLoader("HR_POLICIES.pdf")
#     documents = loader.load()
#     print(documents)
#
#     # Chroma DB
#     db = Chroma.from_documents(documents, GoogleGenerativeAIEmbeddings(model="models/embedding-001",
#                                                                        google_api_key=google_api_key))
#     # user = "tell me the authors of attention is all you need"
#     result = db.similarity_search(user)
#     print(result[0].page_content)
#
#     return render_template("index.html", title="Flask + FastAPI App")
#
# # FastAPI app
# fastapi_app = FastAPI()
#
# @fastapi_app.get("/api/data")
# def get_data():
#     return {"message": "Hello from FastAPI API"}
#
# # Mount Flask into FastAPI
# app = fastapi_app  # Rename to 'app' for Uvicorn
# app.mount("/", WSGIMiddleware(flask_app))
