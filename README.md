# lecture-slidecounter
Lists information about the amount of slides contained in a folder of PDFs

First step in learning for an exam is to get an overview of the amount of slides.
Often the lecture is separated into multipe PDF files (one for each lecture).
By merging the PDF file we get the total amount of slides easily - but without the information which lecture had how many slides.

As i like to see my progress while revising lectures (e.g. for estimating if I'm on track regarding the exam date) I wrote this script to generate a list which gives an overview of the number of slides in each PDF.

## Requirements
the only requirement is pyPdf for reading the page count of the PDF files

## Installation
    git clone https://github.com/eiselems/lecture-slidecounter.git && cd lecture-slidecounter
    pip install requirements.txt

## Usage

Example: 
```
python slide-counter.py /c/lectures/
```

Example output:
```
Web 00 Content - Web based integration.pdf                          16
Web 01 - Web as Platform.pdf                                       109
Web 02 - CSS & RSS & Forms.pdf                                      33
Web 03 - Portals.pdf                                                20
Web 04 - HTTP.pdf                                                  163
Web 05 - REST.pdf                                                  121
Web 06 - eMail.pdf                                                  65
Web 07 - Dynamic Pages.pdf                                          59
Web 08 - XML - Namespaces & Info Set ONLY.pdf                       21
Web 12 - SOAP.pdf                                                  138
Web 13 - WSDL.pdf                                                   57
Web 14 - Policy.pdf                                                 97
Web 15 - Axis2 & JAX-WS.pdf                                         17
Web 16 - Discovery Basics.pdf                                       31
Web 17 - Aggreement.pdf                                             41
---------------------------------------------------------------------------
Total Pages: 988
```
