# SQLAlchemy model markdown generator

Turn your sqlalchemy models into a markdown table.

## Example

The generator turns this

``` python
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
Model = declarative_base(name='Model')

class TestModel(Model):
    __tablename__ = 'test_model'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    active = Column(Boolean)
```

into this:

|name|type|unique|nullable|
|-|-|-|-|
|id|INTEGER|None|False|
|name|VARCHAR|None|False|
|email|VARCHAR|True|True|
|active|BOOLEAN|None|True|


with following script

``` python3
from generator import Generator
from test_model import TestModel

md_table_generator = Generator(TestModel, fields=('name','type', 'unique', 'nullable  '))
md_table_generator.generate_file('table.md')
```

## Usage
- Download `generator.py`. (Maybe available via pip in the future).
- Import it
- Create and instance of the `Generator` class
- First arg needs to be an sqlalchemy model
- Seconds is a tuple of columns you want to show in your table
- Call the `generate_file` method and pass the filename
- Your ready to go!
