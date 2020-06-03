# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: Python 3 [conda env:pDL]
#     language: python
#     name: python3
# ---

# %% [markdown]
# # My first interactive web app
#
# Here is my first attempt to create a webapp that sums, subtracts, multiplies, and divides two numbers.

# %%
import ipywidgets as widgets
import IPython.display


# %%
class Calculator():
    def __init__(self):
        self.a = widgets.Text(placeholder='a', description='a: ')
        self.b = widgets.Text(placeholder='b', description='b: ')
        self.c = widgets.Text(placeholder='c', description='c: ')

        def sum(x=None):
            self.c.value = f'{float(self.a.value) + float(self.b.value):.2f}'
            self.c.description = 'c = a + b: '
        def sub(x=None):
            self.c.value = f'{float(self.a.value) - float(self.b.value):.2f}'
            self.c.description = 'c = a – b: '
        def mul(x=None):
            self.c.value = f'{float(self.a.value) * float(self.b.value):.2f}'
            self.c.description = 'c = a * b: '
        def div(x=None):
            self.c.value = f'{float(self.a.value) / float(self.b.value):.2f}'
            self.c.description = 'c = a / b: '

        operations = (
            (sum, '+'),
            (sub, '–'),
            (mul, '*'),
            (div, '/'),
        )

        items = [widgets.Button(description=o[1]) for o in operations]
        for i, o in zip(items, operations): i.on_click(o[0])

        box1 = widgets.HBox([items[0], items[1]])
        box2 = widgets.HBox([items[2], items[3]])
        self.box = widgets.VBox([self.a, self.b, box1, box2, self.c])

    def display(self):
        IPython.display.display(self.box)


# %%
cal = Calculator()

# %%
cal.display()
