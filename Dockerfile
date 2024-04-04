FROM scrapybase

COPY ./site_search_poc ./

EXPOSE 80
# Run scrapy when the container launches

#CMD ["scrapy", "shell", "https://github.com/microsoft/playwright-python/issues/792"]
CMD ["tail", "-f", "/dev/null"]