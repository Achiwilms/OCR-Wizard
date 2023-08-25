# PDF_OCR

A shell script that use [OCRmyPDF](https://github.com/ocrmypdf/OCRmyPDF) to perform OCR on all PDFs in a folder.

## Environment 

1. Install OCRmyPDF, following the instructions in [Installing OCRmyPDF](https://ocrmypdf.readthedocs.io/en/latest/installation.html). 
For Windows users, I recommend to first install Windows Subsystem for Linux ([Installing WSL](https://learn.microsoft.com/en-us/windows/wsl/install)) and then install OCRmyPDF on WSL using one-liner command, `apt install ocrmypdf`. It's much simpler.
2. Install languages supported in this shell script, "Chinese (Traditional)" and "Chinese (Simplified)", following the instructions in [Install language pack](https://ocrmypdf.readthedocs.io/en/latest/languages.html). If you are Debian and Ubuntu user the commands are: 
```bash
sudo apt-get install tesseract-ocr-chi-tra
sudo apt-get install tesseract-ocr-chi-sim
```

## Usage
1. Clone or download this repository
2. Move to the repo's directory.
```bash
cd /path/to/directory/
```
3. Place the PDF files you want to OCR to folder `pdf_original`
4. Grant Execute Permission
```bash
chmod +x OCR.sh
```
4. Run `OCR.sh`
```bash
./OCR.sh
```
5. An user interface should appear. 
```bash
Options:
1. English
2. Chinese (Traditional) + English
3. Chinese (Simplified) + English
-----------------------------------
For Wei Chuan Dragons.pdf
Enter your choice (1-3):
```
6. Enter the language for each PDF file.  
7. You can find the OCR-ed PDF file in the folder `pdf_OCR`. 


## Contributing

Feel free to add more language options. Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
