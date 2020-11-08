# [![F1000 header](https://f1000research.com/img/AMP/F1000Research_image.png)](https://f1000research.com/)

# F1000Scraper

[F1000Research](https://f1000research.com/) is an open access publishing platform. It provides an [API](https://f1000research.com/developers) to extract XML or PDF of articles published in F1000Research. F1000Scraper is a python wrapper for scraping these articles as XML, and parsing the XML. 

<!-- ## Sample

Scrape defines traversal functions like `Find` and `FindAll` while attempting
to be generic. It also defines convenience functions such as `Attr` and `Text`.

```go
// Parse the page
root, err := html.Parse(resp.Body)
if err != nil {
    // handle error
}
// Search for the title
title, ok := scrape.Find(root, scrape.ByTag(atom.Title))
if ok {
    // Print the title
    fmt.Println(scrape.Text(title))
}
```

## A full example: Scraping Hacker News

```go
package main

import (
	"fmt"
	"net/http"

	"github.com/yhat/scrape"
	"golang.org/x/net/html"
	"golang.org/x/net/html/atom"
)

func main() {
	// request and parse the front page
	resp, err := http.Get("https://news.ycombinator.com/")
	if err != nil {
		panic(err)
	}
	root, err := html.Parse(resp.Body)
	if err != nil {
		panic(err)
	}

	// define a matcher
	matcher := func(n *html.Node) bool {
		// must check for nil values
		if n.DataAtom == atom.A && n.Parent != nil && n.Parent.Parent != nil {
			return scrape.Attr(n.Parent.Parent, "class") == "athing"
		}
		return false
	}
	// grab all articles and print them
	articles := scrape.FindAll(root, matcher)
	for i, article := range articles {
		fmt.Printf("%2d %s (%s)\n", i, scrape.Text(article), scrape.Attr(article, "href"))
	}
}
``` -->

## Contributors

- Shahan Ali Memon
- Bedoor AlShebli

<!-- [![Stargazers repo roster for @waylonwalker/waylonwalker](https://reporoster.com/stars/waylonwalker/waylonwalker)](https://github.com/waylonwalker/waylonwalker/stargazers) -->
