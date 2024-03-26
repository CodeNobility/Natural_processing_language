# Text Emotion Analysis

This Python script analyzes the emotions expressed in a given text and visualizes the frequency of each emotion using a bar chart.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example](#example)

## Description

This script reads a text file containing some content and identifies the emotions associated with the words in the text. It utilizes a list of words associated with specific emotions from the `emotions.txt` file. It then cleans the text, removes punctuation and common stop words, and extracts the relevant words. After that, it matches the words with the emotions they represent and counts the frequency of each emotion. Finally, it generates a bar chart to visualize the distribution of emotions in the text.

## Features

- Analyzes the emotions expressed in a given text.
- Removes punctuation and common stop words for accurate analysis.
- Visualizes the frequency of each emotion using a bar chart.
- Customizable stop words list.
- Supports different input text files.

## Requirements

- Python 3.x
- Matplotlib library

## Usage

1. Clone this repository to your local machine:

### git clone 
    https://github.com/CodeNobility/Natural_processing_language.git


2. Ensure you have Python installed on your system. You can download it from [here](https://www.python.org/downloads/).

3. Install the required libraries using pip:

   pip install matplotlib

4. Place your text file to be analyzed in the repository directory. Ensure it's named `file.txt`.

5. Run the script: natural_processing_language.py

6. The script will generate a bar chart (`graph.png`) in the same directory, visualizing the distribution of emotions in the text.

## Example

Suppose you have a text file named `file.txt` containing: Prince kuMAr @email id # is princeGupta1726@gmail.com !


The script will analyze the text and generate a bar chart showing the distribution of emotions expressed in the text.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.









