# Port Scanner
[![MIT License](https://a11ybadges.com/badge?text=MIT_License&badgeColor=FCD12A)](https://choosealicense.com/licenses/mit/)
## Description
A simple and fast port scanner built in Python that allows you to scan a range of ports on a target IP. This tool uses threading to improve speed and efficiency, providing quick feedback on what ports are open. The output lists open ports found by port number and a detailed information about each port's service and description. It features, multi-threaded scanning, a large list of common ports in order to provide as much information to users about the open port found, and a formatted output with color-coding of ports/services that increases readability.

## Table of Contents
- [Port Scanner](#port-scanner)
  - [Description](#description)
  - [Table of Contents](#table-of-contents)
  - [Languages \& Technologies Used](#languages--technologies-used)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Questions](#questions)
  - [License](#license)


## Languages & Technologies Used

[![Python](https://a11ybadges.com/badge?logo=python)](https://www.python.org/)

[![threading](https://a11ybadges.com/badge?text=threading&badgeColor=orange)](https://docs.python.org/3/library/threading.html)

[![socket](https://a11ybadges.com/badge?text=socket&badgeColor=cyan)](https://docs.python.org/3/library/socket.html)

[![colorama](https://a11ybadges.com/badge?text=colorama&badgeColor=purple)](https://pypi.org/project/colorama/)

[![pyfiglet](https://a11ybadges.com/badge?text=pyfiglet&badgeColor=green)](https://pypi.org/project/pyfiglet/)


## Installation
1. Clone the repository to the desired location:

```
git clone https://github.com/dsoda86/DIY-Port-Scanner
```

2. Install required dependencies:
   
```
pip install colorama pyfiglet
```

1. Run the script:

```
python port-scanner.py
```

## Usage
After running the script, you'll be prompted to enter a target IP address. The scanner will then check the specified range of ports and provide feedback on which ports are open. If a port is open, the service name and description will be displayed.

![scanner-started](/images/scanner-started.png)

![scanning-complete](/images/scanning-complete.png)

## Questions
Check out my work at  
[![github/dsoda86](https://a11ybadges.com/badge?logo=github&logoColor=skyblue)](https://github.com/dsoda86)


Please send your questions to  [dsoda86@gmail.com](mailto:dsoda86@gmail.com?subject=[GitHub]%20Dev%20Connect).
## License
Click to learn more about this license and other commonly used licenses.

[![MIT License](https://a11ybadges.com/badge?text=MIT_License&badgeColor=FCD12A)](https://choosealicense.com/licenses/)

