from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
from PyPDF2 import PdfReader
import pytesseract
import tempfile
import os

router = APIRouter()

def extract_text_ocr(file_path):
    try:
        image = Image.open(file_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        return f"OCR error: {str(e)}"

def read_image_metadata(file_path):
    try:
        image = Image.open(file_path)
        exif_data = image.getexif()
        if not exif_data:
            return {"message": "No metadata found (suspicious)"}
        return {str(tag): value for tag, value in exif_data.items()}
    except Exception as e:
        return {"error": str(e)}

def read_pdf_metadata(file_path):
    try:
        reader = PdfReader(file_path)
        metadata = reader.metadata
        return {key: str(value) for key, value in metadata.items() if value}
    except Exception as e:
        return {"error": str(e)}

@router.post("/check-proof")
async def check_proof(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=f"_{file.filename}") as temp:
        temp.write(await file.read())
        temp_path = temp.name

    extension = os.path.splitext(file.filename)[-1].lower()
    result = {}

    try:
        if extension in [".jpg", ".jpeg", ".png"]:
            result["metadata"] = read_image_metadata(temp_path)
            result["text"] = extract_text_ocr(temp_path)
        elif extension == ".pdf":
            result["metadata"] = read_pdf_metadata(temp_path)
            result["text"] = "OCR not applied to PDF. Please convert to image."
        else:
            raise HTTPException(status_code=400, detail="File type not supported.")

        result["status"] = "Suspicious" if "Photoshop" in str(result["metadata"]) else "Not suspicious"

        return JSONResponse(content=result)

    finally:
        os.remove(temp_path)