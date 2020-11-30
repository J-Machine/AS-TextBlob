## Entorno

- Trabajando con Virtualenv en pip-20.3

  -- Installing collected packages: filelock, appdirs, distlib, virtualenv
- Tutorial seguido para el entorno virtual https://help.dreamhost.com/hc/es/articles/115000695551-Instalar-y-usar-virtualenv-con-Python-3
- textblob-0.15.3-py2.py3-none-any.whl
- nltk>=3.1
- click-7.1.2-py2.py3-none-any.whl
- joblib-0.17.0-py3-none-any.whl
- regex-2020.11.13-cp38-cp38-manylinux2014_x86_64.whl
- tqdm-4.54.0-py2.py3-none-any.whl
- 
## Para activar el nuevo ambiente virtual, corre lo siguiente:
    [server]$ source venv/bin/activate
## Desactivar tu virtualenv
Cuando finalices tu trabajo en tu ambiente virtual, puedes desactivarlo corriendo lo siguiente:

    [server]$ deactivate

- Forma correcta de activar ambientes vituales: https://medium.com/@jtpaasch/the-right-way-to-use-virtual-environments-1bc255a0cba7
  
## Creación de los requirements.txt 

    pip freeze --local > requirements.txt

El parámetro --local solo generará una lista de paquetes y versiones que se instalan localmente en un virtualenv. Los paquetes globales no serán listados.

