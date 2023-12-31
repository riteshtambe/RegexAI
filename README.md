# RegexAi 

[![Release](https://img.shields.io/pypi/v/regexai?label=Release&style=flat-square)](https://pypi.org/project/regexai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1hN9JohE5BdZrH5viCkDLfGF5pRI9S4KQ?usp=sharing)

RegexAI is a user-friendly library powered by generative AI, simplifying regular expression use. It interprets plain language regex queries, making data extraction and text manipulation easy. Whether you're a beginner or pro, RegexAI adapts to your needs, streamlining [regex](https://pypi.org/project/regex/) tasks for enhanced efficiency and accessibility.


## 🔧 Quick install

```bash
pip install regexai
```

## 🔍 Demo

Try out RegexAI in your browser :

[![Open in Colab](https://camo.githubusercontent.com/84f0493939e0c4de4e6dbe113251b4bfb5353e57134ffd9fcab6b8714514d4d1/68747470733a2f2f636f6c61622e72657365617263682e676f6f676c652e636f6d2f6173736574732f636f6c61622d62616467652e737667)](https://colab.research.google.com/drive/1hN9JohE5BdZrH5viCkDLfGF5pRI9S4KQ?usp=sharing)



RegexAI is designed to be used in conjunction with regex. It makes regex conversational, allowing you to ask questions to your data in natural language.

### Queries

For example, you can ask RegexAI to Find words that contain the letter 'q' but not followed by 'u,' and replace them with the word 'quarantined.' from the user given paragraph :

```python
from regexai.pattern import apikey

# Sample paragraph and regex query
test_paragraph = """In a racecar, the radar detected an abnormal level of radioactive materials. Please contact support at support@example.com or visit our website at https://www.example.com. You can also reach us at +1 (123) 456-7890. For inquiries, please send an email to info@example.org. Remember, regex is a powerful tool that can validate 1234 different types of input data! Not all q
words are quirky, but regex can help you find them. Please enter your 16-digit credit card number: 4532015115898164.""" 
query = """ Find words that contain the letter 'q' but not followed by 'u,' and replace them with the word 'quarantined.' """

# Instantiate an object
od=apikey("your openai key")
print("Output : ", od.find_all(test_paragraph,query))
print("Generated Code for your Query : ")
print(od.get_pattern())
```

The above code will return the following:

```
Output :  In a racecar, the radar detected an abnormal level of radioactive materials.
Please contact support at support@example.com or visit our website at https://www.example.com. You can also reach us at +1 (123) 456-7890. For inquiries, please send an email to info@example.org. Remember, regex is a powerful tool that can validate 1234 different types of input data! Not all quarantined words are quirky, but regex can help you find them.
Please enter your 16-digit credit card number: 4532015115898164.

Generated Code for your Query : 
import re
result = re.sub(r'\bq(?!u)\w+\b', 'quarantined', da)
```

Of course, you can also ask RegexAI to perform more complex queries depending upon your need and requirements. 

## 🔒 Privacy & Security

In order to protect your privacy and safety , we do not save any type of file or data on our side and the package totally runs on your local system.


## 🤝 Contributing

Contributions are welcome! Please check out the to-dos below, and feel free to open a pull request.

To-dos:
1. Connect with different file sources feteching from different databases.
2. Ideas to bypass token limit set by openai.
3. Multiagent capabilities to perform parallel operations on different chunk of text data.
4. Any contributions which you think can boost regexai use in your daily life.

For more information, please visit our [github page](https://github.com/riteshtambe/RegexAI).

After installing the virtual environment, please remember to install `pre-commit` to be compliant with our standards:

```bash
pre-commit install
```

## Contributors

[![Contributors](https://contrib.rocks/image?repo=riteshtambe/RegexAI)](https://github.com/riteshtambe/RegexAI/graphs/contributors)

## 📜 License

RegexAI is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgements

- This project is based on the regex library by independent contributors, but it's in no way affiliated with the regex project.
- This project is meant to be used as a tool for data extraction, feature processing from textual data, and it's not meant to be used for production purposes. Please use it responsibly.
