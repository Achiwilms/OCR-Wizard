#!/bin/bash

# path to orignal PDF dir
path_ori="./pdf_original"

# path to OCR PDF dir
path_ocr="./pdf_ocr/"

# Choose language
echo "Options:"
echo "1. English"
echo "2. Chinese (Traditional) + English"
echo "3. Chinese (Simplified) + English"

# language array
lng_array=()
for file_ori in "$path_ori"/*; do
    # file type
    file_type=$(file -b --mime-type "$file_ori")

    # PDF file
    if [ "$file_type" == "application/pdf" ]; then
        # get the filename without the path
        file_ocr=$(basename "$file_ori")

        # enter language
        echo "-----------------------------------"
        echo "For ""$file_ocr"
        read -p "Enter your choice (1-3): " option
        echo "-----------------------------------"
        
        # Add the option to the array
        lng_array+=("$option")
    fi
done

# counter (used for array element access)
counter=0

# iterate through the original PDF dir
for file_ori in "$path_ori"/*; do
    # file type
    file_type=$(file -b --mime-type "$file_ori")

    # OCR PDF file 
    if [ "$file_type" == "application/pdf" ]; then
        # get the filename without the path
        file_ocr=$(basename "$file_ori")

        # message
        echo "ᕦ(･ㅂ･)ᕤ"
        echo "Working on ""$file_ocr"
        echo "=========================="

        # add OCR to the filename
        file_ocr="OCR_""$file_ocr"

        # add path to OCR PDF dir
        file_ocr="$path_ocr""$file_ocr"

        # OCR the file!
        case ${lng_array[$counter]} in
            1)
                ocrmypdf -l eng "$file_ori" "$file_ocr" --skip-text
                ;;
            2)
                ocrmypdf -l chi_tra "$file_ori" "$file_ocr" --skip-text
                ;;
            3)
                ocrmypdf -l chi_sim "$file_ori" "$file_ocr" --skip-text
                ;;
            *)
                echo "Invalid option. Please choose a valid option (1-3)."
                ;;
        esac        
        
        # increment the counter
        ((counter++))
        echo "=========================="
    fi
done
