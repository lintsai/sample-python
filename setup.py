from setuptools import setup, find_packages 
 
setup( 
    name='sample-python', 
    version='0.1', 
    packages=find_packages(), 
    install_requires=[ 
        # 在這裡添加需求，例如 'numpy', 'requests' 等。 >> setup.py
    ], 
    entry_points={ 
        'console_scripts': [ 
            'sample-python=sample_python.main:main' 
        ] 
    }, 
) 
