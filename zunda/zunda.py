# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE


class Parser(object):
    """Zunda: Japanese Enhanced Modality Analyzer

    Zunda is an extended modality analyzer for Japanese.
    Please see details in https://jmizuno.github.io/zunda/ (written in Japanese)
    And this module requires installing Zunda, which is available at https://github.com/jmizuno/zunda/releases

    >>> import zunda
    >>> parser = zunda.Parser()
    >>> parser.parse('花子は太郎を食事に誘った裕子が嫌いだった')
    [{'assumptional': '0',
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
    """

    def __init__(self, zunda_args='', encoding='utf-8'):
        """
        Params:
            zunda_args (str) : argument for zunda
            encoding (str) : character encoding (default utf-8)
        """
        self.zunda_args = zunda_args
        self.encoding = encoding

    def _parse_zunda_return(self, zunda_return):
        events = []
        chunks = []
        word_count = 0
        for line in zunda_return.splitlines()[:-1]:  # The last line is EOS
            if not line:
                continue
            elif line.startswith('#FUNCEXP'):
                funcexp_str = line.split('\t')[1]
                funcexp = funcexp_str.split(',')
            elif line.startswith('#EVENT'):
                event_info = line.split('\t')
                event = {'word': int(event_info[1]), 'source': event_info[2].split(':')[1],
                         'tense': event_info[3], 'assumptional': event_info[4],
                         'type': event_info[5], 'authenticity': event_info[6],
                         'sentiment': event_info[7], 'chunks': []}
                events.append(event)
            elif line.startswith('* '):
                chunk_info = line.split(' ')
                chunk = {'link_to': int(chunk_info[2][:-1]), 'link_from': [],
                         'head': int(chunk_info[3].split('/')[0]),
                         'func': int(chunk_info[3].split('/')[1]),
                         'score': float(chunk_info[4]), 'words': []}
                chunks.append(chunk)
            else:
                (surface, feature) = line.split('\t')
                chunks[-1]['words'].append({'surface': surface, 'feature': feature,
                                            'funcexp': funcexp[word_count]})
                word_count += 1

        for (i, chunk) in enumerate(chunks):
            if chunk['link_to'] != -1:
                chunks[chunk['link_to']]['link_from'].append(i)
            chunks[i]['head'] = chunk['words'][chunks[i]['head']]['surface']
            chunks[i]['func'] = chunk['words'][chunks[i]['func']]['surface']

        word_count = 0
        for (i, event) in enumerate(events):
            for (j, chunk) in enumerate(chunks):
                for word in chunk['words']:
                    if event['word'] == word_count:
                        events[i]['word'] = word['surface']
                        for link_chunk in chunk['link_from']:
                            events[i]['chunks'].append(chunks[link_chunk])
                        events[i]['chunks'].append(chunk)
                        events[i]['words'] = ''.join([word['surface'] for chunk in events[i]['chunks'] for word in chunk['words']])
                    word_count += 1
            word_count = 0
        return events

    def parse(self, sentence):
        """Parse the sentence
        Param:
            sentence (str)
        Return:
            events (list of dict)
        """
        cmd = 'echo %s| zunda %s' % (sentence, self.zunda_args)
        with Popen(cmd, shell=True, stdout=PIPE) as proc:
            zunda_return = proc.communicate()[0].decode(self.encoding)
        events = self._parse_zunda_return(zunda_return)
        return events
