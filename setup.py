from setuptools import find_packages, setup

setup(
    name='medibot',                         
    version='0.0.0',
    author='Anshuman Acharya',
    author_email='anshuman.acharyaa@gmail.com',
    description='AI-powered medical chatbot built with Generative AI and LLMs.',
    packages=find_packages(),
    install_requires=[
        # 'openai', 'transformers', 'torch', 'flask', etc.
    ],
    python_requires='>=3.8',
    license='MIT',
    url='https://github.com/anshux01/Medical-ChatBot',  
)
