@echo off

echo Creating virtual environment...
python -m venv myenv


echo Activating virtual environment...
call myenv\Scripts\activate


echo Installing required packages...
pip install -r requirements.txt

REM İşlem tamamlandığında bilgilendirme
echo Setup is complete! You can now run your project.
pause

