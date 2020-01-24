#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from sqlalchemy import Column, Integer, String, Boolean
Model = declarative_base(name='Model')

class TestModel(Model)
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    active = Column(Boolean)
