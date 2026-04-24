from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================


class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp).
    """

    document_id: str = Field(
        ..., description="Mã định danh duy nhất của tài liệu (từ docId hoặc video_id)"
    )
    source_type: str = Field(
        ..., description="Định dạng nguồn dữ liệu (ví dụ: 'PDF' hoặc 'Video')"
    )
    author: str = Field(
        default="Unknown",
        description="Tên tác giả hoặc người tạo (từ authorName hoặc creator_name)",
    )
    category: str = Field(
        default="Uncategorized", description="Phân loại nội dung tài liệu"
    )
    content: str = Field(
        ..., description="Nội dung chính đã làm sạch (từ extractedText hoặc transcript)"
    )
    timestamp: str = Field(
        ...,
        description="Thời gian tạo hoặc xuất bản (từ createdAt hoặc published_timestamp)",
    )
