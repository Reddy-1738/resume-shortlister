import fitz 
from docx import Document

def extract_text(pdf_path):
    pdf = fitz.open(pdf_path)
    extracted_text=""
    

    for page in pdf:
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0]))

        for block in blocks:
            print(block[4])  
            print("----")
    return extracted_text



def extract_txt_from_docx(path):
  doc=Document(path)
  txt=[]
   
  for para in doc.paragraphs:
      txt.append(para.text)

  ext_txt="\n".join(txt).strip() 
  return ext_txt


file_path=input("Enter the file in pdf or docx only:")

try:
    path=file_path.split(".")[-1]
    if path=="pdf":
        extract_text(file_path)
        
    elif path=="docx":
        extract_txt_from_docx(file_path)
    else:
        print(f"Unsupported file type")
except Exception as e:
    print(f"Some error occurred:{e}")        

          
          




