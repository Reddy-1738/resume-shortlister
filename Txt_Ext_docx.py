from docx import Document  

def extract_txt_from_docx(path):
  doc=Document(path)
  txt=[]
   
  for para in doc.paragraphs:
      txt.append(para.text)

  ext_txt="\n".join(txt).strip() 
  return ext_txt

doc_path="Resumes\PUNITH.docx"
print(extract_txt_from_docx(doc_path))