#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from generator import Generator
from test_model import TestModel

md_table_generator = Generator(TestModel, fields=('name','type', 'unique', 'nullable  '))
md_table_generator.generate_file('table.md')
