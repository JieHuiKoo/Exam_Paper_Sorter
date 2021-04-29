from PyPDF2 import PdfFileReader as pdfFR, PdfFileWriter as pdfFW, pdf, PdfFileMerger as pdfFM # For dealing with pdf
import os # For dealing with file directory

def obtain_pdfs():
    # Obtain current directory main.py program is in
    current_directory = os.getcwd()

    # location of all exam papers
    data_folder_directory = current_directory + "\Data"
    
    # Examine the folder and make a data structure
    data_folder = os.walk(data_folder_directory)

    # For every folder in the Data folder
    # Print and store in own data structure, exam_papers_collated = [file_directory, year, file_name]
    exam_papers_collated = []
    unwanted_words = ["Level", "PG", "UG", "Exam", "1", "2", "3", "4" ,"5", "6" ,"7", "8", "9", "0", " ", "-"]
    for year_folder in data_folder: # year_folder contains = [directory, list of subfolders, list of file names in year_folder]
        
        # === Obtain the year ===

        # Obtain folder directory
        folder_directory = year_folder[0]
        # Split by space
        split_folder_name = folder_directory.split(' ')
        # Obtain the last split, which is the year
        year = split_folder_name[-1]

        # For every paper in each year_folder
        for exam_paper_name in year_folder[2]:
            if ".pdf" not in exam_paper_name:
                continue

            exam_paper_directory = str(folder_directory)+"\\"+str(exam_paper_name)
            
            # Store the original exam paper name for future reference
            original_exam_paper_name = exam_paper_name.replace(".pdf", "")
            
            # === Clean the exam paper name ===
            # Remove last group of numbers, it is usually the module code
            exam_paper_name = exam_paper_name.rsplit(' ', 1)[0]
            # Check if exam_paper_name has unwanted_word
            for unwanted_word in unwanted_words:
                if unwanted_word in exam_paper_name:
                    # Clean the module name, remove all unwanted words
                    exam_paper_name = exam_paper_name.replace(unwanted_word, "")

            # convert all exam_paper_name to lowercase
            exam_paper_name = exam_paper_name.lower() + ".pdf"
            
            # Append the data into our own data structure [directory, year, cleaned exam paper name, original exam paper name]
            exam_papers_collated.append([exam_paper_directory, year, exam_paper_name.lower(), original_exam_paper_name])
            #print("Year: " + str(year) + " || " + "Paper: " + str(exam_paper_name).ljust(70) + " || " + str("Directory: "+ exam_paper_directory))
        #print("========")

    # Sort our data structure by file name => [file directory, year, file name, original exam paper name]
    exam_papers_collated.sort(key = lambda exam_papers_collated: exam_papers_collated[1], reverse=True)
    return exam_papers_collated
def export_pdf(data):
    # Obtain the current directory of where the main.py is stored
    current_directory = os.getcwd()

    # Generate the output directory
    output_directory = current_directory + str("\output")

    # If output directory does not exist, create it
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    progression_count = 1
    
    for exam_paper in data:
        print("Processing " + str(progression_count) + " of " + str(len(data)+1) + " || Year: " + exam_paper[1] + " || " + exam_paper[2])
        progression_count = progression_count + 1
        try:
            #print("Opening Existing")
            # Try to open the destination file. 
            exam_file = pdfFR(open(output_directory + "\\" + str(exam_paper[2]), 'rb'))

            # Open the file to be merged
            exam_file_to_merge = pdfFR(open(exam_paper[0], 'rb'))

            # Get number of pages
            num_of_pages = exam_file_to_merge.getNumPages()

            merger = pdfFM()
            # Merge it
            merger.append(exam_file)
            merger.append(exam_file_to_merge)

        # If not created, open the current file
        except IOError:
            #print("Creating New")
            exam_file = pdfFR(open(exam_paper[0], 'rb'))

            merger = pdfFM()

            # Merge the exam_file
            merger.append(exam_file)
        
        except:
            print("\n\n")
            print("Error" + "|| Year: " + exam_paper[1] + " || " + exam_paper[2])
            print("Try removing all bookmarks, embedded files and thumbnails.")
            print("You may use this tool. https://avepdf.com/en/remove-pdf-content")
            print("\n\n")

        # Export it to output
        merger.write(output_directory + '\\' + str(exam_paper[2]))
        merger.close()

# Obtain the data structure of exam papers
data = obtain_pdfs()

# Merge and export the pdfs
export_pdf(data)

print("Bubba <3 Wubba")