#!/bin/bash

#pybabel extract -F babel.cfg -k lazy_gettext -o messages.pot .
#pybabel init -i messages.pot -d translations -l es
pybabel update -i messages.pot -d translations
