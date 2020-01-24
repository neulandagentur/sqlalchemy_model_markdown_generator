#!/usr/bin/env python3
# -*- encoding: utf-8 -*-


class Generator:
    def __init__(self, model, fields=('name',)):
        self.model = model
        self.columns = self.model.__table__.columns
        self.fields = fields
        self.rows_length = len(self.columns)
        self.header_length = len(fields)

    def generate_file(self, filename):
        # create a new file
        with open(filename, 'w') as file:

            # create header
            header = '|'
            for field in self.fields:
                header += '{}|'.format(field)

            file.write(header)

            # create split
            split = '|'
            for _ in range(self.header_length):
                split += '-|'

            file.write('\n{}'.format(split))

            #  create table content
            table = ''
            for col in self.columns:
                row = '|'
                for field in self.fields:
                    row += '{}|'.format(col.__dict__[field])
                table += '\n{}'.format(row)

            file.write(table)
