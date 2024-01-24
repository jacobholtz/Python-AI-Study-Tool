A python script that uses Chat-GPT-3.5 to generate questions based off of a local file supplied via a command line argument. An API key must be generated from https://platform.openai.com/api-keys and assigned to an environment variable via ```setx OPENAI_API_KEY "your_api_key"```

The local file must be in a format that contains bullet points and sub-bullet points:
<img src=".\images\style.png">

Converting from Microsoft OneNote to a usable .txt file requires exporting from OneNote > Word > .txt

Prior to tool usage, run ```pip install -r requirements.txt``` to install the required dependencies.

Usage: ```python tool.py file.txt``` where ```file.txt``` is a local file on your system.