#ccda parser

This parser is based on pyccda (A Python library for CCDA XML files. Part of the BlueButton+ health data liberation initiative)
Most of the new code is to deal with Observations for Lab measurements. 

##Usage

Before using, run `pip install -r requirements.txt` to install dependencies.

    import pyccda
    ccda = pyccda.CcdaDocument(open('ccda_file.xml'))

    # Returns CCDA represented as a simple CSV, which can be
    # useful to load data into an external data analysis tool.
    ccda.to_csv()


