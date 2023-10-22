# Download OCRmyPDF on Windows

#### Step1. Open Windows PowerShell as Administrator

#### Step2. Download Chocolatey
Run the following command, 

```bash
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))
```

#### Step2. Download Required Packages Using Chocolatey
```bash
choco install --pre tesseract
```

```bash
choco install ghostscript
```
```bash
choco install pngquant
```

#### Step3. Download OCRmyPDF Using PIP
```bash
python -m pip install ocrmypdf
```

#### Step4. Download Required Languages

 Download 
 - `chi_tra.traineddata`
 - `chi_sim.traineddata`
 - `jpn.traineddata`
 - `deu.traineddata`
 - `spa.traineddata` 
 
 from https://github.com/tesseract-ocr/tessdata/ and place it in `C:\\Program Files\\Tesseract-OCR\\tessdata` (or wherever Tesseract OCR is installed).

 ---
 That's it. You have successfully setup OCRmyPdf on Windows!