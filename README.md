# Yelp-Analysis

<img src="images/Yelp_RGB_fullcolor_outline.png" width="100">

### Introduction
[**Yelp**](https://en.wikipedia.org/wiki/Yelp) is a `crowd-sourced review` forum, as well as an American multinational corporation headquartered in San Francisco, 
California. It develops, hosts and markets [Yelp.com](https://www.yelp.com) and the Yelp mobile app, which publish 
`crowd-sourced reviews` about local businesses, as well as the online reservation service Yelp Reservations. 
The company also trains small businesses in how to respond to reviews, hosts social events for reviewers, and 
provides data about businesses, including health inspection scores.

### [Relationship with businesses](https://en.wikipedia.org/wiki/Yelp#Relationship_with_businesses)
A Harvard Business School study published in 2011 found that each "star" in a Yelp rating affected the business owner's 
sales by `5–9 percent`. A 2012 study by two Berkeley economists found that an increase from 3.5 to 4 stars on Yelp 
resulted in a `19 percent` increase in the chances of the restaurant being booked during peak hours. A 2014 survey of 
300 small business owners done by Yodle found that `78 percent` were concerned about negative reviews. Also, `43 percent` 
of respondents said they felt online reviews were unfair, because there is no verification that the review is written 
by a legitimate customer.

### Yelp Dataset
Yelp has released part of their data to raise an activity called 
[Yelp Dataset Challenge](https://www.yelp.com/dataset), which offers a chance for people to conduct research 
or analysis and discover what insights lie hidden in their data. Due to the size of data, this project only chooses 
yelp data partially in a zip file called **'dataset.zip'**, which contains three json files including:

- **business.json** - Contains business data including location data, attributes, and categories.
- **user.json** - User data including the user's friend mapping and all the metadata associated with the user.
- **review.json** - Contains full review text data including the user_id that wrote the review and the business_id the review 
is written for.

[Here](https://www.yelp.com/dataset/documentation/main) are the introductions of all the json files.

### Google API Key
In this project we need to use google maps, which needs a Google API key to access it. This key tells Google who you are, presumably so it can keep track of rate limits and such things. To create an API key, follow the [instructions](http://jupyter-gmaps.readthedocs.io/en/latest/authentication.html) in the documentation. Once you have an API key, pass it to gmaps before creating widgets:
```
gmaps.configure(api_key="AI...")
```
