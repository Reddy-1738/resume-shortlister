import fitz  

def extract_text(pdf_path):
    pdf = fitz.open(pdf_path)
    extracted_text = ""  

    for page in pdf:
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0]))  

        for block in blocks:
           print(block[5])
           print("----")

    return extracted_text  

pdf_path = "My cv.pdf"  
text = extract_text(pdf_path)
print(text)  
