cd ../code
rm res.txt
./orient config.txt >> res.txt
cd ../scripts
python3 orient.py
