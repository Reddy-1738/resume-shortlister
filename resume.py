import fitz 

def extract_text(pdf_path):
    pdf = fitz.open(pdf_path)
    

    for i, page in enumerate(pdf, start=1):
        print(f"Page {i}") 
        blocks = page.get_text("blocks")
        blocks.sort(key=lambda b: (b[1], b[0]))

        for block in blocks:
            print(block[4])  
            print("----")
          

    

pdf_path = "My cv.pdf"  
text = extract_text(pdf_path)
print(text)
