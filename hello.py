# Import the required modules
import PyPDF2 # For reading PDF files
import re # For regular expressions

# Open the PDF file in read mode
pdf_file = open("dataset.pdf", "rb")
# Source of dataset: https://sr.indianrailways.gov.in/cris//uploads/files/1659695525713-SR.pdf

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Create an empty list to store the station names
station_names = []


# Loop through each page of the PDF file
for page in range(num_pages):

    # Get the text of the current page
    page_text = pdf_reader.pages[page].extract_text()

    # Split the text by newline characters
    lines = page_text.split("\n")

    # Loop through each line of the text
    for line in lines:

        # Check if the line contains NSG 1 or 2 or 3 as category
        if re.search("NSG [123]", line):

            #remove numbers from beginning of line and text after and including "nsg" text
            cleaned_line = re.sub(r"^\d+|\sNSG.*$", "", line)

            #print each station name per line
            print(cleaned_line)

            # Append the station name to the list
            station_names.append(cleaned_line)

# Close the PDF file
pdf_file.close()

# Print the no of stations
print(len(station_names))