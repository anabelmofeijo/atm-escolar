from app import FastAPI, CORSMiddleware
from app.routers import (
    payment_router,
    student_router,
    exam_router,
    proof
)
from app.core.config import Base, engine
from app.models import (
    payment_model,
    student_model,
    exam_model,
    monthly_model
)


app = FastAPI(title="ATM Escolar", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(student_router.router, prefix="/api/v1/student", tags=["student"])
app.include_router(payment_router.router, prefix="/api/v1/payment", tags=["payment"])
app.include_router(exam_router.router, prefix="/api/v1/exam", tags=["exam"])
app.include_router(proof.router, prefix="/api/v1/proof", tags=["proof"])


@app.get("/")
async def start():
    return {"message": "API is running"} 