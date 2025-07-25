pip install wikipedia

    import wikipedia
    
    results = wikipedia.search("Python programming language")
    print(results)
    
    page = wikipedia.page("Python (programming language)")
    print(page.title)
    print(page.summary)
    
    links = page.links
    print(links)
