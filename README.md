# florr.io

Welcome to the florr.io public repository, brought to you by Nautical and teddybear! This repository acts as a database of all things in florr.io, including hosting images for petals and mobs along with their corresponding statistics.

## Contributing
If you find that the information in this database is wrong or out-dated, please create a [pull request](https://github.com/NauticalTwilight/florr/pulls) for us to fix. If you are new to Git/GitHub and don't know how to create a pull request, head over to the [Issues](https://github.com/NauticalTwilight/florr/issues) tab and create an issue so that we can fix it.

## Using This Repository
The quickest way to use this repository is to browse the respective folders to find the information you need. Statistics are given as a `.JSON` file, which you will need to be able to read. All information given is as human-readable as possible.

If you want to use this repository in your code, you will need to be able to parse user information to fetch the correct database information. For images, you can fetch the raw HTTPS GitHub endpoint for this. Petal/mob statistics need to be parsed by your client-side code because they are given as a JSON file per petal.