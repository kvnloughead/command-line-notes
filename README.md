# Command Line Notes

A simple command line note taking utility. It's like [tldr](https://github.com/tldr-pages/tldr) 
but without all the features, and it's completely empty until you start using it.

Basic usage

```bash
cln foo
```

opens a file `foo.md`, creating it if it doesn't already exist. Note files are saved in a directory
`~/.notes` and are subdivided by category. The default category is cheatsheet, and feel free to 
just use that. 