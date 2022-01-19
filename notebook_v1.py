#!/usr/bin/env python
# -*- coding: utf-8 -*-
# +
# Python Standard Library
import base64
import io
import json
import pprint

import ast
# -
"""
an object-oriented version of the notebook toolbox
"""
def load_ipynb(filename):
    aouvrir = open(filename)
    b = aouvrir.read() 
    dict = json.loads(b)
    aouvrir.close()
    return dict

def get_format_version(ipynb):
    #on transforme le filename en dictionnaire
    nb_format=ipynb['nbformat']
    nb_format_minor=ipynb['nbformat_minor']
    return f'{nb_format}'+ '.' + f'{nb_format_minor}'

def get_cells(ipynb):
    return ipynb['cells']


def to_percent(ipynb):
    t=''
    for cell in ipynb['cells']:
        if cell['cell_type']=='markdown':
            t+='# %% [markdown]\n'
            for line in cell['source']:
                t+='# '+line
            t+='\n'
        else:
            t=t+'# %% \n'
            for line in cell['source']:
                t=t+line
            t=t+'\n'
    t=t[:-1]
    return t

def save_ipynb(ipynb, filename):
    aouvrir = open(filename, "w")
    aouvrir.write(json.dumps(ipynb))
    aouvrir.close() 



class CodeCell:
    r"""A Cell of Python code in a Jupyter notebook.

    Args:
        ipynb (dict): a dictionary representing the cell in a Jupyter Notebook.

    Attributes:
        id (int): the cell's id.
        source (list): the cell's source code, as a list of str.
        execution_count (int): number of times the cell has been executed.

    Usage:

        >>> code_cell = CodeCell({
        ...     "cell_type": "code",
        ...     "execution_count": 1,
        ...     "id": "b777420a",
        ...     'source': ['print("Hello world!")']
        ... })
        >>> code_cell.id
        'b777420a'
        >>> code_cell.execution_count
        1
        >>> code_cell.source
        ['print("Hello world!")']
    """

    def __init__(self, ipynb):
        self.id = ipynb["id"]
        self.source = ipynb['source']
        self.execution_count = ipynb["execution_count"]


class MarkdownCell:
    r"""A Cell of Markdown markup in a Jupyter notebook.

    Args:
        ipynb (dict): a dictionary representing the cell in a Jupyter Notebook.

    Attributes:
        id (int): the cell's id.
        source (list): the cell's source code, as a list of str.

    Usage:

        >>> markdown_cell = MarkdownCell({
        ...    "cell_type": "markdown",
        ...    "id": "a9541506",
        ...    "source": [
        ...        "Hello world!\n",
        ...        "============\n",
        ...        "Print `Hello world!`:"
        ...    ]
        ... })
        >>> markdown_cell.id
        'a9541506'
        >>> markdown_cell.source
        ['Hello world!\n', '============\n', 'Print `Hello world!`:']
    """

    def __init__(self, ipynb):
        self.id = ipynb["id"]
        self.source = ipynb["source"]


class Notebook:
    r"""A Jupyter Notebook.

    Args:
        ipynb (dict): a dictionary representing a Jupyter Notebook.

    Attributes:
        version (str): the version of the notebook format.
        cells (list): a list of cells (either CodeCell or MarkdownCell).

    Usage:

        - checking the verion number:

            >>> ipynb = toolbox.load_ipynb("samples/minimal.ipynb")
            >>> nb = Notebook(ipynb)
            >>> nb.version
            '4.5'

        - checking the type of the notebook parts:

            >>> ipynb = toolbox.load_ipynb("samples/hello-world.ipynb")
            >>> nb = Notebook(ipynb)
            >>> isinstance(nb.cells, list)
            True
            >>> isinstance(nb.cells[0], Cell)
            True
    """

    def __init__(self, ipynb):
        self.version = get_format_version(ipynb)
        self.cells = get_cells(ipynb)

    @staticmethod
    def from_file(filename):
        return(Notebook(load_ipynb(filename)))
        r"""Loads a notebook from an .ipynb file.

        Usage:

            >>> nb = Notebook.from_file("samples/minimal.ipynb")
            >>> nb.version
            '4.5'
        """

    def __iter__(self):
        r"""Iterate the cells of the notebook.

        Usage:

            >>> nb = Notebook.from_file("samples/hello-world.ipynb")
            >>> for cell in nb:
            ...     print(cell.id)
            a9541506
            b777420a
            a23ab5ac
        """
        return iter(self.cells) 


# On remarque que cette dernière fonction est bien définie car self.cells est une liste ; devenant ici un itérateur.

# +
class PyPercentSerializer:
    r"""Prints a given Notebook in py-percent format.
    Args:
        notebook (Notebook): the notebook to print.

    Usage:
            >>> nb = Notebook.from_file("samples/hello-world.ipynb")
            >>> ppp = PyPercentSerializer(nb)
            >>> print(ppp.to_py_percent()) # doctest: +NORMALIZE_WHITESPACE
            # %% [markdown]
            # Hello world!
            # ============
            # Print `Hello world!`:
            <BLANKLINE>
            # %%
            print("Hello world!")
            <BLANKLINE>
            # %% [markdown]
            # Goodbye! 👋
    """
    def __init__(self, notebook):
        self.notebook=notebook
    
    def to_py_percent(self):
        nb=dict() # on s'en servira pour contenir le futur notebook
        NB=self.notebook
        nb['cells']=[]
        for cellule in NB.cells:
            nouvelle_cellule=dict() #il contiendra les cellules
            if type(cellule)==MarkdownCell: #on construit la cellule comme dans les exemples.
                nouvelle_cellule["cellule_type"]='markdown'
                nouvelle_cellule['metadata']={}
                nouvelle_cellule["id"]=cellule.id
                nouvelle_cellule["source"]=cellule.source
            else:
                nouvelle_cellule['cellule_type']='code'
                nouvelle_cellule["execution_count"]=cellule.execution_count
                nouvelle_cellule['metadata']={}
                nouvelle_cellule["source"]=cellule.source
                nouvelle_cellule['outputs']=[]
            nb['cells'].append(nouvelle_cellule) #la cellule construite appartient maintenant à la liste des cellules
        nb['metadata']={}
        Z=NB.version
        Z.split('.') #afin de séparer deux indicateurs de version
        nb['nbformat']=int(Z[0])
        nb['nbformat_minor']=int(Z[-1])
        r"""Converts the notebook to a string in py-percent format.
        """
        return(to_percent(nb))
        

    def to_file(self, filename):
        r"""Serializes the notebook to a file

        Args:
            filename (str): the name of the file to write to.

        Usage:

                >>> nb = Notebook.from_file("samples/hello-world.ipynb")
                >>> s = PyPercentSerializer(nb)
                >>> s.to_file("samples/hello-world-serialized-py-percent.py")
        """
        ipynb=self.to_py_percent()
        save_ipynb(ipynb,filename)
    
class Serializer:
    r"""Serializes a Jupyter Notebook to a file.

    Args:
        notebook (Notebook): the notebook to print.

    Usage:

        >>> nb = Notebook.from_file("samples/hello-world.ipynb")
        >>> s = Serializer(nb)
        >>> pprint.pprint(s.serialize())  # doctest: +NORMALIZE_WHITESPACE
            {'cells': [{'cell_type': 'markdown',
                'id': 'a9541506',
                'medatada': {},
                'source': ['Hello world!\n',
                           '============\n',
                           'Print `Hello world!`:']},
               {'cell_type': 'code',
                'execution_count': 1,
                'id': 'b777420a',
                'medatada': {},
                'outputs': [],
                'source': ['print("Hello world!")']},
               {'cell_type': 'markdown',
                'id': 'a23ab5ac',
                'medatada': {},
                'source': ['Goodbye! 👋']}],
            'metadata': {},
            'nbformat': 4,
            'nbformat_minor': 5}
        >>> s.to_file("samples/hello-world-serialized.ipynb")
    """

    def __init__(self, notebook):
        self.notebook=notebook

    def serialize(self):
        r"""Serializes the notebook to a JSON object

        Returns:
            dict: a dictionary representing the notebook.
        """
        nb=dict()
        NB=self.notebook
        nb['cells']=[]
        for cellule in NB.cells:
            nouvelle_cellule=dict() 
            if type(cellule)==MarkdownCell: 
                nouvelle_cellule["cellule_type"]='markdown'
                nouvelle_cellule['metadata']={}
                nouvelle_cellule["id"]=cellule.id
                nouvelle_cellule["source"]=cellule.source
            else:
                nouvelle_cellule['cellule_type']='code'
                nouvelle_cellule["execution_count"]=cellule.execution_count
                nouvelle_cellule['metadata']={}
                nouvelle_cellule["source"]=cellule.source
                nouvelle_cellule['outputs']=[]
            nb['cells']=nb['cells']+[nouvelle_cellule]
        nb['metadata']={}
        Z=NB.version
        Z.split('.') 
        nb['nbformat']=int(Z[0])
        nb['nbformat_minor']=int(Z[-1])
        return(nb)

    def to_file(self, filename):
        #pas compris
        r"""Serializes the notebook to a file

        Args:
            filename (str): the name of the file to write to.

        Usage:

                >>> nb = Notebook.from_file("samples/hello-world.ipynb")
                >>> s = Serializer(nb)
                >>> s.to_file("samples/hello-world-serialized.ipynb")
                >>> nb = Notebook.from_file("samples/hello-world-serialized.ipynb")
                >>> for cell in nb:
                ...     print(cell.id)
                a9541506
                b777420a
                a23ab5ac
        """
        pass


# -

class Outliner:
    def init(self,notebook):
        self.notebook=notebook
    def outline(self):
        pass

