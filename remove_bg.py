from rembg import remove
from PIL import Image
import io

# 입력 및 출력 경로 설정
input_path = '손흥민.jpg'
output_path = '손흥민_remove.png'  # PNG 포맷으로 변경해야 투명 배경 가능!

try:
    # 입력 이미지 업로드
    with open(input_path, 'rb') as inp_file:
        input_data = inp_file.read()
    
    # 배경 제거해서 바이너리 데이터가 나옴
    output_data = remove(input_data)
    
    # 바이너리 데이터 -> 이미지 데이터 변환
    output_image = Image.open(io.BytesIO(output_data))
    
    # PNG 형식으로 파일 저장
    output_image.save(output_path, format="PNG")
    print(f"Completed: {output_path}")

except Exception as e:
    print(f"ERROR: {e}")
