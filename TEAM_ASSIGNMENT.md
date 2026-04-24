# Phân Chia Công Việc - Data Pipeline Lab

## Thứ Tự Ưu Tiên (Để Tránh Xung Đột)

### 🎯 Bước 1: Lead Data Architect (LÀMS TRƯỚC TIÊN)
**Người phụ trách:** 👤 **Dương Hoàng Thái**  
**File:** `starter_code/schema.py`  
**Thời gian:** ~30 phút  
**Nhiệm vụ:**
- Định nghĩa các trường dữ liệu chung (Schema)
- Tạo Pydantic model để validate dữ liệu
- **KHÔNG CẦN** chờ ai khác

**Dependency:**
- ✅ Độc lập - có thể bắt đầu ngay

**Output cần có:**
```python
class DataRecord(BaseModel):
    # Các trường dữ liệu chuẩn cho cả PDF và Video
    ...
```

---

### 🎯 Bước 2: ETL Builder (CÓ THỂ BẮT ĐẦU SAU KHI ARCHITECT XONG)
**Người phụ trách:** 👤 **Nguyễn Thùy Linh**  
**File:** `starter_code/process_unstructured.py`  
**Thời gian:** ~40 phút  
**Nhiệm vụ:**
- Đọc dữ liệu từ PDF và Video metadata
- Làm sạch text (xóa header/footer bằng Regex)
- Map dữ liệu sang Schema chuẩn từ Bước 1

**Dependency:**
- 🔴 PHẢI CHỜ: `schema.py` (để import DataRecord)

**Các hàm cần:**
```python
def clean_pdf_text(text):
    # Xóa header/footer, noise
    ...

def map_pdf_to_schema(pdf_data):
    # Convert sang DataRecord
    ...

def map_video_to_schema(video_data):
    # Convert sang DataRecord
    ...
```

---

### 🎯 Bước 3: Observability Engineer (SAU BUILDER)
**Người phụ trách:** 👤 **Mạc Phương Nga**  
**File:** `starter_code/quality_check.py`  
**Thời gian:** ~30 phút  
**Nhiệm vụ:**
- Kiểm tra dữ liệu theo schema (validation)
- Phát hiện dữ liệu hỏng (ví dụ: doc2_corrupt.json)
- Loại bỏ bản ghi không hợp lệ
- Logging lỗi

**Dependency:**
- 🔴 PHẢI CHỜ: `schema.py` (để import DataRecord và validate)
- 🟡 NÊN CHỜ: `process_unstructured.py` (để test với dữ liệu đã được xử lý)

**Các hàm cần:**
```python
def validate_record(record: DataRecord) -> bool:
    # Kiểm tra dữ liệu hợp lệ
    ...

def quality_gate(records: List[DataRecord]) -> List[DataRecord]:
    # Filter dữ liệu hỏng, return chỉ dữ liệu tốt
    ...
```

---

### 🎯 Bước 4: DevOps Specialist (CUỐI CÙNG)
**Người phụ trách:** 👤 **Dương Hoàng Thái**  
**File:** `starter_code/orchestrator.py`  
**Thời gian:** ~20 phút  
**Nhiệm vụ:**
- Kết nối tất cả thành phần
- Lặp qua tất cả file trong `raw_data/`
- Chạy pipeline: read → process → quality_check → output
- Tạo file `processed_knowledge_base.json`

**Dependency:**
- 🔴 PHẢI CHỜ: Tất cả 3 file trên (schema, process, quality_check)

**Pseudo code:**
```python
def main():
    # 1. Đọc tất cả file từ raw_data/group_a_pdfs/ và group_b_videos/
    # 2. Gọi process_unstructured.py để transform
    # 3. Gọi quality_check.py để filter
    # 4. Merge tất cả vào list
    # 5. Lưu vào processed_knowledge_base.json
    ...
```

---

## Timeline Đề Xuất

| Giai Đoạn | Vai Trò | Người làm | Task | Thời Gian |
|-----------|--------|----------|------|----------|
| **Phase 1** | Architect | Dương Hoàng Thái | `schema.py` | 0:00 - 0:30 |
| **Phase 2** | Builder | Nguyễn Thùy Linh | `process_unstructured.py` | 0:30 - 1:10 |
| **Phase 3** | Observability | Mạc Phương Nga | `quality_check.py` | 1:10 - 1:40 |
| **Phase 4** | DevOps | Dương Hoàng Thái | `orchestrator.py` | 1:40 - 2:00 |
| **Kiểm tra** | Tất cả | `pytest tests/test_lab.py` | 2:00+ |

---

## Checklist Tránh Xung Đột

### Lead Data Architect - Dương Hoàng Thái ✓
- [ ] Tạo xong `schema.py`
- [ ] Commit / Push cho team biết
- [ ] Chia sẻ link API schema

### ETL Builder - Nguyễn Thùy Linh ✓
- [ ] Đã pull `schema.py` từ Architect
- [ ] Import thành công `from schema import DataRecord`
- [ ] Test `process_unstructured.py` với 1 file mẫu

### Observability Engineer - Mạc Phương Nga ✓
- [ ] Đã pull `schema.py` và `process_unstructured.py`
- [ ] Import thành công
- [ ] Test `quality_check.py` với dữ liệu từ Builder

### DevOps Specialist - Dương Hoàng Thái ✓
- [ ] Đã pull tất cả 3 file trên
- [ ] Import thành công
- [ ] `orchestrator.py` chạy xong → tạo file output

---

## Notes
- **Lưu ý**: Nếu làm song song (parallel), hãy đảm bảo các interface (tên hàm, tham số) được định nghĩa trước
- **Ghi chú**: Nếu Architect chưa xong, Builder có thể tạo schema tạm thời để test
- **Git workflow**: Sử dụng git branch riêng mỗi người để tránh merge conflict
