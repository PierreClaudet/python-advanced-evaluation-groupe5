#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
starter code for your evaluation assignment
"""

# +
# Python Standard Library
import base64
import io
import json
import pprint

# -

# Third-Party Libraries
import numpy as np
import PIL.Image  # pillow


def load_ipynb(filename):
    aouvrir = open(filename)
    b = aouvrir.read() 
    dict = json.loads(b)
    aouvrir.close()
    return dict
    r"""
    Load a jupyter notebook .ipynb file (JSON) as a Python dict.

    Usage:

        >>> ipynb = load_ipynb("samples/minimal.ipynb")
        >>> ipynb
        {'cells': [], 'metadata': {}, 'nbformat': 4, 'nbformat_minor': 5}

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> pprint.pprint(ipynb)
        {'cells': [{'cell_type': 'markdown',
                    'id': 'a9541506',
                    'metadata': {},
                    'source': ['Hello world!\n',
                               '============\n',
                               'Print `Hello world!`:']},
                   {'cell_type': 'code',
                    'execution_count': 1,
                    'id': 'b777420a',
                    'metadata': {},
                    'outputs': [{'name': 'stdout',
                                 'output_type': 'stream',
                                 'text': ['Hello world!\n']}],
                    'source': ['print("Hello world!")']},
                   {'cell_type': 'markdown',
                    'id': 'a23ab5ac',
                    'metadata': {},
                    'source': ['Goodbye! 👋']}],
         'metadata': {},
         'nbformat': 4,
         'nbformat_minor': 5}
    """


ipynb=load_ipynb("samples/hello-world.ipynb")
ipynb


def save_ipynb(ipynb, filename):
    aouvrir = open(filename, "w")
    aouvrir.write(json.dumps(ipynb))
    aouvrir.close() 
    r"""
    Save a jupyter notebook (Python dict) as a .ipynb file (JSON)

    Usage:

        >>> ipynb = load_ipynb("samples/minimal.ipynb")
        >>> ipynb
        {'cells': [], 'metadata': {}, 'nbformat': 4, 'nbformat_minor': 5}
        >>> ipynb["metadata"]["clone"] = True
        >>> save_ipynb(ipynb, "samples/minimal-save-load.ipynb")
        >>> load_ipynb("samples/minimal-save-load.ipynb")
        {'cells': [], 'metadata': {'clone': True}, 'nbformat': 4, 'nbformat_minor': 5}

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> save_ipynb(ipynb, "samples/hello-world-save-load.ipynb")
        >>> ipynb == load_ipynb("samples/hello-world-save-load.ipynb")
        True

    """


ipynb = load_ipynb("samples/minimal.ipynb")
ipynb

ipynb["metadata"]["clone"] = True
save_ipynb(ipynb, "samples/minimal-save-load.ipynb")
load_ipynb("samples/minimal-save-load.ipynb")


def get_format_version(ipynb):
    #on transforme le filename en dictionnaire
    nb_format=ipynb['nbformat']
    nb_format_minor=ipynb['nbformat_minor']
    return f'{nb_format}'+ '.' + f'{nb_format_minor}'

    r"""
    Return the format version (str) of a jupyter notebook (dict).

    Usage:

        >>> ipynb = load_ipynb("samples/minimal.ipynb")
        >>> get_format_version(ipynb)
        '4.5'

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> get_format_version(ipynb)
        '4.5'
    """


ipynb = load_ipynb("samples/minimal.ipynb")
get_format_version(ipynb)


def get_metadata(ipynb):
    return ipynb['metadata']
    r"""
    Return the global metadata of a notebook.
    Usage:

        >>> ipynb = load_ipynb("samples/metadata.ipynb")
        >>> metadata = get_metadata(ipynb)
        >>> pprint.pprint(metadata)
        {'celltoolbar': 'Edit Metadata',
         'kernelspec': {'display_name': 'Python 3 (ipykernel)',
                        'language': 'python',
                        'name': 'python3'},
         'language_info': {'codemirror_mode': {'name': 'ipython', 'version': 3},
                           'file_extension': '.py',
                           'mimetype': 'text/x-python',
                           'name': 'python',
                           'nbconvert_exporter': 'python',
                           'pygments_lexer': 'ipython3',
                           'version': '3.9.7'}}
    """


ipynb = load_ipynb("samples/Hello-world.ipynb")
metadata = get_metadata(ipynb)
pprint.pprint(metadata)


def get_cells(ipynb):
    return ipynb['cells']
    r"""
    Return the notebook cells.

    Usage:

        >>> ipynb = load_ipynb("samples/minimal.ipynb")
        >>> cells = get_cells(ipynb)
        >>> cells
        []

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> cells = get_cells(ipynb)
        >>> pprint.pprint(cells)
        [{'cell_type': 'markdown',
          'id': 'a9541506',
          'metadata': {},
          'source': ['Hello world!\n', '============\n', 'Print `Hello world!`:']},
         {'cell_type': 'code',
          'execution_count': 1,
          'id': 'b777420a',
          'metadata': {},
          'outputs': [{'name': 'stdout',
                       'output_type': 'stream',
                       'text': ['Hello world!\n']}],
          'source': ['print("Hello world!")']},
         {'cell_type': 'markdown',
          'id': 'a23ab5ac',
          'metadata': {},
          'source': ['Goodbye! 👋']}]
    """


ipynb = load_ipynb("samples/hello-world.ipynb")
cells = get_cells(ipynb)
pprint.pprint(cells)


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
    r"""
    Convert a ipynb notebook (dict) to a Python code in the percent format (str).

    Usage:

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> print(to_percent(ipynb)) # doctest: +NORMALIZE_WHITESPACE
        # %% [markdown]
        # Hello world!
        # ============
        # Print `Hello world!`:
        # %%
        print("Hello world!")
        # %% [markdown]
        # Goodbye! 👋

        >>> notebook_files = Path(".").glob("samples/*.ipynb")
        >>> for notebook_file in notebook_files:
        ...     ipynb = load_ipynb(notebook_file)
        ...     percent_code = to_percent(ipynb)
        ...     with open(notebook_file.with_suffix(".py"), "w", encoding="utf-8") as output:
        ...         print(percent_code, file=output)
    """


ipynb = load_ipynb("samples/hello-world.ipynb")
print(to_percent(ipynb)) 


# +
# def starboard_html(code):
#     return f"""
# <!doctype html>
# <html>
#     <head>
#         <meta charset="utf-8">
#         <title>Starboard Notebook</title>
#         <meta name="viewport" content="width=device-width,initial-scale=1">
#         <link rel="icon" href="https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/favicon.ico">
#         <link href="https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/starboard-notebook.css" rel="stylesheet">
#     </head>
#     <body>
#         <script>
#             window.initialNotebookContent = {code!r}
#             window.starboardArtifactsUrl = `https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/`;
#         </script>
#         <script src="https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/starboard-notebook.js"></script>
#     </body>
# </html>
# """
# -

def to_starboard(ipynb, html=False):
    t=''
    for cell in ipynb['cells']:
        if cell['cell_type']=='markdown':
            t+='# %% [markdown]'+'\n'
            for line in cell['source']:
                t+=line 
            t+='\n\n'
        else:
            t=t+'# %% [python]'+'\n'
            for line in cell['source']:
                t=t+line
            t=t+'\n\n'
        t=t[:-1]
    if html ==False:
        return t
    else:
        return f'''
<!doctype html>
<html>
    <head>
        <meta charset="utf-8">
        <title>Starboard Notebook</title>
        <meta name="viewport" content="width=device-width,initial-scale=1">
        <link rel="icon" href="https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/favicon.ico">
        <link href="https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/starboard-notebook.css" rel="stylesheet">
    </head>
    <body>
        <script>
            window.initialNotebookContent = {t!r}
            window.starboardArtifactsUrl = `https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/`;
        </script>
        <script src="https://cdn.jsdelivr.net/npm/starboard-notebook@0.15.2/dist/starboard-notebook.js"></script>
    </body>
</html>
'''
    r"""
    Convert a ipynb notebook (dict) to a Starboard notebook (str)
    or to a Starboard HTML document (str) if html is True.

    Usage:

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> print(to_starboard(ipynb))
        # %% [markdown]
        Hello world!
        ============
        Print `Hello world!`:
        # %% [python]
        print("Hello world!")
        # %% [markdown]
        Goodbye! 👋

        >>> html = to_starboard(ipynb, html=True)
        >>> print(html) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
        <!doctype html>
        <html>
        ...
        </html>

        >>> notebook_files = Path(".").glob("samples/*.ipynb")
        >>> for notebook_file in notebook_files:
        ...     ipynb = load_ipynb(notebook_file)
        ...     starboard_html = to_starboard(ipynb, html=True)
        ...     with open(notebook_file.with_suffix(".html"), "w", encoding="utf-8") as output:
        ...         print(starboard_html, file=output)
    """


ipynb=load_ipynb("samples/hello-world.ipynb")
print(to_starboard(ipynb))


# Outputs
# ------------------------------------------------------------------------------
def clear_outputs(ipynb):
    r"""
    Remove the notebook cell outputs and resets the cells execution counts.

    Usage:

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> pprint.pprint(ipynb)
        {'cells': [{'cell_type': 'markdown',
                    'id': 'a9541506',
                    'metadata': {},
                    'source': ['Hello world!\n',
                               '============\n',
                               'Print `Hello world!`:']},
                   {'cell_type': 'code',
                    'execution_count': 1,
                    'id': 'b777420a',
                    'metadata': {},
                    'outputs': [{'name': 'stdout',
                                 'output_type': 'stream',
                                 'text': ['Hello world!\n']}],
                    'source': ['print("Hello world!")']},
                   {'cell_type': 'markdown',
                    'id': 'a23ab5ac',
                    'metadata': {},
                    'source': ['Goodbye! 👋']}],
         'metadata': {},
         'nbformat': 4,
         'nbformat_minor': 5}
        >>> clear_outputs(ipynb)
        >>> pprint.pprint(ipynb)
        {'cells': [{'cell_type': 'markdown',
                    'id': 'a9541506',
                    'metadata': {},
                    'source': ['Hello world!\n',
                               '============\n',
                               'Print `Hello world!`:']},
                   {'cell_type': 'code',
                    'execution_count': None,
                    'id': 'b777420a',
                    'metadata': {},
                    'outputs': [],
                    'source': ['print("Hello world!")']},
                   {'cell_type': 'markdown',
                    'id': 'a23ab5ac',
                    'metadata': {},
                    'source': ['Goodbye! 👋']}],
         'metadata': {},
         'nbformat': 4,
         'nbformat_minor': 5}
    """
    for cellule in ipynb['cells']:
        if cellule['cell_type']=='code':
            cellule['outputs']=[]
            cellule['execution_count'] = None


ipynb = load_ipynb("samples/hello-world.ipynb")
pprint.pprint(ipynb)

clear_outputs(ipynb)
pprint.pprint(ipynb)


def get_stream(ipynb, stdout=True, stderr=False):
    r"""
    Return the text written to the standard output and/or error stream.

    Usage:

        >>> ipynb = load_ipynb("samples/streams.ipynb")
        >>> print(get_stream(ipynb)) # doctest: +NORMALIZE_WHITESPACE
        👋 Hello world! 🌍
        >>> print(get_stream(ipynb, stdout=False, stderr=True)) # doctest: +NORMALIZE_WHITESPACE
        🔥 This is fine. 🔥 (https://gunshowcomic.com/648)
        >>> print(get_stream(ipynb, stdout=True, stderr=True)) # doctest: +NORMALIZE_WHITESPACE
        👋 Hello world! 🌍
        🔥 This is fine. 🔥 (https://gunshowcomic.com/648)
    """
    text=''
    for dic in ipynb['cells']:
        if dic['cell_type']=='code':
            for output in dic['outputs']:
                if stdout==True:
                    if output['name']=='stdout':
                        for element in output['text']:
                            text=text+element
                            
                if stderr==True:
                    if output['name']=='stdder':
                        for element in output['text']:
                            text=text+element
    return text            


ipynb = load_ipynb("samples/Hello-world.ipynb")
print(get_stream(ipynb))


def get_exceptions(ipynb):
    liste_d_erreur=[]
    for cellule in ipynb['cells']:
        if cellule['cell_type']=='markdown':
            for output in cells[1]['outputs']:
                if output['output_type']=='error':
                    text=eval(output['ename'] + '(\"' +f"{output['evalue']}" +'\)"' )
                    liste_d_erreur.append(text)
    return liste_d_erreur
            
    
    r"""
    Return all exceptions raised during cell executions.

    Usage:

        >>> ipynb = load_ipynb("samples/hello-world.ipynb")
        >>> get_exceptions(ipynb)
        []

        >>> ipynb = load_ipynb("samples/errors.ipynb")
        >>> errors = get_exceptions(ipynb)
        >>> all(isinstance(error, Exception) for error in errors)
        True
        >>> for error in errors:
        ...     print(repr(error))
        TypeError("unsupported operand type(s) for +: 'int' and 'str'")
        Warning('🌧️  light rain')
    """



def get_images(ipynb):
    output=[]
    Liste_Cell=get_cells(ipynb)
    for cellule in Liste_Cell:
        for content in cellule['outputs']:
            try:
                str_64=content['data']['image/png']
                str_decode=base64.b64decode(str_64)
                image=PIL.Image.open(io.BytesIO(str_decode))
                output=output+[np.array(image)]
            except:
                pass
    return output
                
    r"""
    Return the PNG images contained in a notebook cells outputs
    (as a list of NumPy arrays).

    Usage:

        >>> ipynb = load_ipynb("samples/images.ipynb")
        >>> images = get_images(ipynb)
        >>> images # doctest: +ELLIPSIS
        [array([[[ ...]]], dtype=uint8)]
        >>> grace_hopper_image = images[0]
        >>> np.shape(grace_hopper_image)
        (600, 512, 3)
        >>> grace_hopper_image # doctest: +ELLIPSIS
        array([[[ 21,  24,  77],
                [ 27,  30,  85],
                [ 33,  35,  92],
                ...,
                [ 14,  13,  19]]], dtype=uint8)
    """



ipynb = load_ipynb("samples/images.ipynb")
images = get_images(ipynb)
images






