# [![F1000 header](https://f1000research.com/img/AMP/F1000Research_image.png)](https://f1000research.com/)

# F1000Scraper

[F1000Research](https://f1000research.com/) is an open access publishing platform. It provides an [API](https://f1000research.com/developers) to extract XML or PDF of articles published in F1000Research. F1000Scraper is a python wrapper for scraping these articles as XML, and parsing the XML. 

## Usage

### Collecting data using start and end date of the articles

Currently, the only functionality we provide within this wrapper is that of collecting data using the date option in the API. After downloading the files, you can simply run the program `scrape.py` from the api directory as follows:

`python3 scrape.py <date_from> <date_to> <output_directory_path> <output_format> <keyword in the title (optional)>`

whereas

- `data_from` can be any date of the form `"dd-mm-yyyy"` or just `"*"` and defines the starting date.
- `data_to` can be any date of the form `"dd-mm-yyyy"` or just `"*"` and defines the end date.
- `output_directory` defines the path where the data files should be saved.
- `output_format` needs to be either `xml` or `pdf`
- `keyword` is an optional argument and will only download articles within the given date range where the provided keyword occurs in the title.

#### Example 1
`python3 scrape.py 01-01-2019 01-01-2020 data/ xml`

The above commmand will download articles in the XML format from 1st January 2019 to 1st January 2020, and save them to the data folder in the current directory.

#### Example 2
`python3 scrape.py 01-01-2019 * data/ pdf`

The above commmand will download articles in the PDF format from 1st January 2019 to today's date, and save them to the data folder in the current directory.


## Disclaimer

This is a work in progress. 

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
