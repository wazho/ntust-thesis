:: Close the PDF software
taskkill /IM "PDFXEdit.exe"
:: Output path
set file_name=my_ntust_thesis
set output_path=%~dp0
:: Excute xelatex to generate the aux
if exist %output_path%%file_name%.pdf xelatex .\%file_name%.tex -output-directory=%output_path%
:: Use bibtex with aux to create the bbl
if exist %output_path%%file_name%.aux bibtex %output_path%%file_name%.aux
:: Re-xelatex with bbl to create the references
if exist %output_path%%file_name%.bbl xelatex .\%file_name%.tex -output-directory=%output_path%
:: Create the index fo references
if exist %output_path%%file_name%.bbl xelatex .\%file_name%.tex -output-directory=%output_path%
:: Open it
if exist %output_path%%file_name%.pdf start %output_path%%file_name%.pdf
:: Remove caches
del %output_path%%file_name%.lof
del %output_path%%file_name%.lot
del %output_path%%file_name%.toc
del %output_path%%file_name%.aux
del %output_path%%file_name%.log
del %output_path%%file_name%.blg
del %output_path%%file_name%.bbl