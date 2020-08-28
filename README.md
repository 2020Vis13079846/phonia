# Phonia Toolkit

<h3 align="center"><img src="https://user-images.githubusercontent.com/54115104/91619957-3ebb0980-e997-11ea-83fc-c8c58982454d.png" alt="logo" height="250px"></h3>

<p align="center">
  <a href="http://entynetproject.simplesite.com/">
    <img src="https://img.shields.io/badge/entynetproject-Ivan%20Nikolsky-blue.svg">
  </a>
  <a href="https://github.com/entynetproject/phonia/releases">
    <img src="https://img.shields.io/github/release/entynetproject/phonia.svg">
  </a>
  <a href="https://wikipedia.org/wiki/Python_(programming_language)">
    <img src="https://img.shields.io/badge/language-python-blue.svg">
 </a>
  <a href="https://github.com/entynetproject/phonia/issues?q=is%3Aissue+is%3Aclosed">
      <img src="https://img.shields.io/github/issues/entynetproject/phonia.svg">
  </a>
  <a href="https://github.com/entynetproject/phonia/wiki">
      <img src="https://img.shields.io/badge/wiki%20-phonia-lightgrey.svg">
 </a>
  <a href="https://twitter.com/entynetproject">
    <img src="https://img.shields.io/badge/twitter-entynetproject-blue.svg">
 </a>
  <a href="https://github.com/sundowndev/PhoneInfoga">
    <img src="https://img.shields.io/badge/based%20on-PhoneInfoga-red.svg">
 </a>
</p>

***

# About Phonia Toolkit

```
Phonia Toolkit is one of the most advanced toolkits to scan 
phone numbers using only free resources. The goal is to first gather 
standard information such as country, area, carrier and line type on 
any international phone numbers with a very good accuracy.
```

***

# Getting started

## Phonia installation

> cd phonia

> chmod +x install.sh

> ./install.sh

## Phonia uninstallation

> cd phonia

> chmod +x uninstall.sh

> ./uninstall.sh

***

# Phonia Toolkit execution

```
To run Phonia Toolkit you should 
execute the following command.
```

> phonia

```
usage: phonia [-h] [-p <phone>] [-i <input_file>] [-o <output_path>]
              [-s <scanner>] [--recon] [--no-ansi] [-u] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -p <phone>, --phone <phone>
                        The phone number to scan.
  -i <input_file>, --input <input_file>
                        List of phone numbers.
  -o <output_path>, --output <output_path>
                        Output to the specified path.
  -s <scanner>, --scanner <scanner>
                        The scanner to use.
  --recon               Launch custom format reconnaissance.
  --no-ansi             Disable colored output.
  -u, --update          Update Phonia Toolkit.
  --version             Show Phonia Toolkit version.
```

***
  
# Phonia Toolkit examples

## Example of scanning a phone number
    
> phonia -p 15554443333
    
## Example of scanning from a file

> phonia -i input.txt -o output.txt
    
## Example of selecting a scanner

> phonia -p 15554443333 -s footprints

***

# Phonia Toolkit disclaimer

```
Usage of the Phonia Toolkit for attacking targets without prior mutual consent is illegal.
It is the end user's responsibility to obey all applicable local, state, federal, and international laws.
Developers assume no liability and are not responsible for any misuse or damage caused by this program.
```
