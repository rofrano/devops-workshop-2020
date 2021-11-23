# Issues for Workshop

This folder contains an export of the issues used in the DevOps Workshop.

Import/Export Tool
https://github.com/gavinr/github-csv-tools

## Export/Import Issues

Import and export GitHub issues via CSV (https://github.com/gavinr/github-csv-tools)

Prerequisite:  [Install Node.js](https://nodejs.org/en/).

On a Mac you can use [homebrew](http://brew.sh) to do install Node cleanly if you don't already have it:

```bash
brew install node
```

Then run this to install GitHub CSV Tools:

```sh
npm install -g github-csv-tools
```

After install, `githubCsvTools --help` for info on how to use, or see below.

Instructions for exporting or importing:

### To Export Issues

This will export all stories to a file called timestamp-issues.csv

```sh
githubCsvTools -t <token> -o <org> -r <repo>
```

For exmple to export from this repo use the following where `$GIT_TOKEN` is an environment variable that contains your GitHub token for authentication. 

To create a token, go to your GitHub account under **Settings | Developer settings | Personal access tokens** and press the **Generate new token** button. Then set the enironment variable `GET_TOKEN` to the value.

```sh
githubCsvTools -t $GIT_TOKEN -o rofrano -r devops-workshop-2020
```

### To Import Issues

Currently imports title, body, labels, status (closed or open) and milestones.

```sh
githubCsvTools github-issues.csv -t $GIT_TOKEN -o rofrano -r devops-workshop-2020
```
