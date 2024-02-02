# Search Into Files

## Description
"Search Into Files" is a Python script designed for efficiently searching keywords within text files across multiple directories. This tool is perfect for sifting through large data sets or collections of documents to quickly find specific information.

## Features
- **Recursive Search**: Navigate through all subdirectories of a given root directory, ensuring no file is missed.
- **Keyword Highlighting**: Identify and highlight the specific line containing the keyword in each file.
- **Multiple Encoding Support**: Capable of reading files with various encodings, such as UTF-8 and ISO-8859-1.
- **Performance Metrics**: Track and display the total number of files processed, files containing the keyword, and the script's execution time.

## Requirements
- Python 3.x
- `termcolor` package

To install the required package, run:
```
pip install termcolor
```

## Usage
Run the script from the command line using the following format:
```
python3 searchIntoFiles.py -k [KEYWORD] -p [PATH_TO_DIRECTORY]
```
- `-k` or `--keyword`: Specify the keyword to search for.
- `-p` or `--path`: Specify the root directory for the search.

## Example
```
python3 searchIntoFiles.py -k "example keyword" -p "/path/to/directory"
```

## Author
- **Juan Frugeri**
- [Github: jfrugeri](https://github.com/jfrugeri)

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.
```