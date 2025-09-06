import io
from markitdown import MarkItDown


def extract_text_from_pdf(file_bytes: bytes) -> str:
    md = MarkItDown(ocr_enabled=True, preserve_tables=True)
    file_stream = io.BytesIO(file_bytes)  # wrap bytes into BinaryIO
    result = md.convert_stream(file_stream)
    return result.text_content
