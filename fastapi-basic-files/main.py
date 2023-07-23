import os
from fastapi import FastAPI

app = FastAPI()
base_dir = os.path.dirname(os.path.abspath(__file__))
