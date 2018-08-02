# Gram Scanner

Gram Scanner is an unofficial command line interface of Ionian University's Gram-Web.
It can be used by students to easily get a list of their grades.

## Demo

![gif](https://i.imgur.com/qD4kZuX.gif)

## Installation

Run:

    $ sudo pip install gram-scanner

Set your Gram-Web username as enviroment variable:
    
    $ echo "export GramWebUser=<your-username>" >> ~/.bash_profile

Set your Gram-Web password as enviroment variable:

    $ echo "export GramWebPass=<your-password>" >> ~/.bash_profile

Also make sure to reload your `.bash_profile` file after setting your credentials by running:
    
    $ source ~/.bash_profile
    
## Usage

Simply run `gram-scanner` to get a list of your grades:
    
    $ gram-scanner

You can also pass your credentials as arguments:
    
    $ gram-scanner <your-username> <your-password>

## Contributing

If you have found a bug or would like to ask a question please open an issue.
Pull requests are welcome.

## License

The package is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).
