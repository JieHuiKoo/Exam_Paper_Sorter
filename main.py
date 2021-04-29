from PyPDF2 import PdfFileReader as pdfFR, PdfFileWriter as pdfFW
import os

def merge_pdf(paths, output):
    pass

print(os.getcwd())

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
    unwanted_words = ["Level", "PG", "UG", "Exam"]
    for year_folder in data_folder: # year_folder contains = [directory, list of subfolders, list of file names in year_folder]
        
        # Obtain the year
        folder_directory = year_folder[0]
        # Split by space
        split_folder_name = folder_directory.split(' ')
        # Obtain the last split, which is the year
        year = split_folder_name[-1]

        # For every paper in each year_folder
        for exam_paper_name in year_folder[2]:
            exam_paper_directory = str(folder_directory)+"\\"+str(exam_paper_name)
            
            # Check if exam_paper_name has unwanted_word
            for unwanted_word in unwanted_words:
                if unwanted_word in exam_paper_name:
                    # Clean the module name
                    exam_paper_name = exam_paper_name.replace(unwanted_word, "")
                    
            exam_papers_collated.append([exam_paper_directory, year, exam_paper_name])
            #print("Year: " + str(year) + " || " + "Paper: " + str(exam_paper_name).ljust(70) + " || " + str("Directory: "+ exam_paper_directory))
        #print("========")

    return exam_papers_collated


data = obtain_pdfs()


data.sort(key = lambda data: data[2])
for i in data:
    print(i)