# DicMer

DicMer is a Python mini library for recursively merging dictionaries.


## Build status

[![Build Status](https://travis-ci.org/ashep/dicmer.svg?branch=master)](https://travis-ci.org/ashep/dicmer)
[![Coverage](https://codecov.io/gh/ashep/dicmer/branch/master/graph/badge.svg)](https://codecov.io/gh/ashep/dicmer)


## Features

* Unlimited number and depth of source dictionaries.
* Doesn't modify source dictionaries. 
* Properly merges lists.


## Requirements

Python >=3.5


## Installation

```bash
pip install dicmer
```

## Usage

Following example:

```python
from dicmer import dict_merge

a = {
    'string': 'Lorem Ipsum',
    'dicts': {
        'b1': 'It is simply dummy text',
        'b2': {
            'b2_1': 'Printing and typesetting industry',
            'b2_2': 'It has survived not only five centuries',
        }
    },
    'list': [
        'What is Lorem Ipsum?',
        'Where does it come from?',
    ]
}

b = {
    'dicts': {
        'b2': {
            'b2_1': 'WARNING: This key was overwritten!',
            'b2_3': 'WARNING: This key was aded!',
        },
        'b3': 'WARNING: This key was added!'
    },
    'list': [
        'Why do we use it?',
        'Where can I get some?',
    ],
    'new key': {
        'I am': 'a new string!'
    }
}

print(dict_merge(a, b))
```

Will provide following result:

```python
{
    'string': 'Lorem Ipsum', 
    'dicts': {
        'b1': 'It is simply dummy text', 
        'b2': {
            'b2_1': 'WARNING: This key was overwritten!', 
            'b2_2': 'It has survived not only five centuries', 
            'b2_3': 'WARNING: This key was aded!'
        }, 
        'b3': 'WARNING: This key was added!'
    },
    'list': [
        'What is Lorem Ipsum?',
        'Where does it come from?',
        'Why do we use it?',
        'Where can I get some?'
    ], 
    'new key': {
        'I am': 'a new dict!'
    }
}
```

## Documentation

See usage example.


## Testing

```bash
python setup.py test
```
or

```bash
make test
```


## Contributing

If you want to contribute to a project and make it better, your help is very 
welcome. Contributing is also a great way to learn more about social coding on 
Github, new technologies and and their ecosystems and how to make constructive, 
helpful bug reports, feature requests and the noblest of all contributions: 
a good, clean pull request.

- Create a personal fork of the project on Github.
- Clone the fork on your local machine. Your remote repo on Github is called 
  `origin`.
- Add the original repository as a remote called `upstream`.
- If you created your fork a while ago be sure to pull upstream changes into 
  your local repository.
- Create a new branch to work on. Branch from `develop` if it exists, else from 
  `master`.
- Implement/fix your feature, comment your code.
- Follow the code style of the project, including indentation.
- If the project has tests run them.
- Write or adapt tests as needed.
- Add or change the documentation as needed.
- Squash your commits into a single commit with git's interactive rebase. Create 
  a new branch if necessary.
- Push your branch to your fork on Github, the remote `origin`.
- From your fork open a pull request in the correct branch. Target the project's 
  `develop` branch if there is one, else go for `master`.
- If the maintainer requests further changes just push them to your branch. 
- Once the pull request is approved and merged you can pull the changes from 
  `upstream` to your local repo and delete your extra branch(es).

And last but not least: Always write your commit messages in the present tense. 
Your commit message should describe what the commit, when applied, does to the 
code – not what you did to the code.


## Roadmap

None.


## Support

If you have any issues or enhancement proposals feel free to report them via 
project's [Issue Tracker](https://github.com/ashep/dicmer/issues). 


## Authors

* [Oleksandr Shepetko](https://shepetko.com) -- initial work.


## Credits

None.


## License

This project is licensed under the MIT License. See the [LICENSE.md](LICENSE.md) 
file for details.
