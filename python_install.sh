#!/bin/bash
sudo yum install git gcc gcc-c++ make readline-devel sqlite-devel patch openssl-devel zlib libffi-devel zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel -y
curl -L https://raw.github.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash

export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"

pyenv install 2.7.6
pyenv install 3.5.0

pyenv virtualenv 2.7.6 1st
pyenv virtualenv 3.5.0 2nd
