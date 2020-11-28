def parse(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('http://example.com/?age=29') == {'age': '29'}
    assert parse('http://example.com/?name=Rodion') == {'name': 'Rodion'}
    assert parse('http://example.com/?age=19') == {'age': '19'}
    assert parse('http://example.com/?') == {'HelloWorld'}
    assert parse('http://example.com/?skill=Pro') == {'skill': 'Pro'}
    assert parse('http://example.com/?game=cs') == {'game': 'cs'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?program=self_check') == {'program': 'self_check'}
    assert parse('http://example.com/?book=DeepLearning') == {'book': 'DeepLearning'}
    assert parse('http://example.com/?author=Francois_Chollet') == {'author': 'Francois_Chollet'} 

def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
    assert parse_cookie('age=29') == {'age': '29'}
    assert parse_cookie('name=Rodion') == {'name': 'Rodion'}
    assert parse_cookie('age=19') == {'age': '19'}
    assert parse_cookie('') == {'HelloWorld'}
    assert parse_cookie('skill=Pro') == {'skill': 'Pro'}
    assert parse_cookie('game=cs') == {'game': 'cs'}
    assert parse_cookie('') == {}
    assert parse_cookie('program=self_check') == {'program': 'self_check'}
    assert parse_cookie('book=DeepLearning') == {'book': 'DeepLearning'}
    assert parse_cookie('author=Francois_Chollet') == {'author': 'Francois_Chollet'}