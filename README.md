# Gram Scanner

Gram Scanner is a command line interface of Ionian University's Gram-Web.
It can be used for students to easily get a list of their grades.

## Installation

Run:

    $ sudo pip install gram-scanner

Set your Gram-Web username as enviroment variable:
    
    $ echo "export GramWebUser=<your-username>" >> ~/.bash_profile

Set your Gram-Web password as enviroment variable:

    $ echo "export GramWebPass=<your-pass>" >> ~/.bash_profile

Also make sure to reload your `.bash_profile` file after setting your credentials by running:
    
    $ source ~/.bash_profile
    
## Usage

Simply run `gram-scanner` to get a list of your grades:
    
    $ gram-scanner


## Contributing

If you have found a bug or would like to ask a question please open an issue.
Pull requests are welcome.

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
