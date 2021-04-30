## Exam_Paper_Sorter

Sorts Durham University's collection of law exam papers by module instead of year, and merges them into a single PDF by module.

# Setup
1. pip install pypdf2
1. Please put a folder called "Data" in the same folder as where main.py is located. "Data" must have sub-folders containing exam papers.
1. "Data" MUST have sub folders named in the following format:
   1. "XXX 2010" where XXX can appear an arbitrary number of times.
1. Delete the folder "output" if it exists.
1. Program will output pdf files in a folder named "output".

**NOTE**

PDF file names (Module name of pdf) must be the **exact** same for all PDFs of the same module.
