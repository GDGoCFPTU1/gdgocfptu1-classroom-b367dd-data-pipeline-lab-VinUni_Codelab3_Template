from pydantic import BaseModel, Field

# ==========================================
# ROLE 1: LEAD DATA ARCHITECT
# ==========================================

class UnifiedDocument(BaseModel):
    """
    Hệ thống cần 6 trường thông tin chuẩn (document_id, source_type, author, category, content, timestamp). 
    TODO: Khai báo các trường với kiểu dữ liệu str ở dưới.
    """
    # Khai báo các trường ở đây...
    document_id: str = Field(..., description="ID chuẩn hóa của tài liệu hoặc video")
    source_type: str = Field(..., description="Nguồn dữ liệu sau harmonization, ví dụ PDF hoặc Video")
    author: str = Field(..., description="Tác giả hoặc người tạo nội dung")
    category: str = Field(..., description="Nhóm chủ đề chuẩn hóa của nội dung")
    content: str = Field(..., description="Nội dung chính đã được làm sạch để đưa vào knowledge base")
    timestamp: str = Field(..., description="Mốc thời gian gốc của tài liệu/video dưới dạng chuỗi")
