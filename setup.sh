# pip
python3 -m venv .
source bin/activate
pip3 install pyswip

# APE
cd APE
make install
mv ape.exe ..
cd ..