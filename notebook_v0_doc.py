    # Help on module notebook_v0:

    # NAME
    # notebook_v0 - starter code for your evaluation assignment

    # FUNCTIONS
    #     clear_outputs(ipynb)
    #         Remove the notebook cell outputs and resets the cells execution counts.
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> pprint.pprint(ipynb)
    #             {'cells': [{'cell_type': 'markdown',
    #                         'id': 'a9541506',
    #                         'metadata': {},
    #                         'source': ['Hello world!\n',
    #                                 '============\n',
    #                                 'Print `Hello world!`:']},
    #                     {'cell_type': 'code',
    #                         'execution_count': 1,
    #                         'id': 'b777420a',
    #                         'metadata': {},
    #                         'outputs': [{'name': 'stdout',
    #                                     'output_type': 'stream',
    #                                     'text': ['Hello world!\n']}],
    #                         'source': ['print("Hello world!")']},
    #                     {'cell_type': 'markdown',
    #                         'id': 'a23ab5ac',
    #                         'metadata': {},
    #                         'source': ['Goodbye! \U0001f44b']}],
    #             'metadata': {},
    #             'nbformat': 4,
    #             'nbformat_minor': 5}
    #             >>> clear_outputs(ipynb)
    #             >>> pprint.pprint(ipynb)
    #             {'cells': [{'cell_type': 'markdown',
    #                         'id': 'a9541506',
    #                         'metadata': {},
    #                         'source': ['Hello world!\n',
    #                                 '============\n',
    #                                 'Print `Hello world!`:']},
    #                     {'cell_type': 'code',
    #                         'execution_count': None,
    #                         'id': 'b777420a',
    #                         'metadata': {},
    #                         'outputs': [],
    #                         'source': ['print("Hello world!")']},
    #                     {'cell_type': 'markdown',
    #                         'id': 'a23ab5ac',
    #                         'metadata': {},
    #                         'source': ['Goodbye! \U0001f44b']}],
    #             'metadata': {},
    #             'nbformat': 4,     
    #             'nbformat_minor': 5}
        
    #     get_cells(ipynb)
    #         Return the notebook cells.
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/minimal.ipynb")
    #             >>> cells = get_cells(ipynb)
    #             >>> cells
    #             []
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> cells = get_cells(ipynb)
    #             >>> pprint.pprint(cells)
    #             [{'cell_type': 'markdown',
    #             'id': 'a9541506',
    #             'metadata': {},
    #             'source': ['Hello world!\n', '============\n', 'Print `Hello world!`:']},
    #             {'cell_type': 'code',
    #             'execution_count': 1,
    #             'id': 'b777420a',
    #             'metadata': {},
    #             'outputs': [{'name': 'stdout',
    #                         'output_type': 'stream',
    #                         'text': ['Hello world!\n']}],
    #             'source': ['print("Hello world!")']},
    #             {'cell_type': 'markdown',
    #             'id': 'a23ab5ac',
    #             'metadata': {},
    #             'source': ['Goodbye! \U0001f44b']}]
        
    #     get_exceptions(ipynb)
    #         Return all exceptions raised during cell executions.
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> get_exceptions(ipynb)
    #             []
            
    #             >>> ipynb = load_ipynb("samples/errors.ipynb")
    #             >>> errors = get_exceptions(ipynb)
    #             >>> all(isinstance(error, Exception) for error in errors)
    #             True
    #             >>> for error in errors:
    #             ...     print(repr(error))
    #             TypeError("unsupported operand type(s) for +: 'int' and 'str'")
    #             Warning('\U0001f327\ufe0f  light rain')
        
    #     get_format_version(ipynb)
    #         Return the format version (str) of a jupyter notebook (dict).
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/minimal.ipynb")
    #             >>> get_format_version(ipynb)
    #             '4.5'
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> get_format_version(ipynb)
    #             '4.5'
        
    #     get_images(ipynb)
    #         Return the PNG images contained in a notebook cells outputs
    #         (as a list of NumPy arrays).
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/images.ipynb")
    #             >>> images = get_images(ipynb)
    #             >>> images # doctest: +ELLIPSIS
    #             [array([[[ ...]]], dtype=uint8)]
    #             >>> grace_hopper_image = images[0]
    #             >>> np.shape(grace_hopper_image)
    #             (600, 512, 3)
    #             >>> grace_hopper_image # doctest: +ELLIPSIS
    #             array([[[ 21,  24,  77],
    #                     [ 27,  30,  85],
    #                     [ 33,  35,  92],
    #                     ...,
    #                     [ 14,  13,  19]]], dtype=uint8)
        
    #     get_metadata(ipynb)
    #         Return the global metadata of a notebook.
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/metadata.ipynb")
    #             >>> metadata = get_metadata(ipynb)
    #             >>> pprint.pprint(metadata)
    #             {'celltoolbar': 'Edit Metadata',
    #             'kernelspec': {'display_name': 'Python 3 (ipykernel)',
    #                             'language': 'python',
    #                             'name': 'python3'},
    #             'language_info': {'codemirror_mode': {'name': 'ipython', 'version': 3},
    #                             'file_extension': '.py',
    #                             'mimetype': 'text/x-python',
    #                             'name': 'python',
    #                             'nbconvert_exporter': 'python',
    #                             'pygments_lexer': 'ipython3',
    #                             'version': '3.9.7'}}
        
    #     get_stream(ipynb, stdout=True, stderr=False)
    #         Return the text written to the standard output and/or error stream.
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/streams.ipynb")
    #             >>> print(get_stream(ipynb)) # doctest: +NORMALIZE_WHITESPACE
    #             \U0001f44b Hello world! \U0001f30d
    #             >>> print(get_stream(ipynb, stdout=False, stderr=True)) # doctest: +NORMALIZE_WHITESPACE
    #             \U0001f525 This is fine. \U0001f525 (https://gunshowcomic.com/648)
    #             >>> print(get_stream(ipynb, stdout=True, stderr=True)) # doctest: +NORMALIZE_WHITESPACE
    #             \U0001f44b Hello world! \U0001f30d
    #             \U0001f525 This is fine. \U0001f525 (https://gunshowcomic.com/648)
        
    #     load_ipynb(filename)
    #         Load a jupyter notebook .ipynb file (JSON) as a Python dict.
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/minimal.ipynb")
    #             >>> ipynb
    #             {'cells': [], 'metadata': {}, 'nbformat': 4, 'nbformat_minor': 5}
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> pprint.pprint(ipynb)
    #             {'cells': [{'cell_type': 'markdown',
    #                         'id': 'a9541506',
    #                         'metadata': {},
    #                         'source': ['Hello world!\n',
    #                                 '============\n',
    #                                 'Print `Hello world!`:']},
    #                     {'cell_type': 'code',
    #                         'execution_count': 1,
    #                         'id': 'b777420a',
    #                         'metadata': {},
    #                         'outputs': [{'name': 'stdout',
    #                                     'output_type': 'stream',
    #                                     'text': ['Hello world!\n']}],
    #                         'source': ['print("Hello world!")']},
    #                     {'cell_type': 'markdown',
    #                         'id': 'a23ab5ac',
    #                         'metadata': {},
    #                         'source': ['Goodbye! \U0001f44b']}],
    #             'metadata': {},
    #             'nbformat': 4,
    #             'nbformat_minor': 5}
        
    #     save_ipynb(ipynb, filename)
    #         Save a jupyter notebook (Python dict) as a .ipynb file (JSON)
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/minimal.ipynb")
    #             >>> ipynb
    #             {'cells': [], 'metadata': {}, 'nbformat': 4, 'nbformat_minor': 5}
    #             >>> ipynb["metadata"]["clone"] = True
    #             >>> save_ipynb(ipynb, "samples/minimal-save-load.ipynb")
    #             >>> load_ipynb("samples/minimal-save-load.ipynb")
    #             {'cells': [], 'metadata': {'clone': True}, 'nbformat': 4, 'nbformat_minor': 5}
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> save_ipynb(ipynb, "samples/hello-world-save-load.ipynb")
    #             >>> ipynb == load_ipynb("samples/hello-world-save-load.ipynb")
    #             True
        
    #     starboard_html(code)
        
    #     to_percent(ipynb)
    #         Convert a ipynb notebook (dict) to a Python code in the percent format (str).
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> print(to_percent(ipynb)) # doctest: +NORMALIZE_WHITESPACE
    #             # %% [markdown]
    #             # Hello world!
    #             # ============
    #             # Print `Hello world!`:
    #             # %%
    #             print("Hello world!")
    #             # %% [markdown]
    #             # Goodbye! \U0001f44b
            
    #             >>> notebook_files = Path(".").glob("samples/*.ipynb")
    #             >>> for notebook_file in notebook_files:
    #             ...     ipynb = load_ipynb(notebook_file)
    #             ...     percent_code = to_percent(ipynb)
    #             ...     with open(notebook_file.with_suffix(".py"), "w", encoding="utf-8") as output:
    #             ...         print(percent_code, file=output)
        
    #     to_starboard(ipynb, html=False)
    #         Convert a ipynb notebook (dict) to a Starboard notebook (str)
    #         or to a Starboard HTML document (str) if html is True.
            
    #         Usage:
            
    #             >>> ipynb = load_ipynb("samples/hello-world.ipynb")
    #             >>> print(to_starboard(ipynb))
    #             # %% [markdown]
    #             Hello world!
    #             ============
    #             Print `Hello world!`:
    #             # %% [python]
    #             print("Hello world!")
    #             # %% [markdown]
    #             Goodbye! \U0001f44b
            
    #             >>> html = to_starboard(ipynb, html=True)
    #             >>> print(html) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    #             <!doctype html>
    #             <html>
    #             ...
    #             </html>
            
    #             >>> notebook_files = Path(".").glob("samples/*.ipynb")
    #             >>> for notebook_file in notebook_files:
    #             ...     ipynb = load_ipynb(notebook_file)
    #             ...     starboard_html = to_starboard(ipynb, html=True)
    #             ...     with open(notebook_file.with_suffix(".html"), "w", encoding="utf-8") as output:
    #             ...         print(starboard_html, file=output)

    # FILE
    #     c:\users\pierre claudet\desktop\projets\python-advanced\python-advanced-evaluation-groupe5\notebook_v0.py


