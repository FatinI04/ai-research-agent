results = [
    {"title": "Python Guide", "url": "python.org"},
    {"title": "AI News"},
    {"title": "   ", "url": "example.com"},
    {"title": "Research", "url": " python.org "}
]


def process_results(results: list[dict]) -> list[dict]:
    list_result: list[dict] = []
    urls=set()
    for item in results: 
        if (isinstance(item.get("title"), str) and isinstance(item.get("url"), str)):
            title=item["title"].strip()
            url=item["url"].strip()
            if (title!="" and url!=""):
                if (url not in urls): 
                    value: list[dict] = {"title": title, "url": url}
                    list_result.append(value)
                    urls.add(url)

    return list_result


print(process_results(results))
            

