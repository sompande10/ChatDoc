import PyPDF2

def parse_pdf(uploaded_file):
    read_pdf = PyPDF2.PdfReader(uploaded_file)

    # Get the number of pages in the uploaded PDF
    num_pages = len(read_pdf.pages)

    # Create a list to store the extracted text from each page
    pdf_content = []

    extract = ""

    # Extract the text from each page
    for i in range(num_pages):
        page = read_pdf.pages[i]
        page_text = page.extract_text()
        extract+=page_text
        pdf_content.append(page_text)

    return extract