from src.processor import process_results

def test_valid_results(): 
    results = [
    {"title": "Python Guide", "url": "python.org"},
    {"title": "Research", "url": " python1.org "}
    ]
    assert process_results(results) == [{'title': 'Python Guide', 'url': 'python.org'}, {"title": "Research", "url": "python1.org"}]




def test_duplicate_urls():
    results = [
        {"title": "Python Guide", "url": "python.org"},
        {"title": "Research", "url": " python.org "}
        ]
    assert process_results(results) == [{'title': 'Python Guide', 'url': 'python.org'}]




def test_missing_keys():
    results = [
            {"title": "Python Guide", "url": "python.org"},
            {"url": " python.org "},
            {"title": "Research"}
            ]
    assert process_results(results) == [{'title': 'Python Guide', 'url': 'python.org'}]




def test_whitespace():
    results = [
                {"title": "      ", "url": "python.org"},
                {"title": "Python Guide", "url": "     "},
                {"title": "        Python Guide   ", "url": "     python.org "}
                ]
    assert process_results(results) == [{'title': 'Python Guide', 'url': 'python.org'}]




def test_empty_input():
    results = []
    assert process_results(results) == []

