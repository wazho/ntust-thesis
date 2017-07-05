:: At first, please check your environment variable has 'xelatex' and 'bibtex'.
:: Add the path like "C:\Program Files\MiKTeX 2.9\miktex\bin\x64" in Path.
:: And install the packages of latex that are 'l3kernel', 'xparse', 't3enc' ... etc

:: Close the PDF software
taskkill /IM "PDFXEdit.exe"
:: Output path
set file_name=my_ntust_thesis
set new_file_name=Ze_Hao_Wang-M10415096-Game_Design_Goal_Oriented_Approach_for_Procedural_Content_Generation
set output_path=%~dp0
:: Remove olds
del %output_path%%file_name%.pdf
del %output_path%%new_file_name%.pdf
:: Excute xelatex to generate the aux
xelatex .\%file_name%.tex -output-directory=%output_path%
:: Use bibtex with aux to create the bbl
if exist %output_path%%file_name%.aux bibtex %output_path%%file_name%.aux
:: Re-xelatex with bbl to create the references
if exist %output_path%%file_name%.bbl xelatex .\%file_name%.tex -output-directory=%output_path%
:: Create the index fo references
if exist %output_path%%file_name%.bbl xelatex .\%file_name%.tex -output-directory=%output_path%
:: Rename is and open it
if exist %output_path%%file_name%.pdf ren %output_path%%file_name%.pdf %new_file_name%.pdf
if exist %output_path%%new_file_name%.pdf start %output_path%%new_file_name%.pdf
:: Remove caches
del %output_path%%file_name%.lof
del %output_path%%file_name%.lot
del %output_path%%file_name%.toc
del %output_path%%file_name%.aux
del %output_path%%file_name%.log
del %output_path%%file_name%.blg
del %output_path%%file_name%.bbl