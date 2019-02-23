Zunda Python
===================

|pyversion| |version| |license|

Zunda: Japanese Enhanced Modality Analyzer client for Python.

Zunda is an extended modality analyzer for Japanese.
For details about Zunda, See https://jmizuno.github.io/zunda/ (Written in Japanese)

this module requires installing Zunda, which is available at (https://github.com/jmizuno/zunda/releases), CaboCha (https://taku910.github.io/cabocha/), and MeCab (http://taku910.github.io/mecab/).


Contributions are welcome!


Installation
==============

::

 # Install Zunda
 wget https://github.com/jmizuno/zunda/archive/2.0b4.tar.gz
 tar xzf zunda-2.0b4.tar.gz
 rm zunda-2.0b4.tar.gz
 cd zunda-2.0b4
 ./configure
 make
 sudo make install
 cd ../
 rm -rf zunda-2.0b4

 # Install zunda-python
 pip install zunda-python

Example
===========

.. code:: python

    import zunda
    parser = zunda.Parser()
    parser.parse('花子は太郎を食事に誘った裕子が嫌いだった')
    # => [{'assumptional': '0',
      'authenticity': '成立',
      'chunks': [{'func': 'に',
        'head': '食事',
        'link_from': [],
        'link_to': 3,
        'score': 1.883877,
        'words': [{'feature': '名詞,サ変接続,*,*,*,*,食事,ショクジ,ショクジ',
          'funcexp': 'O',
          'surface': '食事'},
         {'feature': '助詞,格助詞,一般,*,*,*,に,ニ,ニ',
          'funcexp': 'B:判断',
          'surface': 'に'}]}],
      'sentiment': '0',
      'source': '筆者',
      'tense': '非未来',
      'type': '叙述',
      'word': '食事',
      'words': '食事に'},
     {'assumptional': '0',
      'authenticity': '成立',
      'chunks': [{'func': 'を',
        'head': '太郎',
        'link_from': [],
        'link_to': 3,
        'score': 1.640671,
        'words': [{'feature': '名詞,固有名詞,地域,一般,*,*,太郎,タロウ,タロー',
          'funcexp': 'O',
          'surface': '太郎'},
         {'feature': '助詞,格助詞,一般,*,*,*,を,ヲ,ヲ', 'funcexp': 'O', 'surface': 'を'}]},
       {'func': 'に',
        'head': '食事',
        'link_from': [],
        'link_to': 3,
        'score': 1.883877,
        'words': [{'feature': '名詞,サ変接続,*,*,*,*,食事,ショクジ,ショクジ',
          'funcexp': 'O',
          'surface': '食事'},
         {'feature': '助詞,格助詞,一般,*,*,*,に,ニ,ニ', 'funcexp': 'B:判断', 'surface': 'に'}]},
       {'func': 'た',
        'head': '誘っ',
        'link_from': [1, 2],
        'link_to': 4,
        'score': 1.565227,
        'words': [{'feature': '動詞,自立,*,*,五段・ワ行促音便,連用タ接続,誘う,サソッ,サソッ',
          'funcexp': 'O',
          'surface': '誘っ'},
         {'feature': '助動詞,*,*,*,特殊・タ,基本形,た,タ,タ',
          'funcexp': 'B:完了',
          'surface': 'た'}]}],
      'sentiment': '0',
      'source': '筆者',
      'tense': '非未来',
      'type': '叙述',
      'word': '誘っ',
      'words': '太郎を食事に誘った'},
     {'assumptional': '0',
      'authenticity': '成立',
      'chunks': [{'func': 'は',
        'head': '花子',
        'link_from': [],
        'link_to': 5,
        'score': -1.81792,
        'words': [{'feature': '名詞,固有名詞,人名,名,*,*,花子,ハナコ,ハナコ',
          'funcexp': 'O',
          'surface': '花子'},
         {'feature': '助詞,係助詞,*,*,*,*,は,ハ,ワ', 'funcexp': 'O', 'surface': 'は'}]},
       {'func': 'が',
        'head': '裕子',
        'link_from': [3],
        'link_to': 5,
        'score': -1.81792,
        'words': [{'feature': '名詞,固有名詞,人名,名,*,*,裕子,ユウコ,ユーコ',
          'funcexp': 'O',
          'surface': '裕子'},
         {'feature': '助詞,格助詞,一般,*,*,*,が,ガ,ガ', 'funcexp': 'O', 'surface': 'が'}]},
       {'func': 'た',
        'head': '嫌い',
        'link_from': [0, 4],
        'link_to': -1,
        'score': 0.0,
        'words': [{'feature': '名詞,形容動詞語幹,*,*,*,*,嫌い,キライ,キライ',
          'funcexp': 'O',
          'surface': '嫌い'},
         {'feature': '助動詞,*,*,*,特殊・ダ,連用タ接続,だ,ダッ,ダッ',
          'funcexp': 'B:判断',
          'surface': 'だっ'},
         {'feature': '助動詞,*,*,*,特殊・タ,基本形,た,タ,タ',
          'funcexp': 'B:完了',
          'surface': 'た'}]}],
      'sentiment': '0',
      'source': '筆者',
      'tense': '非未来',
      'type': '叙述',
      'word': '嫌い',
      'words': '花子は裕子が嫌いだった'}]

LICENSE
=========

MIT License


Copyright
=============

Zunda Python
(c) 2019- Yukino Ikegami. All Rights Reserved.

Zunda (Original version)
(c) 2013- @jmizuno

ACKNOWLEDGEMENT
=================

This module uses Zunda.
I thank to @jmizuno and Tohoku University Inui-Okazaki Lab.


.. |pyversion| image:: https://img.shields.io/pypi/pyversions/zunda-python.svg

.. |version| image:: https://img.shields.io/pypi/v/zunda-python.svg
    :target: http://pypi.python.org/pypi/zunda-python/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/zunda-python.svg
    :target: http://pypi.python.org/pypi/zunda-python/
    :alt: license
