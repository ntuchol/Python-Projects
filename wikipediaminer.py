pip install wikipedia

    import wikipedia
    
    # Search for a page
    results = wikipedia.search("Python programming language")
    print(results)
    
    # Get a specific page
    page = wikipedia.page("Python (programming language)")
    print(page.title)
    print(page.summary)
    
    # Extract links from a page
    links = page.links
    print(links)