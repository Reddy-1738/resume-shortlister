import fitz  

def extract_text(pdf_path):
    pdf = fitz.open(pdf_path)
    extracted_text = ""  

    for i, page in enumerate(pdf, start=1):
        extracted_text += f"Page {i}\n"
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0]))  

        for block in blocks:
            extracted_text += block[4] + "\n----\n"  

    return extracted_text  

pdf_path = "My cv.pdf"  
text = extract_text(pdf_path)
print(text)  
