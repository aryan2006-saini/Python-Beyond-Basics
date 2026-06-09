from fastapi import FastAPI
from app.routes.issues import router as issues_router
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Issue Tracker API",
    version="1.0.0"
)

app.include_router(issues_router)
app.middleware("http")(timing_middleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins =['*'],
    allow_credentials=True,
    allow_methods = ['*'],
    allow_headers = ['*'],
    )

@app.get("/")
def root():
    return {"message": "Issue Tracker API is running"}

# from fastapi import FastAPI
# from app.routes.issues import router as issues_router

# app = FastAPI()

# # items = [
# #     {"id":1, "name":"Item-One"},
# #     {"id":2, "name":"Item-Two"},
# #     {"id":3, "name":"Item-Three"}
# # ]

# # # GET Request method
# # @app.get("/health")
# # def health_check():
# #     return {"status": "ok"}

# # @app.get("/items")
# # def get_items():
# #     return items

# # # single item by id
# # @app.get("/items/{item_id}")
# # def get_item(item_id: int):
# #     for item in items:
# #         if item["id"]==item_id:
# #             return item
# #     return {"error":"Item not found"}

# # @app.get("/items/")
# # def read_items(skip: int=0, limit: int = 10):
# #     return {"skip":skip, "limit":limit}

# # # POST request method
# # @app.post("/items")
# # def create_item(item:dict):
# #     items.append(item)
# #     return item

# app.include_router(issues_router)

