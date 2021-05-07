# PyCon India 2021 Website

This repo contains the code for PyCon India 2021's website.
The website is build using Hugo and contains both the hugo templates and data files related to the website

## Content Updates

The website uses data files to fill up most of the contents in the different sections of the website. Following is a brief overview for content editors to update content in the website:

- **Top Navigation**(always live): The items in the top navigation are managed by [data/nav.yml](https://github.com/pythonindia/inpycon2021/blob/main/data/nav.yml). The file has a list of link items with properties `name` and `link`. You can add, remove or update items to decide which items to show in the top navigation. Also, there are two other keys: `primary_button_text` and `primary_button_link`. These are used to decide what the primary button in the top navigation points to.
- **Hero**(always live): All the content in the hero section and about section are managed by [data/hero.yml](https://github.com/pythonindia/inpycon2021/blob/main/data/hero.yml). The `primary_button` and `secondary_button` in this file control which links and things the buttons in the hero sections points to and can be updated as needed by the content team.
- **Keynote speakers**(optional live): The contents for this section can be found at [data/keynote_speakers.yml](https://github.com/pythonindia/inpycon2021/blob/main/data/keynote_speakers.yml).To make this section live, you need to mark `live` key in the file as `true`. Apart from this, the file has a `data` key which contains the list of keynote speaker items. Each of these items have keys `name`, `affiliation` and `image`.
- **Tickets**(optional live): The contents for this section can be found at [data/tickets.yml](https://github.com/pythonindia/inpycon2021/blob/main/data/tickets.yml).To make this section live, you need to mark `live` key in the file as `true`. Apart from this, the file has a `data` key which contains the list of ticket items. Each of these items have keys:
    - `name`: ticket name
    - `details`: details about closing date, etc. for the ticket
    - `price`: price of ticket in INR
    - `category`: `conference`, `workshop` or `devsprint`. There can be only ticket each with category `workshop` and `devsprint`
    - `link`: absolute url to the ticket link
- **Outreach Partners**(optional live): The contents for this section can be found at [data/communities.yml](https://github.com/pythonindia/inpycon2021/blob/main/data/communities.yml).To make this section live, you need to mark `live` key in the file as `true`. Apart from this, the file has a `data` key which contains the list of outreach partner items. Each of these items have keys `name`, `link` and `image`.
- **Footer**(always live): The footer section has 2 sets of links - `social_links` and `quick_links`. The items in `social_links` have 3 keys: `name`(shown as title attribute or tooltip), `icon`(class name of font-awesome icon), `link`(link to the particular social media). The items in `quick_links` just have 2 attributes `name` and `link`.

## Getting Started with Development

This site is built with Hugo. For a basic introduction to git and GitHub you can follow [https://guides.github.com/introduction/git-handbook/](https://guides.github.com/introduction/git-handbook/)

- Install Hugo using the steps from [https://gohugo.io/getting-started/installing/](https://gohugo.io/getting-started/installing/).
- Fork the repository and clone to your machine by using git clone `https://github.com/- <username>/inpycon2021`.
- `cd` to the repo.
- Run `make dev`.
- Visit the local development server at [http://localhost:1313/](http://localhost:1313/).

If you are interested in contributing to the website, please check out our Contributing Guide

## Code of Conduct

As a contributor please follow the Code of Conduct to keep the community open and inclusive. Please read and follow the [PyCon India Code of Conduct](https://in.pycon.org/2020/coc/) which governs the overall conduct for the conference.