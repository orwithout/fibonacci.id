%userprofile%\miniconda3\Scripts\activate.bat senseurl
conda install -y python
pip install fastapi
pip install uvicorn
conda install -y -c conda-forge python-jose
conda install -y -c conda-forge python-dotenv
conda install -c conda-forge pydantic-settings -y
conda install -c conda-forge aiofiles -y
conda install -c conda-forge python-multipart -y
conda install -c conda-forge pyjwt -y