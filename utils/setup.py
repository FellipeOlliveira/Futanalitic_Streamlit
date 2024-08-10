from setuptools import setup, find_packages

setup(
    name='utils',                   # Nome do pacote
    version='0.1.0',                 # Versão do pacote
    description='A sample utils package',  # Descrição curta
    author='Marco',               # Nome do autor
    author_email='marcosf1625@gmail.com',  # Email do autor
    url='https://github.com/FellipeOlliveira/Futanalitic_Streamlit',  # URL do projeto (opcional)
    packages=find_packages(),         # Encontra todos os pacotes e subpacotes
    classifiers=[                    # Classificadores de projeto (opcional)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',          # Versão mínima do Python
    install_requires=[               # Dependências do pacote (se houver)
        # 'some_dependency>=1.0',
    ]
)
